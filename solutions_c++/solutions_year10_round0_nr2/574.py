#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
#include <memory.h>
#include <set>
#include <map>
using namespace std;

#define lint long long

#define file ""

const int MAXL = 55;
const int MAXN = 1005;

struct big
{
	int l;
	int a[MAXL];
	big()
	{
		l = 0;
		memset( a, 0, sizeof( a ) );
	}
	bool operator <( const big &b ) const
	{
		if ( l != b.l )
			return l < b.l;
		int i;
		for ( i = l - 1; i >= 0; i-- )
		{
			if ( a[i] != b.a[i] )
				return a[i] < b.a[i];
		}
		return false;
	}
	big operator -( const big &b ) const
	{
		if ( operator <( b ) )
			return *this;
		big c;
		int i;
		for ( i = 0; i < l; i++ )
		{
			c.a[i] += a[i] - b.a[i];
			while ( c.a[i] < 0 )
			{
				c.a[i] += 10;
				c.a[i + 1]--;
			}
		}
		c.l = l;
		while ( c.l > 0 && c.a[c.l - 1] == 0 )
			c.l--;
		return c;
	}
	void operator <<=( int n )
	{
		int i;
		for ( i = l - 1; i >= 0; i-- )
			a[i + n] = a[i];
		for ( i = n - 1; i >= 0; i-- )
			a[i] = 0;
		l += n;
		return;
	}
	void operator >>=( int n )
	{
		int i;
		for ( i = 0; i < l; i++ )
			a[i] = a[i + n];
		l -= n;
		if ( l < 0 )
			l = 0;
		memset( a + l, 0, sizeof( a ) - sizeof( int ) * l );
		return;
	}
	big operator %( big b ) const
	{
		if ( operator <( b ) )
			return *this;
		big c = *this;
		int i;
		i = b.l;
		b <<= l - b.l;
		while ( i <= b.l )
		{
			while ( !( c < b ) )
				c = c - b;
			b >>= 1;
		}
		while ( c.l > 0 && c.a[c.l - 1] == 0 )
			c.l--;
		return c;
	}
	void operator ++( )
	{
		memset( a, 0, sizeof( a ) );
		do
		{
			a[0] = getchar( );
		}
		while ( a[0] < '0' || a[0] > '9' );
		l = 0;
		do
		{
			a[l + 1] = getchar( );
			a[l] -= '0';
			++l;
		}
		while ( a[l] >= '0' && a[l] <= '9' );
		a[l] = 0;
		reverse( a, a + l );
		return;
	}
	void operator --( ) const
	{
		int i;
		if ( l == 0 )
			putchar( '0' );
		for ( i = l - 1; i >= 0; i-- )
			putchar( a[i] + '0' );
		putchar( '\n' );
		return;
	}
};

big gcd( big a, big b )
{
	return b.l == 0 ? a : gcd( b, a % b );
}

void prepare( )
{
	#ifdef _DEBUG
		freopen( "in.txt", "r", stdin );
	#else
		freopen( "input.txt", "r", stdin );
		freopen( "output.txt", "w", stdout );
	#endif
}

big a[MAXN];

bool solve( )
{
	int i, n;
	scanf( "%d", &n );
	for ( i = 0; i < n; i++ )
		++a[i];
	sort( a, a + n );
	big res;
	for ( i = 1; i < n; i++ )
		res = gcd( res, a[i] - a[i - 1] );
	big z;
	z = a[0] % res;
	if ( z.l != 0 )
		res = res - z;
	else
		res = z;
	--res;
	return true;
}

int main( )
{
	prepare( );
	int i, t;
	scanf( "%d", &t );
	for ( i = 0; i < t; i++ )
	{
		printf( "Case #%d: ", i + 1 );
		solve( );
	}
	return 0;
}