# include <stdio.h>
# include <string>
# include <algorithm>
# include <iostream>

using namespace std;

# define max_n 10
# define inf 200000001

int order[max_n];
bool vis[max_n];
int a[max_n],b[max_n];
int n,ans,case_cnt;

void readin()
{
    scanf("%d",&n);
    for (int i=1;i<=n;i++)
        scanf("%d",&a[i]);
    for (int i=1;i<=n;i++)
        scanf("%d",&b[i]);
}

void dfs(int depth)
{
    if (depth>n) {
        int tot=0;
        for (int i=1;i<=n;i++)
            tot+=a[order[i]]*b[i];
        ans=min(ans,tot);
    }
    for (int i=1;i<=n;i++)
        if (!vis[i]) {
            vis[i]=true;
            order[depth]=i;
            dfs(depth+1);
            vis[i]=false;
        }
}

void process()
{
    ans=inf;
    memset(vis,false,sizeof(vis));
    dfs(1);
    printf("Case #%d: %d\n",++case_cnt,ans);
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
