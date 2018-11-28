#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int l, d, n;

char dic[ 5001 ][ 16 ];
char pat[ 5000 ];
char s[ 16 ][ 27 ];
int total = 0;

int main()
{
    //freopen( "a.in", "r", stdin );
    //freopen( "a.out", "w", stdout );

    scanf( "%d %d %d", &l, &d, &n );

    for( int k = 0; k < d; k++ )
        scanf( "%s", dic[ k ] );

    for( int t = 0; t < n; t++ )
    {
        total = 0;
        scanf( "%s", pat );
        int len = strlen( pat );
        memset( s, 0, sizeof( s ) );

        int p = 0;
        for( int j = 0; j < len; )
        {
            if( pat[ j ] == '(' )
            {
                while( pat[ j + 1 ] != ')' )
                {
                    j++;
                    s[ p ][ pat[ j ] - 97 ] = 1;
                }
                p++;
                j += 2;
            }
            else
            {
                s[ p ][ pat[ j ] - 97 ] = 1;
                j++;
                p++;
            }
        }

        for( int k = 0; k < d; k++ )
        {
            int sign = 1;
            for( int j = 0; j < l; j++ )
            {
                if( s[ j ][ dic[ k ][ j ] - 97 ] == 0 )
                {
                    sign = 0;
                    break;
                }
            }

            total += sign;
        }

        printf( "Case #%d: %d\n", t + 1, total );
    }

    return 0;
}




