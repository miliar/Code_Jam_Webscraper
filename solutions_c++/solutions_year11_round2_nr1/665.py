#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int T, N;
int g[101][101]; //1win 0lose
double wp[110], owp[110];
double oowp[110], ans[110];

int main()
{
    freopen("in.in", "r",stdin);
    freopen("out.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas)
    {
        memset(g, -1, sizeof (g));
        memset(wp, 0, sizeof (wp));
        memset(owp, 0, sizeof (owp));
        memset(oowp, 0, sizeof (oowp));
        scanf("%d", &N);
        char str[110];
        for (int i = 1; i <= N; ++i)
        {
            scanf("%s", str + 1);
            int len = strlen(str + 1);
            for (int j = 1; j <= len; ++j)
            {
                if (str[j] == '.');
                else if (str[j] == '1') g[i][j] = 1;
                else g[i][j] = 0;
            }
        }
        for (int i = 1; i <= N; ++i)
        {
            int WIN = 0, LOSE = 0;
            for (int j = 1; j <= N; ++j)
            {
                if (g[i][j] == 1) WIN++;
                else if (g[i][j] == 0) LOSE++;
            }
            if (WIN + LOSE != 0)
                wp[i] = 1.0 * WIN / (WIN + LOSE);
            else wp[i] = 1;
        }
        for (int i = 1; i <= N; ++i)
        {
            int geshu = 0;
            for (int j = 1; j <= N; ++j)
            {
                if (g[j][i] != -1)
                {
                    geshu++;
                    int cnt = 0, win = 0;
                    for (int k = 1; k <= N; ++k)
                    {
                        if (k != i && g[j][k] != -1)
                        {
                            cnt++;
                            if (g[j][k] == 1) win++;
                        }
                    }
                    owp[i] += 1.0 * win / cnt;
                }
            }
            owp[i] /= geshu;
        }
        for (int i = 1; i <= N; ++i)
        {
            int cnt = 0;
            double tmp = 0;
            for (int j = 1; j <= N; ++j)
            {
                if (g[i][j] != -1)
                {
                    ++cnt;
                    tmp += owp[j];
                }
            }
            oowp[i] = tmp / cnt;
        }
        for (int i = 1; i <= N; ++i)
            ans[i] = wp[i] / 4 + owp[i] / 2 + oowp[i] / 4;
        printf("Case #%d:\n", cas);
        for (int i = 1; i <= N; ++i)
            printf("%.8f\n", ans[i]);
    }
    return 0;
}