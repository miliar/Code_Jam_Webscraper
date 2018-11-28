#include <cstdio>
using namespace std;

void dfs(int);
int num[105],ty[105][20],ch[105][20],cur[20],ans[20],ansnum,tot,n,m;

int main(){
    scanf("%d",&tot);
    for (int cases=0;cases<tot;++cases){
        scanf("%d%d",&n,&m);
        for (int i=0;i<m;++i){
            scanf("%d",&num[i]);
            for (int j=0;j<num[i];++j) scanf("%d%d",&ty[i][j],&ch[i][j]);
        }
        ansnum=-1;
        dfs(1);
        printf("Case #%d:",cases+1);
        if (ansnum==-1) printf(" IMPOSSIBLE\n");
        else{
            for (int i=1;i<=n;++i) printf(" %d",ans[i]);
            printf("\n");
        }
    }
    return 0;
}

void dfs(int dep){
    if (dep>n){
        int curnum=0;
        for (int i=1;i<=n;++i) if (cur[i]==1) ++curnum;
        bool t=true;
        for (int i=0;i<m;++i){
            bool curt=false;
            for (int j=0;j<num[i];++j) if (cur[ty[i][j]]==ch[i][j]){
                curt=true;
                break;
            }
            if (!curt){
                t=false;
                break;
            }
        }
        if (!t) return;
        if ((ansnum==-1)||(curnum<ansnum)){
            ansnum=curnum;
            for (int i=1;i<=n;++i) ans[i]=cur[i];
        }
        return;
    }
    cur[dep]=0;
    dfs(dep+1);
    cur[dep]=1;
    dfs(dep+1);
}
