#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#define MAXN 512
using namespace std;
int dat[MAXN][MAXN], n;
double a[MAXN], b[MAXN], c[MAXN];
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    char x;
    scanf("%d", &t);
    for (int ca = 1; ca <= t; ++ca)
    {
        memset(dat, 0, sizeof(dat));
        scanf("%d", &n);
        for (int i = 1; i <= n; ++i)
        {
            scanf("\n");
            for (int j = 1; j <= n; ++j)
            {
                scanf("%c", &x);
                switch (x)
                {
                    case '.': dat[i][j] = -1; break;
                    case '1': dat[i][j] =  1; break;
                    case '0': dat[i][j] =  0; break;
                }
            }
        }
        memset(a, 0, sizeof(a));
        memset(b, 0, sizeof(b));
        memset(c, 0, sizeof(c));
        for (int i = 1; i <= n; ++i)
        {
            double cnt = 0;
            for (int j = 1; j <= n; ++j)
                if (dat[i][j] >= 0)
                {
                    a[i] = a[i] + dat[i][j];
                    cnt = cnt + 1;
                }
            a[i] = a[i] / cnt;
        }
        for (int i = 1; i <= n; ++i)
        {
            double scnt = 0;
            for (int j = 1; j <= n; ++j) if (dat[i][j] >= 0)
            {
                double cnt = 0, s = 0;
                for (int k = 1; k <= n; ++k) if (k != i)
                    if (dat[j][k] >= 0)
                    {
                        s = s + dat[j][k];
                        cnt = cnt + 1;
                    }
                s = s / cnt;
                b[i] = b[i] + s;
                scnt = scnt + 1;
            }
            b[i] = b[i] / scnt;
        }
        for (int i = 1; i <= n; ++i)
        {
            double cnt = 0;
            for (int j = 1; j <= n; ++j)
                if (dat[i][j] >= 0)
                {
                    cnt = cnt + 1;
                    c[i] = c[i] + b[j];
                }
            c[i] = c[i] / cnt;
        }
        printf("Case #%d:\n", ca);
        for (int i = 1; i <= n; ++i)
            printf("%.12f\n", a[i] * 0.25f + b[i] * 0.5f + c[i] * 0.25f);
    }
    return 0;
}
