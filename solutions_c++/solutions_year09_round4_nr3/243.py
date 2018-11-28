#include <algorithm>
#include <vector>
#include <string>

#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

const int MAX = 110;

int n, m;

int T[ MAX ][ MAX ];
int graf[ MAX ][ MAX ];

int dp[ 1 << 16 ];
bool okay[ 1 << 16 ];

bool sijeku( int a, int b, int p )
{
    if( T[a][p-1] == T[b][p-1] ) return true;
    if( T[a][p] == T[b][p] ) return true;
    if( T[a][p-1] < T[b][p-1] ) swap( a, b );
    if( T[a][p] < T[b][p] ) return true;
    return false;
}

int solve( int mask )
{
    if( mask == (1<<n)-1 ) return 0;

    int &ref = dp[mask];
    if( ref != -1 ) return ref;

    ref = n;

    for( int uzmi = (mask+1) & ~mask; uzmi+mask < (1<<n); uzmi = ( uzmi+mask+1 ) & ~mask )
        if( okay[uzmi] )
            ref = min( ref, 1 + solve( mask | uzmi ) );

    return ref;
}

int main( void )
{
    int test; scanf( "%d", &test );

    for( int t = 0; t < test; ++t ) {
        scanf( "%d %d", &n, &m );

        for( int i = 0; i < n; ++i )
            for( int j = 0; j < m; ++j )
                scanf( "%d", &T[i][j] );

        memset( graf, 0, sizeof graf );

        for( int a = 0; a < n; ++a )
            for( int b = 0; b < n; ++b )
                for( int i = 1; i < m; ++i )
                    if( sijeku( a, b, i ) )
                        graf[a][b] = 1;

        for( int uzmi = 1; uzmi < (1<<n); ++uzmi ) {
            okay[uzmi] = true;

            for( int i = 0; i < n; ++i )
                for( int j = i+1; j < n; ++j )
                    if( (uzmi>>i&1) && (uzmi>>j&1) && graf[i][j] == 1 )
                        okay[uzmi] = false;
        }

        memset( dp, -1, sizeof dp );
        printf( "Case #%d: %d\n", t+1, solve( 0 ) );
    }

    return 0;
}

