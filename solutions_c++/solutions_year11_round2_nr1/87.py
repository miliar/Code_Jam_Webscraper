#include <cstdio>
#include <cstring>

using namespace std;

const int MAXN = 1111;

int a[MAXN][MAXN];
int n;
double wp[MAXN], owp[MAXN], oowp[MAXN];
double win[MAXN], game[MAXN];

int main()
{
    freopen("in", "rt", stdin);
    freopen("out", "wt", stdout);

    int ctest = 0;
    scanf("%d", &ctest);
    for (int itest = 1; itest <= ctest; itest++)
    {
        scanf("%d\n", &n);
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                char c;
                scanf("%c", &c);
                a[i][j] = -1 * (c == '0') + 1 * (c == '1');
            }
            scanf("\n");
        }


        memset(win, 0, sizeof(win));
        memset(game, 0, sizeof(game));

        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                win[i] += 0 < a[i][j];
                game[i] += a[i][j] != 0;
            }
            wp[i] = win[i] / game[i];
        }


        for (int i = 1; i <= n; i++)
        {
            owp[i] = 0;
            for (int j = 1; j <= n; j++)
                if (a[i][j])
                {
                    double
                        w = win[j],
                        g = game[j];

                    w -= 0 < a[j][i];
                    g -= a[i][j] != 0;
                    owp[i] += w / g;
                }             
            owp[i] /= game[i];
        }

        for (int i = 1; i <= n; i++)
        {
            oowp[i] = 0;
            for (int j = 1; j <= n; j++)
                if (a[i][j])
                    oowp[i] += owp[j];
            oowp[i] /= game[i];
        }

        printf("Case #%d:\n", itest);
        for (int i = 1; i <= n; i++)
            printf("%.10lf\n", wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25);
    }


    return 0;
}
                   