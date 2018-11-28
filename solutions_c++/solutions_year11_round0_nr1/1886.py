#include <iostream>

using namespace std;

const int   maxSize     =   100 + 10;
const int   move[9][2]  =   {{-1, -1}, {1, 1}, {1, 0}, {-1, 0}, {0, 1}, {0, -1},
                            {1, -1}, {-1, 1}, {0, 0}};

int     f[2][maxSize][maxSize];

struct  node
{
    int x, y;
}   que[maxSize];

int     solve()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i ++)
    {
        char c, a;
        int x;
        scanf("%c%c%d", &a, &c, &x);
        x --;
        if (c == 'O')
            que[i].x = 0;
        else
            que[i].x = 1;
        que[i].y = x;
    }

    memset(f, -1, sizeof(f));
    f[0][0][0] = 0;
    for (int t = 1; ; t ++)
    {
        int now = t % 2;
        int pre = 1 - now;
        for (int i = 0; i < 100; i ++)
            for (int j = 0; j < 100; j ++)
            {
                if (f[now][i][j] == n)
                    return t - 2;
                f[now][i][j] = f[pre][i][j];
                for (int k = 0; k < 9; k ++)
                {
                    int a = i + move[k][0];
                    int b = j + move[k][1];
                    if (a >= 0 && a < 100 && b >= 0 && b < 100 && f[pre][a][b]
                        != -1)
                    {
                        f[now][i][j] = max(f[pre][a][b], f[now][i][j]);
                        int l = f[pre][a][b];
                        if (a == i && que[l].x == 0 && que[l].y == i)
                            f[now][i][j] = max(f[now][i][j], f[pre][a][b] + 1);
                        if (b == j && que[l].x == 1 && que[l].y == j)
                            f[now][i][j] = max(f[now][i][j], f[pre][a][b] + 1);
                    }
                }
            }
    }
}

int     main()
{
    freopen("a.in", "r", stdin);
    freopen("a.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i ++)
        printf("Case #%d: %d\n", i, solve());
}
