# include <stdio.h>
# include <string>
# include <algorithm>
# include <iostream>

using namespace std;

# define inf 200000001

# define max_n 20
# define max_m 110

int n,m,case_cnt,cnt,best;
int len[max_m];
int vis[max_n];
int bestvis[max_n];
int a[max_m][max_n*2][2];

void readin()
{
    scanf("%d",&n);
    scanf("%d",&m);
    for (int i=1;i<=m;i++) {
        scanf("%d",&len[i]);
        for (int j=1;j<=len[i];j++)
            scanf("%d%d",&a[i][j][0],&a[i][j][1]);
    }
}

bool check()
{
    for (int i=1;i<=m;i++) {
        bool can=false;
        for (int j=1;j<=len[i];j++)
            if (vis[a[i][j][0]]==a[i][j][1]) {
                can=true;
                break;
            }
        if (!can) return false;
    }
    return true;
}

void dfs(int depth)
{
    if (depth>n) {
        if (check() && cnt<best) {
            best=cnt;
            memcpy(bestvis,vis,sizeof(vis));
        }
        return;
    }
    vis[depth]=1;
    cnt++;
    dfs(depth+1);
    vis[depth]=0;
    cnt--;
    dfs(depth+1);
}

void process()
{
    best=inf;
    cnt=0;
    dfs(1);
    printf("Case #%d: ",++case_cnt);
    if (best==inf)
        printf("IMPOSSIBLE\n");
    else {
        for (int i=1;i<=n;i++) {
            if (i!=1) printf(" ");
            printf("%d",bestvis[i]);
        }
        printf("\n");
    }
}

int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    
    int casen;
    scanf("%d",&casen);
    while (casen--) {
        readin();
        process();
    }
}
