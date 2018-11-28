#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

#define MAXN 10010
#define MAXL 3

int dp[ MAXN ][ MAXL ];
int n, h, f, c, d[ 10010 ], dis[ 10010 ];

int DP( int x, int r )
{
	if ( !x )
		return 0;
	if ( dp[ x ][ r ] != -1 )
		return dp[ x ][ r ];


	if ( r )
		return min( DP( x - 1, r ) + dis[ x - 1 ] * 2, DP( x - 1, r - 1 ) + dis[ x - 1 ] );
	else
		return DP( x - 1, r ) + dis[ x - 1 ] * 2;
}
	
	

int main()
{
	freopen( "B.out", "w", stdout );
	int t;
	scanf( "%d", &t );

	for ( int k = 1; k <= t; ++k )
	{
		scanf( "%d %d %d", &f, &h, &n );
		scanf( "%d", &c );
		for ( int i = 0; i < c; ++i )
			scanf("%d", &d[ i ]  );

		int x = 0;
		for ( int i = 0; i < n; ++i, x = ( ++x ) % c )
			dis[ i ] = d[ x ];


		memset( dp, 63, sizeof( dp ) );

		int INF = dp[ 0 ][ 0 ];
		dp[ 0 ][ f ] = 0;	

		for ( int i = 0; i < n; ++i )
		{
			for ( int j = 0; j <= f; ++j )
			{
				if ( dp[ i ][ j ] != INF )
				{
					dp[ i + 1 ][ j ] = min( dp[ i + 1 ][ j ], dp[ i ][ j ] + dis[ i ] * 2 );
					
					if ( j )
					{
						if ( dp[ i ][ j ] >= h )
							dp[ i + 1 ][ j - 1 ] = min( dp[ i ][ j ] + dis[ i ], dp[ i + 1 ][ j - 1 ] );
							
						int r = h - dp[ i ][ j ];

						if ( r > 0 && dis[ i ] * 2 > r )
							dp[ i + 1 ][ j - 1 ] = min( dp[ i ][ j ] + r + dis[ i ] - r / 2, dp[ i + 1 ][ j - 1 ] );
					}
				}
			}
		}
		
		int MIN = 1e9;
		for ( int i = 0; i <= f; ++i )
			MIN = min( MIN, dp[ n ][ i ] );

		
		printf( "Case #%d: %d\n", k, MIN );
	}
	return 0;
}

			
			
		




