#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

const int N=101;
int A[N][N];
int n,m;

int calc(int s){
    int re,i;
    re=0;
    for(i=0;i<n;i++){
        if(s&(1<<i)) re++;
    }
    return re;
}
bool ok(int s){
    int i,j;
    for(i=0;i<m;i++){
        for(j=0;j<n;j++){
            if(A[i][j]==0) continue;
            if(A[i][j]==1&&(s&(1<<j))==0||(A[i][j]==2&&(s&(1<<j))!=0)) break;
        }
        if(j>=n) return 0;
    }
    return 1;
}
int main(){
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small.out","w",stdout);
    int cas,ic;
    scanf("%d",&cas);
    for(ic=1;ic<=cas;ic++){
        scanf("%d%d",&n,&m);
        int i,j,k,ans,ansi;
        ans=n+2;
        memset(A,0,sizeof(A));
        for(i=0;i<m;i++){
            int t;
            scanf("%d",&t);
            for(j=0;j<t;j++){
                int jj,tt;
                scanf("%d%d",&jj,&tt);
                A[i][jj-1]=tt+1;
            }
        }
        for(i=0;i<(1<<n);i++){
            if(ok(i)){
                int t=calc(i);
                if(ans>t){
                   ansi=i;
                   ans=t;
                }
            }
        }
        printf("Case #%d:",ic);
        if(ans==n+2) printf(" IMPOSSIBLE\n");
        else{
            for(i=0;i<n;i++){
                if(ansi&(1<<i)) printf(" 1");
                else printf(" 0");
            }
            printf("\n");
        }
    }
    return 0;
}
