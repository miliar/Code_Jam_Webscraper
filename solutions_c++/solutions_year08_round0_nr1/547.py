#include<cstdio>
#include<string>
#include<iostream>

using namespace std;

string search[ 101 ];
string query[ 1001 ];

int n, m;

#define INF 1 << 30

int dp[ 1002 ][ 101 ];

int _min( int index )
{
	int res = 1 << 30;
	for( int j = 0; j < n; ++j )
	{
		if( dp[ index ][ j ] < res )
			res = dp[ index ][ j ];
	}
	return res;
}
int solve()
{
	int res = 0;
	for( int cur = 0; cur < m; ++res )
	{
		int best = -1;
		for( int i = 0; i < n; ++i )
		{
			int len = 0;
			int j;
			for( j = cur; j < m; ++j, ++len )
				if( search[ i ] == query[ j ] ) break;
			if( j - cur > best )
				best = j - cur;
		}
		cur += best;
	}
	/*for( int i = 1; i <= m; ++i )
	{
		for( int j = 0; j < n; ++j )	
		{
			if( query[ i - 1 ] == search[ j ] ) 
				dp[ i ][ j ] = _min( i - 1 );
			else
				dp[ i ][ j ] = dp[ i - 1 ][ j ];
		}
	}
	int res = 1 << 30;
	for( int i = 0; i < n; ++i )
		if( dp[ m ][ i ] < res )
			res = dp[ m ][ i ];*/
	if( !m ) return 0;
	return res - 1;
}
int main()
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int t;
	cin >> t;
	int ind = 1;
	for( ; t; --t )
	{
		//cin >> n >> m;
		scanf( "%d\n", & n );
		for( int i = 0; i < n; ++i )
			getline( cin, search[ i ] );
		scanf( "%d\n", & m );
		for( int j = 0; j < m; ++j )
			getline( cin, query[ j ] );
		printf( "Case #%d: %d\n", ind, solve() );
		++ind;	
	}
	return 0;
}