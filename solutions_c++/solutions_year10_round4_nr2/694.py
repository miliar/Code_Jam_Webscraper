# include <iostream>

using namespace std;

const int MaxN = 1 << 10;

int cost[2 * MaxN - 1];
int dp[2 * MaxN - 1][15];

int test;
int p;
int m[MaxN];

int main() {
    freopen( "bla.in", "r", stdin );
    freopen( "bla.out", "w", stdout );
    
    scanf( "%d", &test );
    for ( int testId = 1; testId <= test; testId++ ) {
        scanf( "%d", &p );
        
        int t = 1 << p;
        for ( int i = 0; i < t; i++ )
            scanf( "%d", &m[i] );
            
        memset( cost, 0, sizeof( cost ) );
        int pos = ( MaxN - 1 - 1 ) / 2;
        for ( int i = p - 1; i >= 0; i-- ) {
            for ( int j = 0; j < 1 << i; j++ )
                scanf( "%d", &cost[pos + j] );
            pos = ( pos - 1 ) / 2;
        }
            
        for ( int i = MaxN - 1; i < 2 * MaxN - 1; i++ )
            for ( int j = 0; j < 12; j++ )
                dp[i][j] = 0;
                
        for ( int i = 0; i < t; i++ ) {
            for ( int j = 0; j < 12; j++ )
                dp[MaxN - 1 + i][j] = 1000000000;
                
            for ( int j = m[i]; j >= 0; j-- )
                dp[MaxN - 1 + i][j] = 0;
        }
        
        for ( int i = MaxN - 2; i >= 0; i-- )
            for ( int j = 10; j >= 0; j-- ) {
                dp[i][j] = dp[2 * i + 1][j] + dp[2 * i + 2][j] + cost[i];
                if ( j < 10 ) dp[i][j] = min( dp[i][j], dp[2 * i + 1][j + 1] + dp[2 * i + 2][j + 1] );
                if ( j < 10 ) dp[i][j] = min( dp[i][j], dp[i][j + 1] );
                dp[i][j] = min( dp[i][j], 1000000000 );                
            }
            
        printf( "Case #%d: %d\n", testId, dp[0][0] );
    }
    
    return 0;
}
