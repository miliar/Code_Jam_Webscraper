#include <cstdio>
#include <algorithm>
using namespace std;
int d[100000];
int l[100000];
int dp[100000];
int main()
{
    int T,ca=0;
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++) scanf("%d%d",d+i,l+i);
        for(int i=0;i<n;i++) dp[i]=-1;
        dp[0]=0;
        for(int i=1;i<n;i++){
            for(int j=0;j<i;j++){
                if(dp[j]==-1) continue;
                if(d[j]+min(l[j],d[j]-dp[j])>=d[i]) {
                    dp[i]=d[j];
                    break;
                }
            }
        }
        int len;
        scanf("%d",&len);
        int flag=0;
        for(int i=0;i<n;i++){
          //  printf("%d %d\n",i,dp[i]);
            if(dp[i]!=-1&&d[i]+min(l[i],d[i]-dp[i])>=len) {
                flag=1;
                break;
            }
        }
        if(flag) printf("Case #%d: YES\n",++ca);
        else printf("Case #%d: NO\n",++ca);
    }
}


