#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

typedef long long LL;

#define MAXN 1000

int     y, x, d;
LL      sum[MAXN][MAXN];
LL      sx[MAXN][MAXN];
LL      sy[MAXN][MAXN];
LL      s[MAXN][MAXN];
char    w[MAXN];


bool try_k(int k)
{
    for(int i=0; i<=x; ++i) sum[y][i] = sx[y][i] = sy[y][i] = 0;
    for(int i=0; i<=y; ++i) sum[i][x] = sx[i][x] = sy[i][x] = 0;

    for(int i=y-1; i>=0; --i)
        for(int j=x-1; j>=0; --j)
        {
            sum[i][j] = s[i][j] + sum[i+1][j] + sum[i][j+1] - sum[i+1][j+1];
            sx[i][j] = s[i][j]*2*j + sx[i+1][j] + sx[i][j+1] - sx[i+1][j+1];
            sy[i][j] = s[i][j]*2*i + sy[i+1][j] + sy[i][j+1] - sy[i+1][j+1];
        }
    //for(int i=y-

    int mx = x - k + 1;
    int my = y - k + 1;
    for(int i=0; i<my; ++i)
        for(int j=0; j<mx; ++j)
        {
            LL sk = sum[i][j] + sum[i + k][j + k] - sum[i][j + k] - sum[i + k][j];
            sk = sk - s[i][j] - s[i+k-1][j] - s[i][j+k-1] - s[i+k-1][j+k-1];

            LL xk = sx[i][j] + sx[i + k][j + k] - sx[i][j + k] - sx[i + k][j];
            xk = xk - 2*(s[i][j]*j + s[i+k-1][j]*j + s[i][j+k-1]*(j+k-1) + s[i+k-1][j+k-1]*(j+k-1));

            LL yk = sy[i][j] + sy[i + k][j + k] - sy[i][j + k] - sy[i + k][j];
            yk = yk - 2*(s[i][j]*i + s[i+k-1][j]*(i+k-1) + s[i][j+k-1]*i + s[i+k-1][j+k-1]*(i+k-1));
            if (xk % sk == 0 && yk % sk == 0)
            {
                xk = xk / sk;
                yk = yk / sk;
                if (xk == j*2 + k - 1 && yk == i*2 + k - 1) return true;
            }
        }
    return false;
}

int main()
{
    int tc;
    freopen("b-large.in", "r", stdin);
    //freopen("B-small-attempt1.in", "r", stdin);
    //freopen("b.in", "r", stdin);
    freopen("b-large.out", "w", stdout);
    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt)
    {
        fprintf(stderr, "%i\n", tt);
        scanf("%i %i %i", &y, &x, &d);
        for(int i=0; i<y; ++i)
        {
            scanf("%s", w);
            for(int j=0; j<x; ++j) s[i][j] = w[j] - '0' + d;
        }
        bool ok = false;
        int k = min(x, y);
        while (k >= 3)
        {
            if (try_k(k))
            {
                printf("Case #%i: %i\n", tt, k);
                ok = true;
                break;
            }
            k--;
        }
        if (!ok) printf("Case #%i: IMPOSSIBLE\n", tt);        
    }
}