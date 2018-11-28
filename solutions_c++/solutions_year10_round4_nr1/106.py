#include <iostream>
using namespace std;
int cn, ci, i, j, k;
int p[410], q[410];
int a[410][410];
int fx[410], fy[410];
int ans, tmp, n;

int main()
{
    freopen( "A-large.in", "r", stdin );
    freopen( "A-large.out", "w", stdout );
    scanf( "%d", &cn );
    for ( ci = 1; ci <= cn; ci++ )
    {
        scanf( "%d", &n );
        //cout << n << endl;
        for ( i = 1; i <= n; i++ )
        {
            p[i] = n-i+1;
            q[i] = n+i-1;
        }
        for ( i = n+1; i <=n*2-1; i++ )
        {
            p[i] = p[n*2-i];
            q[i] = q[n*2-i];
        }
        memset( a, 0, sizeof(a) );
        for ( i = 1; i <= n*2-1; i++ )
        for ( j = p[i]; j <= q[i]; j += 2 )
        {
            scanf( "%d", &a[i][j] );
        //    cout << "# " << i << ' ' << j << ' ' << a[i][j] << endl;
        }
        memset( fx, 0, sizeof(fx) );
        memset( fy, 0, sizeof(fy) );
        for ( i = 1; i <= n*2-1; i++ )
        {
            for ( j = 1; j <= n*2-1 && !fx[i] ; j++ )
            for ( k = p[j]; k < i; k += 2 )
            if ( i*2-k <= q[j] && a[k][j] != a[i*2-k][j] ) fx[i] = 1;
            for ( j = 1; j <= n*2-1 && !fy[i] ; j++ )
            for ( k = p[j]; k < i; k += 2 )
            if ( i*2-k <= q[j] && a[j][k] != a[j][i*2-k] ) fy[i] = 1;
        }
        /*
        cout << "! " ;
        for ( i = 1; i <= n*2-1; i++ ) cout << fx[i] << ' ' ;
        cout << endl;
        cout << "! " ;
        for ( i = 1; i <= n*2-1; i++ ) cout << fy[i] << ' ' ;
        cout << endl;
        */
        ans = 100000;
        for ( i = 1; i <= n*2-1; i++ ) if ( !fx[i] )
        for ( j = 1; j <= n*2-1; j++ ) if ( !fy[j] )
        {
            tmp = abs(n-i)+abs(n-j);
            if ( tmp < ans ) ans = tmp;
        }
        ans = (n+ans)*(n+ans)-n*n;
        printf( "Case #%d: %d\n", ci, ans );
    }
    return 0;
}
