#include<algorithm>
#include<cstdio>
#include<cstring>
using namespace std;
int qw[33][3];
int dp[103][103];
int main()
{

freopen("C:\\Users\\pyxf\\Desktop\\B-small-attempt0.in","r",stdin);
freopen("C:\\Users\\pyxf\\Desktop\\out.txt","w",stdout);
    memset(qw,0,sizeof(qw));
    int i;
    for(i=0;i<=10;i++)
    {
        int j;
        for(j=i;j<=10;j++)
        {
            int k;
            for(k=j;k<=10;k++)
            {
                if(j-i<=1&&k-j<=1)
                {
                    qw[i+j+k][0]=k;
                }
                else if(j-i>2||k-j>2)
                continue;
                else
                {
                    qw[i+j+k][1]=k;
                }
            }
        }
    }
    int t;
    scanf("%d",&t);
    int as=1;
#include<algorithm>
#include<cstdio>
#include<cstring>
using namespace std;
int qw[33][3];
int dp[103][103];
int main()
{


   freopen("C:\\Users\\pyxf\\Desktop\\B-small-attempt1.in","r",stdin);
freopen("C:\\Users\\pyxf\\Desktop\\out.txt","w",stdout);
    memset(qw,0,sizeof(qw));
    int i;
    for(i=0;i<=10;i++)
    {
        int j;
        for(j=i;j<=10;j++)
        {
            int k;
            for(k=j;k<=10;k++)
            {
                if(k-i<=1)
                {
                    qw[i+j+k][0]=max(qw[i+j+k][0],k);
                }
                else if(k-i>2)
                continue;
                else
                {

                   qw[i+j+k][1]=max(qw[i+j+k][1],k);
                }
            }
        }
    }

    int t=1000000;
    scanf("%d",&t);
    int as=1;
int n,s,p;
    while(t--)
    {
        memset(dp,0,sizeof(dp));

        scanf("%d %d %d",&n,&s,&p);
        int i;
        for(i=1;i<=n;i++)
        {
            int x;
            scanf("%d",&x);
            int j;
            for(j=0;j<=s;j++)
            {
                if(qw[x][0]>=p)
                {
                    dp[i][j]=max(dp[i][j],dp[i-1][j]+1);
                }
                else
                    dp[i][j]=max(dp[i][j],dp[i-1][j]);

                if(j>=1)
                {
                    if(qw[x][1]>=p)
                    {
                        dp[i][j]=max(dp[i][j],dp[i-1][j-1]+1);
                    }
                    else
                       dp[i][j]=max(dp[i][j],dp[i-1][j-1]);
                }
            }
        }
        printf("Case #%d: %d\n",as++,dp[n][s]);
    }
    return 0;
}

