#include <iostream>

using namespace std;

long long int dp[ 2000 ][ 2 ][ 20 ];
int T[ 2000 ], M[ 2000 ];
int n, P;

long long int DP( int x, int k, int cnt )
{

    if ( x >= n )
    {
        if ( k )
            --cnt;
        if ( cnt < P - M[ x - n ] )
            return 1e9;
        else
            return 0;
    }

    if ( ~dp[ x ][ k ][ cnt ] )
        return dp[ x ][ k ][ cnt ];

    dp[ x ][ k ][ cnt ] = 1e9;

    dp[ x ][ k ][ cnt ] = min( dp[ x ][ k ][ cnt ], DP( 2 * x, 0, cnt ) + DP( 2 * x + 1, 0, cnt ) );
    dp[ x ][ k ][ cnt ] = min( dp[ x ][ k ][ cnt ], DP( 2 * x, 1, cnt + 1 ) + DP( 2 * x + 1, 0, cnt ) );
    dp[ x ][ k ][ cnt ] = min( dp[ x ][ k ][ cnt ], DP( 2 * x, 0, cnt ) + DP( 2 * x + 1, 1, cnt + 1 ) );
    dp[ x ][ k ][ cnt ] = min( dp[ x ][ k ][ cnt ], DP( 2 * x, 1, cnt + 1 ) + DP( 2 * x + 1, 1, cnt + 1 ) );

    if ( k )
        dp[ x ][ k ][ cnt ] += T[ x ];

    //printf( "%d %d : %lld\n", x, k, dp[ x ][ k ][ cnt ] );

    return dp[ x ][ k ][ cnt ];
}

int main()
{
    freopen( "B-large.in", "r", stdin );
    freopen( "b.txt", "w", stdout );

    int c = 0, cas, i, j, x;

    scanf( "%d", &cas );

    while ( cas-- )
    {

        scanf( "%d", &P );

        n = 1 << P;

        for ( i = 0; i < n; ++i )
            scanf( "%d", &M[ i ] );

        for ( i = P - 1; i >= 0; --i )
        {
            x = 1 << i;
            for ( j = 0; j < x; ++j )
                scanf( "%d", &T[ x + j ] );
        }

        memset( dp, -1, sizeof( dp ) );
        printf( "Case #%d: %lld\n", ++c, min( DP( 1, 0, 0 ), DP( 1, 1, 1 ) ) );
    }
    return 0;
}

