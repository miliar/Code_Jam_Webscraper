#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAXN 1100
#define MAXM 30000
#define eps (1e-8)
#define INF 1000000000
#define abs(x) ( (x) > 0? (x): -(x) )
#define sqr(x) ((x) * (x))
#define MAX(a, b) ((a) > (b)? (a): (b))
#define MIN(a, b) ((a) < (b)? (a): (b))

typedef long long LL;

int n;
double ans;
int a[MAXN];
double f[MAXN], g[MAXN];
bool p[MAXN];

void swap( int &x, int &y ) { int temp = x; x = y; y = temp; }

void init()
{
    double c = 0, d = 0, e = 1, v = 1;
    f[0] = f[1] = 0; f[2] = 2;
    g[0] = g[1] = 0; g[2] = 2;
    for ( int i = 3; i < MAXN; ++i )
    {
        f[i] = 0;
        e *= ( i - 1 );
        v = 1;
        for ( int k = 1; k < i; ++k ) v *= k;
        double regv = v;
        g[i] = 0;
        for ( int k = 1; k < i; ++k )
        {
            if ( k == 1 ) c = 1 / e / i; else c = c * ( i - k + 1 );
            f[i] += c * ( f[k] + g[i - k] + v );
            if ( k == 1 ) d = 1; else d = d * ( i - k + 1 );
            g[i] += d * ( f[k] + g[i - k] );
            v /= ( i - k );
        }
        f[i] = f[i] * i / ( i - 1 );
        g[i] += f[i] * regv;
    }
}

int main()
{
    init();
    int T, ca = 0;
    scanf( "%d", &T );
    while ( T-- )
    {
        scanf( "%d", &n );
        for ( int i = 1; i <= n; ++i )
            scanf( "%d", a + i );
        int ans = 0;
        for ( int i = 1; i <= n; ++i ) if ( i != a[i] ) ++ans;
        printf( "Case #%d: %d.000000\n", ++ca, ans );
    }
    return 0;
}
/*
        ans = 0;
        memset( p, 0, sizeof(p) );
        for ( int i = 1; i <= n; ++i ) if ( !p[i] )
        {
            int t = i, cnt = 0;
            do
            {
                p[t] = true;
                ++cnt;
                t = a[t];
            } while ( t != i );
            if ( cnt > 1 ) ans += f[cnt];
        }
        printf( "Case #%d: %.6lf\n", ++ca, ans );
    }
    return 0;
}
*/
