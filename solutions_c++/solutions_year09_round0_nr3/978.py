#include <algorithm>
#include <vector>
#include <string>

#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

const int MAXN = 510;
const int MAXM = 22;
const int mod = 10000;

int n;
char A[ MAXN ];

int m;
char B[ MAXM ] = "welcome to code jam";

int dp[ MAXN ][ MAXM ];

int main( void )
{
    int test; scanf( "%d", &test );

    m = strlen( B );
    scanf( "\n" );

    for( int t = 0; t < test; ++t ) {
        fgets( A, MAXN, stdin );
        n = strlen( A );

        for( int i = 0; i < m; ++i )
            dp[n][i] = 0;

        for( int i = 0; i <= n; ++i )
            dp[i][m] = 1;

        for( int j = m-1; j >= 0; --j )
            for( int i = n-1; i >= 0; --i ) {
                dp[i][j] = dp[i+1][j];

                if( A[i] == B[j] ) {
                    dp[i][j] += dp[i+1][j+1];
                    if( dp[i][j] >= mod ) dp[i][j] -= mod;
                }
            }

        printf( "Case #%d: %04d\n", t+1, dp[0][0] );
    }

    return 0;
}

