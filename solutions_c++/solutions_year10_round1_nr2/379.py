#include <cstdio>
#include <cstring>

int n;
int num[110];
int f[110][300], min[300];

int abs(int x)
{
    return (x < 0)?(-x):(x);
}

int main()
{
    FILE *input = fopen("Bsmall.in", "r");
    FILE *output = fopen("Bsmall.out", "w");
    int t, ca = 0, d, ins, m, i, j, k, ans, r, e;
    fscanf(input, "%d", &t);
    while (t > 0)
    {
        fscanf(input, "%d%d%d%d", &d, &ins, &m, &n);
        for (i = 1; i <= n; i++) fscanf(input, "%d", &num[i]);
        for (j = 0; j <= 255; j++) f[1][j] = abs(j - num[1]);
        for (j = 0; j <= 255; j++) min[j] = f[1][j] - 2 * d;
        for (i = 2; i <= n; i++)
        {
            for (j = 0; j <= 255; j++)
            {
                e = d * i + abs(j - num[i]);
                f[i][j] = e - d;
                if (m!=0)
                {
                    for (k = 0; k <= 255; k++)
                    {
                        if (k == j) r = 0; else r = (abs(k - j) - 1)/m*ins;
                        if (min[k] + r + e < f[i][j]) f[i][j] = min[k] + r + e;
                    }
                }
                else
                {
                    e = abs(j - num[i]);
                    for (k = 1; k < i; k++) if (f[k][j] + d * (i - k - 1) + e < f[i][j]) f[i][j] = f[k][j] + d * (i - k - 1) + e;
                }
            }
            for (j = 0; j <= 255; j++)
            {
                if (f[i][j] - d * (i + 1) < min[j]) min[j] = f[i][j] - d * (i + 1);
            }
        }
        ans = d * n;
        for (i = 0; i <= 255; i++) if (f[n][i] < ans) ans = f[n][i];
        fprintf(output, "Case #%d: %d\n", ++ca, ans);
        t--;
    }
    return 0;
}
