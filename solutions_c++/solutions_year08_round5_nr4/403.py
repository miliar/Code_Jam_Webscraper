#include <cstdio>
#include <string>

const int maxn = 101;
const int D = 10007;

int f[maxn][maxn];
bool g[maxn][maxn];
int casen, n, m, r;
bool block[maxn][maxn];

void init()
{
     scanf("%d%d%d", &n, &m, &r);
     memset(block, 0, sizeof(block));
     int x, y;
     for (int i(1); i <= r; ++i)
     {
         scanf("%d%d", &x, &y);
         block[x][y] = true;
     }
}

int sqr(int x)
{
    return x * x;
}

int check(int x, int y)
{
    g[x][y] = true;
    if (block[x][y]) return 0;
    if (x == 1 && y == 1) return 1;
    int newx, newy;
    int ans = 0;
    for (int i(1); i <= 5; ++i)
    {
        newx = x - i;
        for (int j(1); j <= 5; ++j)
        {
            newy = y - j;
            if (sqr(x - newx) + sqr(y - newy) == 5 && newx > 0 && newy > 0) {
               if (!g[newx][newy]) f[newx][newy] = check(newx, newy);
               ans = (ans + f[newx][newy]) % D;
            }
        }
    }
    return ans;
} 

void work()
{
     memset(g, 0, sizeof(g));
     f[n][m] = check(n, m);
     printf("%d\n", f[n][m]);
}
     

int main()
{
    freopen("D.in", "r", stdin);
    freopen("D1.out", "w", stdout);
    scanf("%d", &casen);
    for (int i(1); i <= casen; ++i)
    {
        init();
        printf("Case #%d: ", i);
        work();
    }
    return 0;
}
