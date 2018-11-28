#include <stdio.h>
#include <string.h>
int cnt;
int num[1010];
int use[1010];
void dfs(int x)
{
    cnt++;
    use[x]=1;
    int next=num[x];
    if (!use[next]) dfs(next);
}
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int ii=1;ii<=t;ii++)
    {
        int n;
        scanf("%d",&n);
        for (int i=1;i<=n;i++)
            scanf("%d",&num[i]);
        memset(use,0,sizeof(use));
        double ans=0;
        for (int i=1;i<=n;i++)
        {
            if (use[i]) continue;
            else
            {
                cnt=0;
                dfs(i);
                if (cnt!=1) ans+=cnt;
            }
        }
        printf("Case #%d: %.6f\n",ii,ans);
    }
    return 0;
}
