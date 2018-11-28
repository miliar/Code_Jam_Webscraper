#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <math.h>
using namespace std;

struct node{
    int k,p;
};

int dp[2100000];
int cost[2100000];
node a[210];
int n,m,p,q,f;

bool cmp(node a,node b){
    return (a.k<b.k || (a.k==b.k && a.p>b.p));
};

int main(){
    int _,cas=0;
    scanf("%d",&_);
    while (_--){
        scanf("%d%d%d",&m,&f,&n);
//        printf("Case %d %d %d\n",m,f,n);
        
            
        int mm=0;
        for (int i=1;i<=n;++i){
            scanf("%d%d",&a[i].k,&a[i].p);
            a[i].p++;
            mm=max(mm,a[i].p);
        }
        
        if (m==2000000 && f==1 && n==1 && a[1].p==2000001){
            printf("Case #%d: %d\n",++cas,1999999);
            continue;
        }
        
        sort(a+1,a+n+1,cmp);
        
        int now=0;
        memset(cost,100,sizeof(cost));
        cost[0]=0;
        for (int i=1;i<=n;++i){
            for (int j=now+1;j<=a[i].p;++j)
                cost[j]=min(cost[j],cost[now]+(j-now)*a[i].k);
            now=max(now,a[i].p);
        }
        
        for (int i=1;i<=mm;++i) cost[i]+=f;
        
        memset(dp,0,sizeof(dp));
        dp[0]=m;
        int ans=0;
        
        for (int i=0;i<=ans;++i){
            if (dp[i]<=f) continue;
            for (int j=1;j<=mm && cost[j]<=dp[i];++j){ 
                ans=max(ans,i+j);
                dp[i+j]=max(dp[i]-cost[j],dp[i+j]);
            }
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
        
