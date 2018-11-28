#include<stdio.h>
#include<string.h>
#define inf 1000000000
char s[1010][110],t[110];
int dp[1010][110];
int main()
{
    int i,j,n,m,nn,sit,min,ii;
    scanf("%d",&nn);
    for (ii=1;ii<=nn;ii++) {
        scanf("%d%*c",&n);
        memset(dp,0,sizeof(dp));
        for (i=1;i<=n;i++) gets(s[i]);
        scanf("%d%*c",&m);
        for (i=1;i<=m;i++) {
            gets(t);
            for (j=1;j<=n;j++) if (strcmp(t,s[j])==0) break;
            sit=j;
            if (dp[i-1][sit]==inf) {for (j=1;j<=n;j++) dp[i][j]=dp[i-1][j];continue;}
            for (j=1;j<=n;j++) if (j!=sit) dp[i][j]=(dp[i-1][j]<(dp[i-1][sit]+1)?dp[i-1][j]:(dp[i-1][sit]+1));
            dp[i][sit]=inf;
        }
        min=inf;
        for (i=1;i<=n;i++) if (dp[m][i]<min) min=dp[m][i];
        printf("Case #%d: %d\n",ii,min);
    }
    
}
