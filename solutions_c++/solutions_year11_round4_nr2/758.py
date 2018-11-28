#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

const int MAX = 1010;

int weight[MAX][MAX];

int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);
    int T;
    scanf("%d", &T);
    int R, C, D;
    int L;
    int cases = 1;
    char in;
    while (T-- > 0)
    {
        scanf("%d %d %d\n", &R, &C, &D);
        memset(weight, 0, sizeof(weight));
        for (int i = 1; i <= R; i++)
        {
            for (int j = 1; j <= C; j++)
            {
                in = getchar();
                weight[i][j] = in - '0' + D;
            }
            getchar();
        }
        L = min(R, C);
        double xx, yy;
        double ww;
        double dx, dy;
        double mx, my;
        int ans;
        int len;
        for (len = L; len >= 1; len--)
        {
            for (int sx = 1; sx <= R - len + 1; sx++)
            {
                for (int sy = 1; sy <= C - len + 1; sy++)
                {
                    xx = yy = 0;
                    ww = 0;
                    for (int i = 0; i < len; i++)
                    {
                        for (int j = 0; j < len; j++)
                        {
                            xx += weight[sx + i][sy + j] * (sx + i);
                            yy += weight[sx + i][sy + j] * (sy + j);
                            ww += weight[sx + i][sy + j];
                        }
                    }
                    xx -= (   weight[sx][sy] * (sx)
                            + weight[sx + len - 1][sy] *(sx + len - 1)
                            + weight[sx][sy + len - 1] * sx
                            + weight[sx + len - 1][sy + len - 1] * (sx + len - 1));
                    yy -= (   weight[sx][sy] * (sy)
                            + weight[sx + len - 1][sy] *(sy)
                            + weight[sx][sy + len - 1] * (sy + len - 1)
                            + weight[sx + len - 1][sy + len - 1] * (sy + len - 1));
                    ww -= (   weight[sx][sy]
                            + weight[sx + len - 1][sy]
                            + weight[sx][sy + len - 1]
                            + weight[sx + len - 1][sy + len - 1]);
                    dx = xx / ww;
                    dy = yy / ww;
                    mx = (sx + sx + len - 1) / 2.0;
                    my = (sy + sy + len - 1) / 2.0;
                    if ((fabs(dx - mx) < 1e-6) && (fabs(dy - my) < 1e-6))
                    {
                        ans = len;
                        goto end;
                    }
                }
            }
        }
        end:
        if (len < 3)
        {
            printf("Case #%d: IMPOSSIBLE\n", cases++);
        }
        else
        {
            printf("Case #%d: %d\n", cases++, ans);
        }
    }
    return 0;
}
