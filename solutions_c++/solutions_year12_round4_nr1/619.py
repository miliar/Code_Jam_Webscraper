#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<list>
#include<sstream>
using namespace std;

int n;
long long d[10004],L[10004];
long long D;
bool reach[10004];

long long dp[10004];

int main()
{
    freopen("A.in","rt",stdin);
    freopen("A.out","wt",stdout);

   int tst,cas;
   scanf("%d",&tst);
   for(cas=1;cas<=tst;cas++) {
        scanf("%d",&n);
        for(int i=0;i<n;i++) {
            scanf("%lld%lld",&d[i],&L[i]);
            dp[i]=0;
            reach[i]=false;
        }
        reach[n]=false;

        scanf("%lld",&D);
        d[n]=D;
        dp[n]=0;
        bool pl=false;

        int cur=0;
        dp[0]=d[0];
        for(int i=0;i<n;i++)
        {
            int mx=cur;
            for(int j=i+1;j<=n;j++) {
                if(d[i]+dp[i]>=d[j]&&dp[i]!=0)
                {
                    dp[j]=max(min(L[j],d[j]-d[i]),dp[j]);
                    reach[j]=1;
                    mx=j;
                   // printf("%d %d\n",i,j);
                }
            }
            cur=mx;
        }
        if(reach[n]) printf("Case #%d: YES\n",cas);
        else printf("Case #%d: NO\n",cas);

   }


    return 0;
}
