#include <algorithm>
#include <functional>

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <string>

using namespace std;

char text[ 50 ] = "welcome to code jam"; int t_len;
char S[ 1000 ]; int len;

int mod = 10000;
int dp[ 1000 ][ 50 ];

int solve( int x, int y )
{
    if( y == t_len ) return 1;

    int &ref = dp[x][y];
    if( ref != -1 ) return ref;
    ref = 0;

    for( int i = x; i < len; ++i )
        if( S[i] == text[y] ) {
            ref += solve( i+1, y+1 );
            if( ref >= mod ) ref -= mod;
        }            

    return ref;
}

int main( void )
{
    t_len = strlen( text );
    int T; scanf( "%d ", &T );

    for( int counter = 0; counter < T; ++counter ) {
        gets( S ); len = strlen( S );
        memset( dp, -1, sizeof dp );
        printf( "Case #%d: %04d\n", counter + 1, solve( 0, 0 ) % mod );
    }

    return (0-0);
}
