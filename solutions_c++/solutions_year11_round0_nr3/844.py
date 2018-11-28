#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

#define MAXN 1010

//int dp[ MAXN ][ 2 ];
int num[ MAXN ];

/*
int DP( int k, int x, int now, int remain )
{
	
	bool state = now == remain;

	if ( ( !k || !x ) && state )
		return 0;

	if ( !k || !x )
		return -1e9;

	if ( dp[ k ][ state ] != -1 )
		return dp[ k ][ state ];
	
	dp[ k ][ state ] = max( DP( k - 1, x, now, remain ), DP( k - 1, x - 1, now ^ num[ k ], remain ^ num[ k ] ) + num[ k ] );

	return dp[ k ][ state ];
}
*/
	


int main()
{
	freopen( "C.out", "w", stdout );
	int test;
	scanf( "%d", &test );

	for ( int t = 0; t < test; ++t )
	{
		int n;
		scanf( "%d", &n );
		int sum = 0;
		for ( int i = 1; i <= n; ++i )
			scanf( "%d", &num[ i ] ), sum ^= num[ i ];
		
		if ( sum )
		{
			printf( "Case #%d: NO\n", t + 1 );
			continue;
		}

		sort( num + 1, num + 1 + n );
		int now = 0, MAX = -1, current = 0;

		for ( int i = n; i > 1; --i )
		{
			now ^= num[ i ], sum ^= num[ i ];
			current += num[ i ];
			if ( now == sum )
				MAX = max( MAX, current );
		}
		printf( "Case #%d: %d\n", t + 1, MAX );


		/*memset( dp, -1, sizeof( dp ) );


		int MAX = DP( n, n - 1, 0, sum );
		
		if ( MAX < 0 )
			printf( "Case #%d: NO\n", t + 1 );
		else
			printf( "Case #%d: %d\n", t + 1, MAX );
			*/
	}
	return 0;
}

