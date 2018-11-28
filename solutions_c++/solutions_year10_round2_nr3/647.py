#include<iostream>
using namespace std;
#define see(x) cout<<#x<<"  "<<endl
#define sp system("pause")
int dp[501][501];
int C[501][501];
int sum[501];
const int mod=100003;
void init()
{
     int i,j;
     memset(C,0,sizeof(C));
     for(i=0;i<=500;i++)
         C[i][0]=1;
     for(i=1;i<=500;i++)
         for(j=1;j<=i;j++)
         {
             C[i][j]=(C[i-1][j-1]+C[i-1][j])%mod;
         }
     C[0][0]=1;
     
} 
int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    memset(dp,0,sizeof(dp));
    init();
    int i,j,n,cas;
    //while(cin>>i>>j)
    //    cout<<C[i][j]<<endl;
    dp[1][1]=0;//!
    dp[2][1]=1;
    dp[3][1]=1;
    dp[3][2]=1;
    dp[4][1]=1;
    dp[4][2]=1;
    dp[4][3]=1;
    for(i=2;i<=500;i++)
        dp[i][1]=1;
    for(i=1;i<=500;i++)
    {
        for(j=1;j<=i;j++)
        {
            for(n=2*i-j;n<=500;n++)
            {
                if(n<=4)
                    continue;
                dp[n][i]+=C[n-i-1][i-j-1]*dp[i][j];
                dp[n][i]%=mod;
            }
        }
    }
    for(n=0;n<=500;n++)
    {
        for(i=0;i<=500;i++)
        {
            sum[n]+=dp[n][i];
            sum[n]%=mod;
        }
    }
    scanf("%d",&cas);
    for(int T=1;T<=cas;T++)
    {
        scanf("%d",&n);
        printf("Case #%d: %d\n",T,sum[n]);
    }
    //system("pause");
}
