#include<iostream>
#include<cstdio>
using namespace std;
char base[]="welcome to code jam";
int dp[20][800];
int mod=10000;
void init()
{
     for(int i=0;i<800;i++)dp[0][i]=1;
     for(int i=1;i<20;i++)dp[i][0]=0;
}
char buf[800];
main()
{
      freopen("C-large.in","r",stdin);
      freopen("out.txt","w+",stdout);
      int t;
      scanf("%d",&t);
      getchar();
      for(int k=1;k<=t;k++)
      {
        init();
        gets(buf);
        for(int i=1;i<=strlen(buf);i++)
        {
           char key=buf[i-1];
           for(int j=0;j<strlen(base);j++)
           {
               if(key==base[j])
               {
                 dp[j+1][i]=(dp[j+1][i-1]+dp[j][i-1])%mod;   
               }
               else dp[j+1][i]=dp[j+1][i-1];
           }
        }
        printf("Case #%d: %.4d\n",k,dp[19][strlen(buf)]);
      }
      return 0;
}
        
