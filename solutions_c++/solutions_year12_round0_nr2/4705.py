#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int T,n,s,p;
int ti[200];
int best1[30],best2[30];
int dp[200][200];

int maxx(int a,int b)
{
    return a > b ? a : b;
}
int calc_best()
{
    for(int i = 0;i < 31;i++)
    {
        for(int a = 0;a <= i;a++)
        {
            for(int b = a;b < a+2;b++)
            {
                int c = i - a - b;
                if(c - a < 2 && c >= a)
                    best1[i] = maxx(best1[i],c);
            }
            for(int b = a;b <= a+2;b++)
            {
                int c = i - a - b;
                if(c >= a && c - a==2)
                    best2[i] = maxx(best2[i],c);
            }
        }
    }
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    calc_best();
    scanf("%d",&T);
    int cas = 0;
    while(++cas <= T)
    {
        memset(dp,0,sizeof dp);
        scanf("%d%d%d",&n,&s,&p);
        for(int i = 0;i < n;i++)
            scanf("%d",ti+i);
        for(int i = 1;i <= n;i++)
            for(int j = 0;j <= s && j <= i;j++)
            {
                dp[i][j] = maxx(dp[i][j],dp[i-1][j]+(best1[ti[i-1]] >= p ? 1 : 0));
                if(j != 0)
                    dp[i][j] = maxx(dp[i][j],dp[i-1][j-1]+(best2[ti[i-1]] >= p ? 1 :0));
            }
        printf("Case #%d: %d\n",cas,dp[n][s]);
    }
    fclose(stdin);
    fclose(stdout);
}
