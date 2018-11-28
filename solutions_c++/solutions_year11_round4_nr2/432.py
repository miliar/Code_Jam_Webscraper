#include <cstdio>
#include <vector>

#define MAXR 500
#define MAXC 500

#define ITERATE(it, x) for(__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; ++testcase)
    {
        int R, C, D;
        scanf("%d%d%d", &R, &C, &D);
        int weights[MAXR][MAXC];
        for (int i = 0; i < R; ++i)
        {
            char line[MAXC + 1];
            scanf("%s", line);
            for (int j = 0; j < C; ++j)
                weights[i][j] = line[j] - '0';
        }
        int ans = -1;
        for (int s = min(R, C); s >= 3; --s)
        {
            for (int u = 0; u <= R - s; ++u)
            {
                for (int v = 0; v <= C - s; ++v)
                {
                    int sum = 0;
                    int px = 0;
                    int py = 0;
                    for (int i = 0; i < s; ++i)
                    {
                        for (int j = 0; j < s; ++j)
                        {
                            if ((i == 0 || i == s - 1) && (j == 0 || j == s - 1))
                                continue;
                            sum += weights[u + i][v + j];
                            px += weights[u + i][v + j] * i;
                            py += weights[u + i][v + j] * j;
                        }
                    }
                    if (px * 2 == sum * (s - 1) && py * 2 == sum * (s - 1))
                    {
                        ans = s;
                        goto found;
                    }
                }
            }
        }
    found:
        printf("Case #%d: ", testcase);
        if (ans == -1)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", ans);
    }
    return 0;
}
