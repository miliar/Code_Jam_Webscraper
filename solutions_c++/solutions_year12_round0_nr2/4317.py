#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int a[110],n,s,p;
int dp[110][110];
int main()
{
    freopen("C:\\Users\\James\\Desktop\\in.txt","r",stdin);freopen("C:\\Users\\James\\Desktop\\out.txt","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d%d",&n,&s,&p);
        for(int i=1;i<=n;i++)
        scanf("%d",&a[i]);
        printf("Case #%d: ",++cas);
        if(p==0)
        {
            printf("%d\n",n);
            continue;
        }
        memset(dp,0,sizeof(dp));
        for(int i=1;i<=n;i++)
        {
            for(int j=0;j<=s;j++)
            {
                if(3*p-2<=a[i])
                dp[i][j]=dp[i-1][j]+1;
                else
                {
                    dp[i][j]=dp[i-1][j];
                    if(j&&p>1&&3*p-4<=a[i])
                    dp[i][j]=max(dp[i][j],dp[i-1][j-1]+1);
                }
            }
        }
        int ans=0;
        for(int i=0;i<=s;i++)ans=max(ans,dp[n][i]);
        printf("%d\n",ans);
    }
}
