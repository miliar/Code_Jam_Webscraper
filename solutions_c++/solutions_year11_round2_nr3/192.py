#include<stdio.h>
#include<vector>
using namespace std;
vector<int> rm[12],v;
bool vis[12];
int cnt[12],ans[12],n,maxval,max1,tot,col[12],arr1[12];
bool edge[12][12];
void f(int x)
{
    int c1,c2,i,j,sz;
    if (x==n+1)
    {
        c1=0;
        for (i=1;i<=maxval;i++)
        {
            if (cnt[i]) c1++;
        }
        if (c1<=max1) return ;
        for (i=0;i<tot;i++)
        {
            sz=rm[i].size();
            c2=0;
            for (j=1;j<=maxval;j++) vis[j]=0;
            for (j=0;j<sz;j++)
            {
                if (!vis[col[rm[i][j]]])
                {
                    vis[col[rm[i][j]]]=1;
                    c2++;
                }
            }
            if (c2!=c1) break;
        }
        if (i==tot&&c1>max1)
        {
            max1=c1;
            for (i=1;i<=n;i++) ans[i]=col[i];
        }
        return ;
    }
    for (i=1;i<=maxval;i++)
    {
        col[x]=i;
        cnt[i]++;
        f(x+1);
        cnt[i]--;
    }
}
void btrack(int x)
{
    int i,sz,j;
    bool d;
    if (x==n+1)
    {
        sz=v.size();
        if (sz>=3)
        {
            for (i=0;i<sz;i++)
            {
                if (!edge[v[i]][v[(i+1)%sz]]) break;
            }
            if (i==sz)
            {
                for (i=0;i<sz;i++)
                {
                    d=0;
                    for (j=(i+2)%sz;j!=(i-1+sz)%sz;j=(j+1)%sz)
                    {
                        if (edge[v[i]][v[j]])
                        {
                            d=1;
                            break;
                        }
                    }
                    if (d) break;
                }
                if (i==sz)
                {
                    rm[tot++]=v;
                }
            }
        }
        return ;
    }
    btrack(x+1);
    v.push_back(x);
    btrack(x+1);
    v.pop_back();
}
int main()
{
    freopen("C-small-attempt0 (1).in","r",stdin);
    freopen("C-small-attempt0 (1).txt","w",stdout);
    int test,cas,m,i,x,j;
    scanf("%d",&test);
    for (cas=1;cas<=test;cas++)
    {
        scanf("%d%d",&n,&m);
        for (i=1;i<=n;i++)
        {
            for (j=1;j<=n;j++) edge[i][j]=0;
        }
        for (i=0;i<m;i++) scanf("%d",&arr1[i]);
        for (i=0;i<m;i++)
        {
            scanf("%d",&x);
            edge[arr1[i]][x]=edge[x][arr1[i]]=1;
        }
        for (i=1;i<=n;i++)
        {
            if (i==1) edge[1][2]=edge[1][n]=1;
            else if (i==n) edge[n][1]=edge[n][n-1]=1;
            else edge[i][i+1]=edge[i][i-1]=1;
        }
        tot=0;
        btrack(1);
        maxval=(n+2)/2;
        max1=0;
        for (i=1;i<=maxval;i++) cnt[i]=0;
        f(1);
        printf("Case #%d: %d\n",cas,max1);
        for (i=1;i<n;i++) printf("%d ",ans[i]);
        printf("%d\n",ans[i]);
        for (i=0;i<tot;i++) rm[i].clear();
    }
    return 0;
}
