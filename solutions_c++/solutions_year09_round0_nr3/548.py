#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_LEN 511

char b[20] = "welcome to code jam";
int count[20];
char s[MAX_LEN];
int n;

int main( )
{
    freopen( "in.in", "r", stdin );
    freopen( "out.txt", "w", stdout );
    scanf( "%d", &n );
    gets( s );
    for( int i = 1; i <= n; ++i )
    {
        memset( count, 0, sizeof( count ) );
        gets( s );
        for( int k = 0; s[k]; ++k )
        {
            for( int j = 0; j < 19; ++j )
                if( s[k] == b[j] )
                {
                    if( j > 0 ) count[j] = ( count[j] + count[j-1] ) % 10000;
                    else ++count[j];
                }
        }
        printf( "Case #%d: %0.4d\n", i, count[18] );
    }
    return 0;
}
