#include <algorithm>
#include <stdio.h>
#include <math.h>

#define eps 0.000001
#define MAX 511
#define ll long long

using namespace std;

int testCases;
double matM[MAX][MAX], sumM[MAX][MAX], sumX[MAX][MAX], sumY[MAX][MAX];

double calc(int x, int y, int t = 1)
{
    return matM[x][y] * t;
}

double comp(double x, double p)
{
    if (fabs(x - p) <= eps)
        return 1;
    return 0;
}

int main()
{
    freopen("b-small.in", "r", stdin);
    freopen("b-small.out", "w", stdout);

    int test = 0;
    for (scanf("%d", &testCases); testCases; testCases--)
    {
        test++;
        printf("Case #%d: ", test);

        int r, c, d;
        scanf("%d %d %d\n", &r, &c, &d);

        for (int i = 1; i <= r; i++)
        {
            for (int j = 1; j <= c; j++)
            {
                char ch;
                scanf("%c", &ch);

                matM[i][j] = ch - '0' + d;

                sumM[i][j] = sumM[i - 1][j] + sumM[i][j - 1] - sumM[i - 1][j - 1] + matM[i][j];

                sumX[i][j] = sumX[i - 1][j] + sumX[i][j - 1] - sumX[i - 1][j - 1] + i * matM[i][j];
                sumY[i][j] = sumY[i - 1][j] + sumY[i][j - 1] - sumY[i - 1][j - 1] + j * matM[i][j];
            }
            scanf("\n");
        }

        int k, ok = 1, rez = 2;
        for (k = min(r, c); ok && k > 2; k--)
        {
            for (int i = k; ok && i <= r; i++)
                for (int j = k; ok && j <= c; j++)
                {
                    double x = sumX[i][j] + sumX[i - k][j - k] - sumX[i - k][j] - sumX[i][j - k];
                    double y = sumY[i][j] + sumY[i - k][j - k] - sumY[i - k][j] - sumY[i][j - k];
                    double m = sumM[i][j] + sumM[i - k][j - k] - sumM[i - k][j] - sumM[i][j - k];

                    x -= calc(i - k + 1, j - k + 1, i - k + 1);
                    x -= calc(i, j - k + 1, i);
                    x -= calc(i - k + 1, j, i - k + 1);
                    x -= calc(i, j, i);

                    y -= calc(i - k + 1, j - k + 1, j - k + 1);
                    y -= calc(i, j - k + 1, j - k + 1);
                    y -= calc(i - k + 1, j, j);
                    y -= calc(i, j, j);

                    m -= calc(i - k + 1, j - k + 1);
                    m -= calc(i, j - k + 1);
                    m -= calc(i - k + 1, j);
                    m -= calc(i, j);

                    x /= m;
                    y /= m;

                    fprintf(stderr, " -> %.6lf %.6lf %d %d \n", x, y, i, j);

                    if (comp(x, (double) i - k + (double) (k + 1) / 2.0) && comp(y, (double) j - k + (double) (k + 1) / 2.0))
                    {
                        rez = k;
                        ok = 0;
                    }
                }
        }

        if (rez > 2)
            printf("%d\n", rez);
        else printf("IMPOSSIBLE\n");
        fprintf(stderr, "%d\n", testCases);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
