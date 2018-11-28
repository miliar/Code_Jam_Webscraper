#include <iostream>
using namespace std;
int cn, ci, R, K, n, i, j, r, p, q, m;
int a[1010];
long long b[1010], ans;
long long sum;
int next[1010];

int main()
{
    freopen( "C-small-attempt0.in", "r", stdin );
    freopen( "out.txt", "w", stdout );
    scanf( "%d", &cn );
    for ( ci = 1; ci <= cn; ci++ )
    {
        //cerr << ci << endl;
        scanf( "%d %d %d", &R, &K, &n );
        for ( i = 0; i < n; i++ ) scanf( "%d", &a[i] );
        for ( i = 0; i < n; i++ )
        {
            sum = a[i];
            next[i] = (i+1)%n;
            while ( sum+a[next[i]] <= K )
            {
                sum += a[next[i]];
                next[i] = (next[i]+1)%n;
            }
            b[i] = sum;
        }
        ans = 0;
        i = 0;
        for ( r = 0; r < R; r++ )
        {
            ans = ans+b[i];
            i = next[i];
        }
        printf( "Case #%d: %lld\n", ci, ans );
    }
    return 0;
}
