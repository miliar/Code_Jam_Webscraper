#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#define INF 1000000000
using namespace std;
int N;
int D[10010],L[10010];
int states[10010]={0};
int F;
int dp(int u){
    if(states[u]!=-1)return states[u];
    int i,j;bool can=false;
    for(i=u+1;i<=N;i++){
        if(dp(i)>=u)break;
    }
    for(j=u-1;j>=0;j--){
        if(L[j]>=D[u]-D[j]&&D[u]+min(D[u]-D[j],L[u])>=F){
            can=true;
            break;
        }
        if(i<=N&&L[j]>=D[u]-D[j]&&D[u]+min(D[u]-D[j],L[u])>=D[i]){
            can=true;
            break;
        }
    }
    if(can)return states[u]=j;
    return states[u]=-INF;
}

int main(){
    int i,j,k,t;
    int T;
    scanf("%d",&T);
    for(t=0;t<T;t++){
        scanf("%d",&N);
        memset(states,-1,sizeof states);
        printf("Case #%d: ",t+1);
        for(i=1;i<=N;i++){
            scanf("%d%d",D+i,L+i);
        }scanf("%d",&F);
        D[0]=0;L[0]=D[1]-D[0];

        if(dp(1)==0)printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
