#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<string>

using namespace std;

int d[11111],l[11111];
int main()
{
    int t,T,n,i,j,D;
    freopen("A-large.in","r",stdin);
   freopen("output.txt","w",stdout);   
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%d%d",&d[i],&l[i]);
            
        }            
        scanf("%d",&D);
        int dp[11111]={};
        dp[0]=d[0];
        for(i=1;i<n;i++)
        {
            for(j=i-1;j>=0;j--)
                if(dp[j]+d[j]>=d[i])
                    dp[i] = max(dp[i], min(l[i],d[i]-d[j]) );
//            cout<<dp[i]<<endl;
        }
        for(i=0;i<n;i++) if(dp[i]+d[i]>=D) break;
        if(i<n)
        printf("Case #%d: YES\n",t);
        else
        printf("Case #%d: NO\n",t);
    }
//system("pause");
    return 0;
}
