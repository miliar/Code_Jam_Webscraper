#include <stdio.h>
#include<string.h>

#define maxn 1001
int g[maxn];
int a[maxn];
long long b[maxn];

long long  r, k, n;

int main () {

    freopen ( "C:\\C-large.in", "r", stdin );
    freopen ( "C:\\C-large.out", "w", stdout );
    int t,i, j;
    int p, q;
    long long sum, ans;
    int  temp;
    scanf ( "%d", &p );
    for (  t = 1; t <= p; t++ )
    {
        memset ( g, 0, sizeof ( g ) );
        scanf ( "%I64d%I64d%I64d", &r, &k, &n );

        for ( j = 0; j < n; j++ )
            scanf ( "%d", &g[j] );


        for ( i = 0; i <  n; i++ )
        {
            sum = g[i];
            for ( j = ( i + 1 ) % n; j != i; j++, j %= n )
            {
                sum += g[j];
                if ( sum > k )
                {
                    sum -= g[j];
                    break;
                }
            }
            a[i] = j;
            b[i] = sum;

        }
        ans = 0;
        temp = 0;
        while ( r-- )
        {
            ans += b[temp];
            temp = a[temp];
        }

        printf ( "Case #%d: %I64d\n", t, ans );
    }
    return 0;
}

