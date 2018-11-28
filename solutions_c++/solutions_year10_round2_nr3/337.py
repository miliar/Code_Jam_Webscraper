#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<map>
#include<iostream>
using namespace std;

int t,n,dp[505][505],nr[505][505];
int mod=100003;

int ncr (int nn,int rr) {
    if (nr[nn][rr]!=-1) return nr[nn][rr];
    if (rr==0) return 1;
    if (nn==0) return 0;
    nr[nn][rr]=ncr(nn-1,rr-1)+ncr(nn-1,rr);
    return nr[nn][rr];
}

int doit (int at,int ord) {
    //printf("-- %d %d = %d\n",at,ord,dp[at][ord]);
    if (ord==1) return 1;
    if (dp[at][ord]!=-1) return dp[at][ord];
    if (at<=ord) return 0;
    int ans=0;
    for (int i=1; i<ord; i++) {
        if (ord-i<=at-ord) {
           ans+=doit(ord,i)*ncr((at-ord-1),(ord-i-1));
           //printf("%d (%d,%d)\n",ans,at-ord-1,ord-i-1);
           ans%=mod;
           }
        }
    dp[at][ord]=ans;
    //printf("%d %d: %d\n",at,ord,ans);
    return ans;
}

int main() {
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d",&t);
    memset(dp,-1,sizeof(dp));
    memset(nr,-1,sizeof(nr));
    for (int i=0; i<t; i++) {
        scanf("%d",&n);
        int ret=0;
        for (int j=1; j<n; j++) {
            ret+=doit(n,j);
            ret%=mod;
            }
        printf("Case #%d: %d\n",i+1,ret);
        }
    
}
