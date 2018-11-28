#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;

const int size = 52;
const char base = '0';


class bn
{
public:
	char data[size];
	int len;
	bn( )
	{
		data[0] = base;
		data[1] = '\0';
		len = 1;
	}
	bn( const char* tp )
	{
		strcpy( data, tp );
		len = strlen( tp );
	}
	bn( const bn& tmp )
	{
		int i;
		for( i=0; i<=tmp.len; ++i )
			data[i] = tmp.data[i];
		len = tmp.len;
	}
	bn& operator=( const bn& tmp )
	{
		int i;
		for( i=0; i<=tmp.len; ++i )
			data[i] = tmp.data[i];
		len = tmp.len;
		return *this;
	}
	void rev( )
	{
		int i = 0;
		int j = len - 1;
		char tmp;
		while( i<j )
		{
			tmp = data[i];
			data[i] = data[j];
			data[j] = tmp;
			i++;
			j--;
		}
	}
	friend ostream& operator<<( ostream& os, const bn& tmp )
	{
		os << tmp.data;
		return os;
	}
	friend istream& operator>>( istream& is, bn& tmp )
	{
		is >> tmp.data;
		tmp.len = strlen( tmp.data );
		return is;
	}
	
};
bn operator+( const bn& t1, const bn& t2 )
{
	bn result;
	int i = 0;
	int tp = 0;
	
	while( i<t1.len && i<t2.len )
	{
		tp += t1.data[i] + t2.data[i] - 2 * base;
		result.data[i] = tp % 10 + base;
		tp /= 10;
		i++;
	}
	while( i<t1.len )
	{
		tp += t1.data[i] - base;
		result.data[i] = base + tp % 10;
		tp /= 10;
		i++;
	}
	while( i<t2.len )
	{
		tp += t2.data[i] - base;
		result.data[i] = base + tp % 10;
		tp /= 10;
		i++;
	}
	if( tp )
	{
		result.data[i] = tp % 10 + base;
		i++;
	}
	result.data[i] = '\0';
	result.len = i;
	return result;
}
bn operator-( const bn& t1, const bn& t2 ) // t1>=t2 t1 - t2
{
	bn result;
	int tp = 0;
	int i = 0;
	while( i<t2.len )
	{
		result.data[i] = tp + base + t1.data[i] - t2.data[i];
		if( result.data[i]<base )
		{
			tp = -1;
			result.data[i] += 10;
		}
		else 
			tp = 0;
		i++;
	}
	while( i<t1.len  )
	{
		result.data[i] = t1.data[i] + tp;
		if( result.data[i] < base )
		{
			tp = -1;
			result.data[i] += 10;
		}
		else
		{
			tp = 0;
		}
		i++;
	}
	for( i=t1.len-1; i>=0&&result.data[i]==base; --i )
		;
	if( i==-1 )
	{
		result.data[0] = base;
		result.data[1] = '\0';
		result.len = 1;
	}
	else
	{
		result.data[i+1] = '\0';
		result.len = i + 1;
	}
	return result;
	
}


bn operator<<( const bn& t, const int bit )
{
	bn result;
	int i;
	for( i=0; i<bit; ++i )
		result.data[i] = base;
	result.len = i;
	for( i=0; i<=t.len; ++i )
		result.data[i+result.len] = t.data[i];
	result.len = bit + t.len;
	return result;
}
bool operator==( const bn& t1, const bn& t2 )
{
	if( t1.len==t2.len )
	{
		int i;
		for( i=0; i<t1.len; ++i )
			if( t1.data[i]!=t2.data[i] )
				return false;
			return true;
	}
	return false;
}

bool operator<=( const bn& t1, const bn& t2 )
{
	if( t1.len==t2.len )
	{
		int i = t1.len-1;
		while( i>=0 )
		{
			if( t1.data[i]==t2.data[i] )
				i--;
			else 
				return t1.data[i]<t2.data[i];
		}
		return true;
	}
	else
		return t1.len<t2.len;
}

bn operator%( bn t1, bn t2 )
{
	bn result("0");
	bn tmp("0");
	
	bn add;
	int i = t1.len - t2.len;
	while( i!=-1 )
	{
		
		add = ( t2<<i );
		
		tmp = result + add;
		
		while( tmp<=t1 )
		{
			result = tmp;
			tmp = result + add;
			
		}
		i--;
	}
	return t1-result;
	
}


bn gcd( bn t1, bn t2 )
{
	
	if( t2==bn("0") )
		return t1;
	bn tmp;
	tmp = t1 % t2;
	while( !(tmp==bn("0")) )
	{
		t1 = t2;
		t2 = tmp;
		tmp = t1 % t2;
		
		
	}
	return t2;
}
bool compare( const bn& t1, const bn& t2 )
{
	if( t1.len==t2.len )
	{
		int i = t1.len-1;
		while( i>=0 )
		{
			if( t1.data[i]==t2.data[i] )
				i--;
			else 
				return t1.data[i]<t2.data[i];
		}
		return false;
	}
	else
		return t1.len<t2.len;
}

const int MAX = 1003;

int main( )
{
	
	// open file
	ifstream in( "in.txt" );
	ofstream out( "out.txt" );
	
	bn da[MAX];
	int N, n;
	int c, C;
	
	in >> C;
	for( c=1; c<=C; ++c )
	{
		in >> N;
		for( n=1; n<=N; ++n )
			in >> da[n];
		
		for( n=1; n<=N; ++n )
			da[n].rev( );

		sort( &da[1], &da[N+1], compare );
		
		for( n=1; n<=N-1; ++n )
			da[n-1] = da[n+1] - da[n];
		
		bn res = da[0];
		
		for( n=1; n<N-1; ++n )
			if( res<=da[n] )
				res = gcd( da[n], res );
			else
				res = gcd( res, da[n] );
			
			bn tt = da[N] % res;
			
			if( tt==bn("0") )
				res = bn("0");
			else
				res = res - tt;
			res.rev( );
			out << "Case #" << c << ": " << res << endl;
			
	}
	
	// close file
	in.close( );
	out.close( );
	
	return 0;
}
