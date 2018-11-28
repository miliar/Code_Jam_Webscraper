#include <cstdio>
#include <iostream>
#include<cstring>
#define city 0
using namespace std;

int dp[200][200];
int t[200];
int p ;
int issurprising(int n )
{
    int t = n /3;
    int ans=0;
    if(n%3==0)
    {
        if(t-1>=p)ans++;
        if(t>=p)ans++;
        if(t+1>=p)ans++;
    }
    if(n%3==1)
    {
        if(t-1>=p)ans++;
    //    if(t>=p)ans++;
        if(t+1>=p)ans+=2;
    }
    if(n%3==2)
    {
    //    if(t-1>=p)ans+=2;
        if(t>=p)ans++;
        if(t+2>=p)ans++;
    }
    return ans==0?0:1;
}


int notsurprising( int n )
{
    int t = n /3;
    int ans=0;
    if(n%3==0)
    {
    //    if(t-1>=p)ans++;
        if(t>=p)ans+=3;
     //   if(t+1>=p)ans++;
    }
    if(n%3==1)
    {
    //    if(t-1>=p)ans++;
        if(t>=p)ans++;
        if(t+1>=p)ans+=2;
    }
    if(n%3==2)
    {
     //   if(t-1>=p)ans+=2;
        if(t>=p)ans+2;
        if(t+1>=p)ans+=2;
    }
    return ans==0?0:1;
}


int main(void)
{

    int cases ;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&cases);
    for(int c=1;c<=cases;++c)
    {
        int n , s  ;
        scanf("%d%d%d",&n,&s,&p);
        for(int i=1;i<=n;++i)
        {
            scanf("%d",&t[i]);
        }
        memset(dp,0,sizeof(dp));
        for(int i=1;i<=n;++i)
        {

            for(int j=0;j<=s&&j<=i;++j)
            {
                int a=notsurprising(t[i]);
                int b=issurprising(t[i]);
       //         printf("%d %d\n",a,b);
                dp[i][j]=dp[i-1][j]+notsurprising(t[i]);
                if(t[i]==30)continue;
                if(t[i]==0)continue;
                if(t[i]==1)continue;
          //      if(t[i]==2)
                if(j!=0)
                    dp[i][j]=max(dp[i][j],dp[i-1][j-1]+issurprising(t[i]));
            }
        }
        printf("Case #%d: %d\n", c,dp[n][s]);

    }
    return 0;
}
