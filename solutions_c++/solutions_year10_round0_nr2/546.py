#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string>
#include <iostream>
using namespace std;
FILE	*fin = stdin;//fopen( "xxx.in" , "r" );
FILE	*fout = stdout;//fopen( "xxx.out" , "w" );
const int maxn = 2000;
const int maxLen = 100;
class	bign
{
	public:
	int len;
	int s[maxLen];
	bign()
	{
		memset( s , 0 , sizeof(s) );
		len = 1;
	}
	void	clean()
	{
		len = maxLen - 1;
		while ( len > 1 && !s[ len - 1 ] ) len --;
	}
	bign operator = ( string b )
	{
		memset( s , 0 , sizeof(s) );
		len = b.length();
		for ( int i = 0 ; i < len ; i ++ )
			s[i] = (int)( b[ len - i - 1 ] - '0' );
		clean();
	}
	bign operator = ( int b )
	{
		memset( s , 0 , sizeof(s) );
		len = 0;
		if ( b == 0 ) len = 1;
		while (b)
		{
			s[ len ++ ] = b % 10;
			b /= 10;
		}
	}
	bool operator > (bign b)
	{
		if ( len != b.len ) return len > b.len;
		for ( int i = len - 1 ; i >= 0 ; i -- )
			if ( s[i] != b.s[i] ) return s[i] > b.s[i];
		return 0;
	}

	bool operator >= (bign b)
	{
		if ( len != b.len ) return len > b.len;
		for ( int i = len - 1 ; i >= 0 ; i -- )
			if ( s[i] != b.s[i] ) return s[i] > b.s[i];
		return 1;
	}
	bool operator > (int b)
	{
		bign tmp;
		tmp = b;
		return *this > tmp;
	}
	bool operator == (bign b)
	{
		if (b.len != len) return false;
		for (int i = 0; i < len; i ++)
			if (s[i] != b.s[i]) return false;
		return 1;
	}
	bool operator == ( int b )
	{
		bign tmp;
		tmp = b;
		return *this == tmp;
	}
	bign operator - ( bign b )
	{
		bign c;
		c.len = 0;
		int g = 0;
		for ( int i = 0 ; i < len ; i ++ )
		{
			int x = s[i] - g;
			if ( i < b.len )	x -= b.s[i];
			if ( x >= 0 )	g = 0;
			else
			{
				x += 10;
				g = 1;
			}
			c.s[ c.len ++ ] = x;
		}
		c.clean();
		return c;
	}
	bign operator * ( bign b )
	{
		bign c;
		c.len = len + b.len;
		for ( int i = 0 ; i < len ; i ++ )
			for ( int j = 0 ; j < b.len ; j ++)
				c.s[i + j] += s[i] * b.s[j];
		for ( int i = 0 ; i < c.len - 1 ; i ++ )
		{
			c.s[i + 1] += c.s[i] / 10;
			c.s[i] %= 10;
		}
		c.clean();
		return c;
	}
	bign operator * ( int b )
	{
		bign c;
		for ( int i = 0 ; i < len ; i ++ )
			c.s[i] = s[i] * b;
		for ( int i = 0 ; i < maxLen ; i ++ )
		{
			c.s[i + 1] += c.s[i] / 10;
			c.s[i] %= 10;
		}
		c.clean();
		return c;
	}
	bign operator + ( int b )
	{
		bign c;
		c = *this;
		c.s[0] += b;
		for ( int i = 0 ; i < maxLen ; i ++ )
		{
			c.s[i + 1] += c.s[i] / 10;
			c.s[i] %= 10;
		}
		c.clean();
		return c;
	}
	bign operator / ( bign b )
	{
		bign c , t;
		t.len = b.len;
		for ( int i = 0 ; i < t.len ; i ++ ) 	t.s[i] = s[len - b.len + i];
		for ( int i = len - b.len ; i >= 0 ; i -- )
		{
			int x;
			for ( x = 9 ; x >= 0 ; x -- )
				if ( t >= b * x ) break;
			c.s[i] = x;
			t = t - b * x;
			if ( i > 0 )	t = t * 10 + s[ i - 1 ];
		}
		c.clean();
		return c;
	}
	bign operator % ( bign b )
	{
		bign c;
		c = *this / b;
		return *this - b * c;
	}
};
bign a[maxn];
bign b[maxn * maxn];
int tot;

bign 	gcd( bign a , bign b )
{
	if ( b > a )
	{
		bign t = a;
		a = b;
		b = t;
	}
	while ( b > 0 )
	{
		bign x = a % b;
		a = b;
		b = x;
	}
	return a;
}

int	main()
{
	int	C , temp = 0;
	fscanf( fin , "%d\n" , &C );
	while (C)
	{
		tot = 0;
		temp ++;
		C --;
		fprintf( fout , "Case #%d: " , temp );
		int N;
		fscanf( fin , "%d" , &N );
		for (int i = 1; i <= N; i ++)
		{
			string tmp;
			cin >> tmp;
			a[i] = tmp;
		}
		for ( int i = 1 ; i <= N ; i ++ )
			for ( int j = i + 1 ; j <= N ; j ++ )
				if ( a[i] > a[j] )
					b[ ++ tot ] = a[i] - a[j];
				else 
					b[ ++ tot ] = a[j] - a[i];

		bign x = b[1];
		for ( int i = 2 ; i <= tot ; i ++ )
			x = gcd( x , b[i] );
		if ( x == 1 || a[1] % x == 0 )	fprintf( fout , "0\n" );
		else
		{
			bign y = x - a[1] % x;
			for ( int i = y.len - 1 ; i >= 0 ; i -- )
				fprintf( fout , "%d" , y.s[i] );
			fprintf( fout , "\n");
		}
	}
}
