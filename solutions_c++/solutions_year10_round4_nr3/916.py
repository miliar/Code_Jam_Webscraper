#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int r;
int m[256][256][2];

int main()
{
    int i, j, k;
    int x, y;
    int x1, x2, y1, y2;
    int T, t;
    int ma;
    int mik = 0;
    int cr, pr;

    scanf( "%d", &T );
    for ( t = 1; t <= T; t++ )
    {
        memset( m, 0, sizeof( m ) );
        scanf( "%d", &r );
        cr = 1; pr = 0;
        for ( i = 1; i <= r; i++ )
        {
            scanf( "%d %d %d %d", &x1, &y1, &x2, &y2 );
            for ( x = x1; x <= x2; x++ )
            {
                for ( y = y1; y <= y2; y++ )
                {
                    m[x][y][cr] = 1;
                }
            }
        }

        ma = 0;
        swap( cr, pr );
        while ( 1 )
        {
            mik = 0;
            for ( i = 1; i <= 200; i++ )
            {
                for ( j = 1; j <= 200; j++ )
                {
                    m[i][j][cr] = m[i][j][pr];
                    if ( ( m[i-1][j][pr] == 0 ) && ( m[i][j-1][pr] == 0 ) )
                        m[i][j][cr] = 0;
                    if ( ( m[i-1][j][pr] != 0 ) && ( m[i][j-1][pr] != 0 ) )
                    {
                        m[i][j][cr] = 1;
                    }
                    if ( ( m[i-1][j][cr] != 0 ) || ( m[i][j-1][cr] != 0 ) )
                    {
                        mik++;
                    }
                }
            }
            ma++;
            if ( mik == 0 )
                break;
            swap( cr, pr );
        }

        printf( "Case #%d: %d\n", t, ma );
    }
    return 0;
}
