#include<cstdio>

int skip[1100];
int r;
int n;
long long dp[20][1100][20];
long long cost[20][1100];

int main()
{
    int i, j, a, p1, p2, r1;
    int teste, t;
    scanf("%d", &teste);
    for (t=0; t<teste; t++)
    {
        scanf("%d", &r);
        n = 1 << r;
        for (i=0; i<n; i++)
        {
            scanf("%d", &skip[i]);
        }
        for (i=0; i<r; i++)
        {
            int aux = 1 << (r - 1 - i);
            for (j=0; j<aux; j++)
            {
                scanf("%I64d", &cost[i][j]);
            }
        }
        for (r1=0; r1<=r; r1++)
        {
            for (i=0; i<n; i++)
            {
                for (j=0; j<=r; j++)
                {
                    dp[r1][i][j] = -1;
                }
            }
        }
        for (i=0; i<n; i++)
        {
            for (j=0; j<=skip[i]; j++)
            {
                dp[0][i][j] = 0;
            }
        }
        int r1;
        for (r1=0; r1<r; r1++)
        {
            n = n>>1;
            for (a=0; a<n; a++)
            {
                p1 = 2 * a;
                p2 = p1 + 1;
                for (i=0; i<=r; i++)
                {
                    if (dp[r1][p1][i] == -1)
                        break;
                    for (j=0; j<=r; j++)
                    {
                        if (dp[r1][p2][j] == -1)
                            break;
                        long long pcost = dp[r1][p1][i] + dp[r1][p2][j];
                        int minskip = i;
                        if (minskip > j) minskip = j;
                        if (minskip > 0)
                        {
                            if (dp[r1+1][a][minskip-1] == -1)
                            {
                                dp[r1+1][a][minskip-1] = pcost;
                            }
                            else if (dp[r1+1][a][minskip-1] > pcost)
                            {
                                dp[r1+1][a][minskip-1] = pcost;
                            }
                        }
                        pcost += cost[r1][a];
                        if (dp[r1+1][a][minskip] == -1)
                        {
                            dp[r1+1][a][minskip] = pcost;
                        }
                        else if (dp[r1+1][a][minskip] > pcost)
                        {
                            dp[r1+1][a][minskip] = pcost;
                        }
                    }
                }
            }
        }
        long long resp = dp[r][0][0];
        for (i=0; i<=r; i++)
        {
            if (resp > dp[r][0][i] && dp[r][0][i] >= 0)
            {
                resp = dp[r][0][i];
            }
        }
        printf("Case #%d: %I64d\n", t+1, resp);
    }
    return 0;
}
