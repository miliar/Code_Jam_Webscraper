#include <cstdio>
const int maxn = 20;
const double delta = 1e-8;

int map[maxn][maxn];
double r, c, d;

int zero(double s)
{
    if (s < -delta)
        return -1;
    return s > delta;
}

bool valid(int a, int b, int dd)
{
    double c = dd / 2.0;
    double sumx = 0.0, sumy = 0.0;

    for (int i = 0; i < dd; i += 1)
        for (int j = 0; j < dd; j += 1)
            if (i == 0 && j == 0 || i == 0 && j == dd - 1 || i == dd - 1 && j == 0 || i == dd - 1 && j == dd - 1)
                continue;
            else {
                sumx += (map[i + a][b + j] + d) * (i + 0.5 - c);
                sumy += (map[i + a][b + j] + d) * (j + 0.5 - c);
            }
    //printf ("%d %d %d: %lf %lf\n", a, b, dd, sumx, sumy);
    return !zero(sumx) && !zero(sumy);
}

double min(double a, double b)
{
    return a > b ? a : b;
}

int main(void)
{
    int T;
    scanf("%d", &T);
    for (int loop = 1; loop <= T; loop++) {
        scanf("%lf%lf%lf", &r, &c, &d);
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                scanf("%1d", &map[i][j]);

        bool flag = false;
        int ans = 0;
        for (int dd = min(r, c); dd >= 3 && !flag; dd--)
            for (int i = 0; i + dd - 1 <= r - 1 && !flag; i++)
                for (int j = 0; j + dd - 1 <= c - 1 && !flag; j++) {
                    //printf("%d\n", dd);
                    if (valid(i, j, dd)) {
                        flag = true;
                        ans = dd;
                    }
                }

        printf("Case #%d: ", loop);
        if (!flag)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", ans);
    }
    return 0;
}
