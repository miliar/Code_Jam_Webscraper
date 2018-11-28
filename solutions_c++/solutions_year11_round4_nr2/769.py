// B CZM1.0
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;

#define oo 1000000000
#define PI acos(-1.0)
#define eps 1e-5
const static int maxN = 10 + 1;

char grid[maxN][maxN];

bool Can(int D, int t, int l, int K)
{
    int i, j;
    double x, y;
    double dx, dy;
    dx = dy = 0;
    if (K % 2)
    {
        x = y = K / 2;
    }
    else
    {
        x = y = K / 2 - 0.5;
    }
    for (i = 0; i < K; i++)
    {
        for (j = 0; j < K; j++)
        {
            if (i == 0 && j == 0
                || i == 0 && j == K - 1
                || i == K - 1 && j == 0
                || i == K - 1 && j == K - 1)
            {
            }
            else
            {
                dx += (D + grid[t + i][l + j] - '0') * (i - x);
                dy += (D + grid[t + i][l + j] - '0') * (j - y);
            }
        }
    }
    return dx == 0 && dy == 0;
}

int main()
{
    //freopen("B-small-attempt1.in", "r", stdin);
    //freopen("B-small-attempt1.out", "w", stdout);
    int T;
    int cas = 1;
    int R, C, D;
    int x, y, l, t;
    int K;
    int i;
    bool flag;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d%d%d", &R, &C, &D);
        for (i = 0; i < R; i++)
        {
            scanf("%s", grid[i]);
        }
        flag = false;
        for (K = min(R, C); K >= 3 && !flag; K--)
        {
            for (x = 0; x <= R - K && !flag; x++)
            {
                for (y = 0; y <= C - K && !flag; y++)
                {
                    if (Can(D, x, y, K))
                    {
                        flag = true;
                        break;
                    }
                }
                if (flag) break;
            }
            if (flag) break;
        }
        if (K >= 3)
        {
            printf("Case #%d: %d\n", cas++, K);
        }
        else
        {
            printf("Case #%d: IMPOSSIBLE\n", cas++);
        }
    }
    return 0;
}
