#include <cstdio>
#include <cstring>

FILE * fp;

int t, i, j, k, len, ans;

int dp[600][20];

char s[600];

char *welcome = "welcome to code jam";

int search(int p, int q)
    {
    if (dp[p][q] != -1)
        return dp[p][q];
    if (q == 19)
        return 1;
    int i, j, ss = 0;
    for (i = p; i < len; i++)
        {
        if (s[i] == welcome[q])
            {
            ss += search(i + 1, q + 1);
            ss %= 10000;
            }
        }
    dp[p][q] = ss;
    return dp[p][q];
    }

int main()
    {
    fp = fopen("c.out", "wt");
    scanf("%d\n", &t);
    for (i = 0; i < t; i++)
        {
        gets(s);
        len = strlen(s);
        for (j = 0; j < 600; j++)
            for (k = 0; k < 20; k++)
                dp[j][k] = -1;
        ans = search(0, 0);
        fprintf(fp, "Case #%d: ", i + 1);
        if (ans < 1000)
            fprintf(fp, "0");
        if (ans < 100)
            fprintf(fp, "0");
        if (ans < 10)
            fprintf(fp, "0");
        fprintf(fp, "%d\n", ans);
        }
    return 0;
    }
