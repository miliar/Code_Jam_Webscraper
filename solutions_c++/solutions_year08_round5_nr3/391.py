#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>
using namespace std;

typedef long long LL;
const int N=11;

char G[N][N];
int sit[N];
int dp[1024][N];
int n,m;
int cnt(int s){
    int re=0;
    for(int i=0;i<n;i++) if(s&(1<<i)) re++;
    return re;
}
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);
    int cas,ic;
    scanf("%d",&cas);
    for(ic=1;ic<=cas;ic++){
        scanf("%d%d",&m,&n);
        int i,j,k;
        for(i=0;i<m;i++) scanf("%s",G[i]);
        for(i=0;i<m;i++){
            sit[i]=0;
            for(j=0;j<n;j++){
                if(G[i][j]=='x') sit[i]|=1<<j;
            }
        }
        memset(dp,0,sizeof(dp));
        for(i=0;i<(1<<n);i++){
            if((i&sit[0])==0&&(i&(i<<1))==0) dp[i][0]=cnt(i);
        }
        for(j=1;j<m;j++){
            for(i=0;i<(1<<n);i++){
                int t=cnt(i);
                if(sit[j]&i){
                    dp[i][j]=0;
                    continue;
                }
                if((i&(i<<1))==0){
                    for(k=0;k<(1<<n);k++){
                        if((k&(k<<1))==0&&(k&(i<<1))==0&&(k&(i>>1))==0){
                            dp[i][j]>?=dp[k][j-1]+t;
                        }
                    }
                }
            }
        }
        //printf("%d %d\n",dp[5][0],dp[5][1]);
        int ans=0;
        for(i=0;i<(1<<n);i++) ans>?=dp[i][m-1];
        printf("Case #%d: %d\n",ic,ans);
    }
    return 0;
}
