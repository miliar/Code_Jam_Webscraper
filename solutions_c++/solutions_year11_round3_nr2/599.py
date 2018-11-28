#include<cstdio>
#include<algorithm>
using namespace std;
int d[1000];
double dp[1001][3];
double dist(int now,int least,double dis)
{
    if (now>=least) return dis;
    double de=least-now;
    return dis-de/2+de;
}
int main()
{
    freopen("B-small-attempt8.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        int l,t,n,c;
        scanf("%d%d%d%d",&l,&t,&n,&c);
        for (int i=0;i<c;i++)
            scanf("%d",&d[i]);
        dp[0][0]=dp[0][1]=dp[0][2]=0;
        for (int i=1;i<=n;i++)
            for (int j=0;j<=l;j++)
            {
                dp[i][j]=dp[i-1][j]+d[(i-1)%c]*2;
                if (j)
                    dp[i][j]=min(dp[i][j],dp[i-1][j-1]+dist(dp[i-1][j-1],t,d[(i-1)%c]));
            }
        printf("Case #%d: %.0f\n",cas,dp[n][l]);
    }
}
