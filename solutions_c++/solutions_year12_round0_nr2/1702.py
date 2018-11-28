#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int MaxN = 105;

int t, n, s, p;
int v[ MaxN ];
int dp[ MaxN ][ MaxN ];

int f( int x, int s ) {
    if( s < 0 ) return -1000;

    if( x == n ) {
     if( s == 0 ) return 0;
     return -1000;
    }

    int &ret = dp[x][s];
    if( ret != -1 ) return ret;
    ret = 0;
    for( int i = 0; i <= 10; ++i )
        for( int j = 0; j <= 10; ++j )
            for( int k = 0; k <= 10; ++k ){
                int dd = max( max( abs( i-j ), abs( i-k ) ), abs( j-k ) );
                if( dd > 2 ) continue;
                if( i+j+k != v[x] ) continue;
                ret = max( ret, f( x+1, s - ( dd == 2 ) ) + (int)(max( i, max( j, k ) ) >= p ) );
            }

    return ret;
}

int main( void ) {
 scanf( "%d", &t );

 for( int tt = 1; tt <= t; ++tt ){
    scanf( "%d%d%d", &n, &s, &p );
    memset( dp, -1, sizeof dp );
    for( int i = 0; i < n; ++i ) scanf( "%d", &v[i] );

    printf( "Case #%d: %d\n", tt, f( 0, s ) );
 }

 return 0;
}
