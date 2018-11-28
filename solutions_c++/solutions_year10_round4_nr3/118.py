#include <iostream>
using namespace std;
int ci, cn, i, j, k, x1, x2, y1, y2, t, flag, n;
int a[110][110], b[110][110];

int main()
{
    freopen( "C-small-attempt1.in", "r", stdin );
    freopen( "C-small-attempt1.out", "w", stdout );
    scanf( "%d", &cn );
    for ( ci = 1; ci <= cn; ci++ )
    {
        scanf( "%d", &n );
        memset( a, 0, sizeof(a) );
        for ( i = 0; i < n; i++ )
        {
            scanf( "%d %d %d %d", &x1, &y1, &x2, &y2 );
            for ( j = x1; j <= x2; j++ )
            for ( k = y1; k <= y2; k++ ) a[j][k] = 1;
        }
        t = 1;
        while ( 1 )
        {
            memset( b, 0, sizeof(b) );
            flag = 0;
            for ( i = 1; i <= 100; i++ )
            for ( j = 1; j <= 100; j++ )
            {
                if ( a[i-1][j] && a[i][j-1] || ( a[i][j] && ( a[i-1][j] || a[i][j-1] )) )
                {
                    flag = 1;
                    b[i][j] = 1;
                }
                else b[i][j] = 0;
            }
            if ( !flag ) break;
            t++;
            for ( i = 0; i <= 100; i++ )
            for ( j = 0; j <= 100; j++ ) a[i][j] = b[i][j];
        }
        printf( "Case #%d: %d\n", ci, t );
    }
    return 0;
}
