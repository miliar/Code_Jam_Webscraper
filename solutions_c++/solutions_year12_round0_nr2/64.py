#include <cstdio>
#include <cstring>

#define MAXN 110
#define INF  1000000

int n, p, s;
int t[MAXN];
int f[MAXN][MAXN];

int mark(int x, bool surprise)
{
    if (surprise)
    {
        int mx = -1;
        for(int i=x/3; i<=10; ++i)
            for(int j=0; j<3; ++j)
                if (i + i - j + i - 2 == x && i>mx && i >= 2) mx = i;
        if (mx >= 0) return mx >= p ? 1 : 0;
    }
    else
    {
        int mx = -1;
        for(int i=x/3; i<=10; ++i)
            for(int j=0; j<2; ++j) if (i-j>=0)
                for(int z=0; z<2; ++z) if (i-z>=0)
                    if (i+i+i-j-z == x && i>mx) mx = i;
        if (mx >= 0) return mx >= p ? 1 : 0;
    }
    return -INF;
}

int main()
{
    int tc;
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt)
    {
        scanf("%i %i %i", &n, &s, &p);
        for(int i=1; i<=n; ++i) scanf("%i", &t[i]);

        memset(f, 0xff, sizeof(f));
        f[1][0] = mark(t[1], false);
        f[1][1] = mark(t[1], true);
        for(int i=2; i<=n; ++i)
        {
            f[i][0] = f[i-1][0] + mark(t[i], false);

            for(int j=1; j<=s; ++j)
            {
                int a = f[i-1][j] + mark(t[i], false);
                int b = f[i-1][j-1] + mark(t[i], true);
                f[i][j] = a > b ? a : b;
            }
        }
        
        printf("Case #%i: %i\n", tt, f[n][s] >= 0 ? f[n][s] : 0);
    
    }
}