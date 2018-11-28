#include<iostream>
using namespace std;
const int maxn=510;
char b[]={"welcome to code jam"};
int cases,tt,dp[maxn][30],ans,n;
char a[maxn];
void init()
{
     n=0;
     while (1)
     {
           a[n]=getchar();
           if (a[n]=='\n') break;
           n++;
     }
}

void work()
{
     int i,j,k;
     memset(dp,0,sizeof(dp));
     dp[0][0]=1;
     ans=0;
     for (i=1;i<=n;i++)
     {
         for (j=1;j<=19;j++)
         if (a[i-1]==b[j-1])
             for (k=0;k<i;k++)
             {
                 dp[i][j]+=dp[k][j-1];
                 if (dp[i][j]>=10000) dp[i][j]-=10000;
             }
         ans+=dp[i][19];
         if (ans>=10000) ans-=10000;
     }
                 
}

void print()
{
     printf("Case #%d: %04d\n",tt+1,ans);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d\n",&cases),tt=0;tt<cases;tt++)
    {
        init();
        work();
        print();
    }
    return 0;
}
