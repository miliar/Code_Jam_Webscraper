#include<iostream>
#include<string.h>
using namespace std;

int dp[20][505];
char a[505];
char temp[20] = "welcome to code jam";

int main( ){
    int i, j, k, cas, len, p;
    freopen( "C-large.in", "r", stdin );
    freopen( "C-large.out", "w", stdout );
    scanf( "%d", &cas );gets( a );
    for( i = 1; i <= cas; i++ ){
        memset( dp, 0, sizeof( dp ) );
        gets( a );
        len = strlen( a );
        for( j = 0; j < len; j++ )
            if( a[j] == 'w' ) dp[0][j] = 1;
        for( k = 1; k < 19; k++ )
            for( j = len - 1; j >= 0; j-- ){
                if( a[j] != temp[k] ) continue;
                for( p = 0; p < j; p++ ){
                    dp[k][j] = ( dp[k][j] + dp[k-1][p] ) % 10000;
                }
            }
        int ans = 0;
        for( j = 0; j < len; j++ )
            ans = ( ans + dp[18][j] ) % 10000;
        printf( "Case #%d: %04d\n", i, ans );
    }
    return 0;
}
