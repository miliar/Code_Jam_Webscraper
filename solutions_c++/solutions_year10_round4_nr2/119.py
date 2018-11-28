#include <iostream>
using namespace std;
long long a[12][600][12], tmp;
int pr[12][600];
int e[12];
int cn, ci, i, j, k;
int b[1200];
int n;

int maxx( int x, int y )
{
    if ( x > y ) return x;
    return y;
}

int main()
{
    freopen( "B-large.in", "r", stdin );
    freopen( "B-large.out", "w", stdout );
    scanf( "%d", &cn );
    e[0] = 1;
    for ( i = 1; i <= 10; i++ ) e[i] = e[i-1]*2;
    for ( ci = 1; ci <= cn; ci++ )
    {
        scanf( "%d", &n );
        for ( i = 0; i < e[n]; i++ ) scanf( "%d", &b[i]);
        for ( i = n-1; i >= 0; i-- )
        for ( j = 0; j < e[i]; j++ )
        {
            scanf( "%d", &pr[i][j] );
            for ( k = 0; k <= n; k++ ) a[i][j][k] = 2000000000;
        }
        for ( i = 0; i < e[n-1]; i++ )
        {
            j = maxx( n-b[i*2], n-b[i*2+1] );
            for ( k = j; k <= n; k++ ) a[n-1][i][k] = 0;
            a[n-1][i][j-1] = pr[n-1][i];
            //cout << i << ' ' << pr[n-1][i] << endl;
        }
        for ( i = n-2; i >=0; i-- )
        for ( j = 0; j < e[i]; j++ )
        for ( k = 0; k <= n; k++ )
        {
            a[i][j][k] = a[i+1][j*2][k]+a[i+1][j*2+1][k];
            if ( k < n )
            {
                tmp = pr[i][j] + a[i+1][j*2][k+1] + a[i+1][j*2+1][k+1];
                if ( tmp < a[i][j][k] ) a[i][j][k] = tmp;
            }
            if ( k > 0 )
            {
                tmp = a[i][j][k-1];
                if ( tmp < a[i][j][k] ) a[i][j][k] = tmp;
            }

        }
        printf( "Case #%d: %lld\n", ci, a[0][0][0] );
    }
    return 0;
}
