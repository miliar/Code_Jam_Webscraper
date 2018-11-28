#include <cstdio>

#define MOD 100003
long long comb[600][600];
long long dp[600][600];
long long resps[600];

int main()
{
    int t, teste;
    int n;
    int i, j, k;
    comb[0][0] = 1;
    for (i=1; i<600; i++)
    {
        comb[i][0] = 1;
        comb[i][i] = 1;
    }
    for (i=1; i<600; i++)
    {
        for (j=1; j<i; j++)
        {
            comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD;
        }
    }
    for (i=2; i<600; i++)
    {
        dp[i][1] = 1;
    }
    for (i=3; i<600; i++)
    {
        for (j=2; j<i; j++)
        {
            long long aux = 0;
            for (k=1; k<j; k++)
            {
                int cn = (i - j - 1);
                int ck = (j - k - 1);
                if (ck >= 0 && ck <=cn)
                {
                    aux = (aux + (dp[j][k] * comb[cn][ck]) % MOD) % MOD;
                }
            }
            dp[i][j] = aux;
        }            
    }
    for (i=2; i<600; i++)
    {
        resps[i] = 0;
        for (j=1; j<i; j++)
        {
            resps[i] = (resps[i] + dp[i][j]) % MOD;
        }
    }
    scanf("%d", &teste);
    for (t=0;t<teste;t++)
    {
        long long resp = 0;
        scanf("%d", &n);
        resp = resps[n];
        printf("Case #%d: %I64d\n", t+1, resp);
    }
    return 0;
}
