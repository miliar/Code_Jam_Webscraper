#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int N=10001;
const int INF=0x1fffffff;

int A[N];
bool chg[N];
int dp[N][2];
int n,v;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int cas,ic;
    scanf("%d",&cas);
    for(ic=1;ic<=cas;ic++){
        scanf("%d%d",&n,&v);
        int i,j,c;
        for(i=1;i<=n/2;i++){
            scanf("%d%d",&A[i],&c);
            if(c==1) chg[i]=1;
            else chg[i]=0;
        }
        for(i=n/2+1;i<=n;i++){
            scanf("%d",&A[i]);
        }
        for(i=0;i<=n;i++){
            for(j=0;j<2;j++) dp[i][j]=INF;
        }
        for(i=n/2+1;i<=n;i++) dp[i][A[i]]=0;
        for(i=n/2;i>0;i--){
            int l=2*i,r=2*i+1;
            for(j=0;j<2;j++){
                if(dp[l][j]!=INF){
                    for(int k=0;k<2;k++){
                        if(dp[r][k]!=INF){
                            if(A[i]==1){
                                int t=j&k;
                                dp[i][t]<?=dp[l][j]+dp[r][k];
                                if(chg[i]==1){
                                    t=j|k;
                                    dp[i][t]<?=1+dp[l][j]+dp[r][k];
                                }
                            }
                            else{
                                int t=j|k;
                                dp[i][t]<?=dp[l][j]+dp[r][k];
                                if(chg[i]==1){
                                    t=j&k;
                                    dp[i][t]<?=1+dp[l][j]+dp[r][k];
                                }
                            }
                        }
                    }
                }
            }
        }                   
        int ans=dp[1][v];
        if(ans==INF) printf("Case #%d: IMPOSSIBLE\n",ic);
        else printf("Case #%d: %d\n",ic,ans);
    }
    return 0;
}
