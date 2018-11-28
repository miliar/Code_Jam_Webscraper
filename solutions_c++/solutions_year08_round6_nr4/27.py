#include<iostream>
using namespace std;
const int maxn=10;
int g1[maxn][maxn],g2[maxn][maxn],a[maxn],n1,n2,ans,t,tt,u[maxn];
void init()
{
     memset(g1,0,sizeof(g1));
     memset(g2,0,sizeof(g2));
     scanf("%d",&n1);
     int i,x,y;
     for (i=1;i<n1;i++)
     {
         scanf("%d%d",&x,&y);
         x--;
         y--;
         g1[x][y]=1;
         g1[y][x]=1;
     }     
     scanf("%d",&n2);
     for (i=1;i<n2;i++)
     {
         scanf("%d%d",&x,&y);
         x--;
         y--;
         g2[x][y]=1;
         g2[y][x]=1;
     }
     ans=0;
     memset(u,0,sizeof(u));
}

void check()
{
    int i,j;
    for (i=0;i<n2;i++)
        for (j=0;j<n2;j++)
        if (g2[i][j]!=g1[a[i]][a[j]]) return;
    ans=1;    
}

void dfs(int dep)
{
     if (ans) return;
     if (dep==n2)
     {
        check();
        return;
     }
     int i;
     for (i=0;i<n1;i++)
     if (!u[i])
     {
        u[i]=1;
        a[dep]=i;
        dfs(dep+1);
        u[i]=0;
     }
}

void print()
{
     printf("Case #%d: ",t+1);
     if (ans) printf("YES\n");
     else printf("NO\n");
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d",&tt),t=0;t<tt;t++)
    {
        init();
        dfs(0);
        print();
    }
    return 0;
}
