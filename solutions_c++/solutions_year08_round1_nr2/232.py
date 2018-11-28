#include<stdio.h>
#include<string.h>

const int maxn=2048;
int a[maxn][maxn];
int d[maxn];
int f[maxn];
bool flag[maxn];
int bfs[maxn];
int ans[maxn];
int len;
int n,m;

void input()
{
    int i,j,t1,t2,tn;
    scanf("%d%d",&n,&m);
    memset(a,0,sizeof(a));
    memset(d,0,sizeof(d));
    memset(f,0,sizeof(f));
    for(i=1;i<=m;i++){
        scanf("%d",&tn);
        for(j=0;j<tn;j++){
            scanf("%d%d",&t1,&t2);
            if(t2==1) f[i]=t1;
            else a[i][t1]=1, d[i]++;
        }
    }
}

bool dfs(int x)
{
    int i;
    if(f[x]<=0) return false;
    if(ans[f[x]]==1) return true;
    ans[f[x]]=1;
    for(i=1;i<=m;i++){
        if(a[i][f[x]]==1){
            d[i]--;
            if(d[i]==0) bfs[len++]=i;
        }
    }
    return true;
}

void solve()
{
    int i,cur;
    memset(flag,0,sizeof(flag));
    memset(ans,0,sizeof(ans));
    for(len=0,i=1;i<=m;i++) if(d[i]==0) bfs[len++]=i;
    for(cur=0;cur<len;cur++){
        if(!dfs(bfs[cur])){
            printf("IMPOSSIBLE\n");
            return;
        }
    }
    for(i=1;i<n;i++) printf("%d ",ans[i]);
    printf("%d\n",ans[i]);
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b.out","w",stdout);
    int i,cas;
    scanf("%d",&cas);
    for(i=1;i<=cas;i++){
        input();
        printf("Case #%d: ",i);
        solve();
    }    
    return 0;
}
