#include <iostream>
using namespace std;
int cn, ci, n, m, s, t, A, B, i;
int x[110], v[110];
int ans;

int main()
{
    freopen( "B-large.in", "r", stdin );
    freopen( "B-large.out", "w", stdout );
    scanf( "%d", &cn );
    for ( ci = 1; ci <= cn; ci++ )
    {
        scanf( "%d %d %d %d", &n, &m, &s, &t );
        ans = 0;
        A = 0;
        B = 0;
        for ( i = 0; i < n; i++ ) scanf( "%d", &x[i] );
        for ( i = 0; i < n; i++ ) scanf( "%d", &v[i] );
        for ( i = n-1; i >= 0 && A < m ; i-- )
        {
            if ( v[i]*t >= s-x[i] )
            {
                ans += B;
                A++;
            }
            else B++;
        }
        printf( "Case #%d: ", ci );
        if ( A < m ) printf( "IMPOSSIBLE\n" );
        else printf( "%d\n", ans );
    }
    return 0;
}
