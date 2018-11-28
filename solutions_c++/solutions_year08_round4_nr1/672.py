#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;

const int N=10001;
const int inf=20000;
int g[N],c[N],v[N],n,m,in,out,f[N][2],V;

int Min(int x,int y)
{
    if (x<y) return x;
    return y;
}

void dfs(int k)
{
     int i,j,l,r,s,t;
     if (k*2>n)
     {
        f[k][v[k]]=0;
        return ;
     }   
     l=2*k;r=l+1;
     dfs(l);dfs(r);
     s=f[l][0]+f[r][0];
     t=Min(f[l][0],f[r][0]);
     if (c[k]==0)
     {
        if (g[k]==0) f[k][0]=s;
        else f[k][0]=t;
     }
     else
     {
         if (g[k]==0) f[k][0]=Min(s,t+1);
         else f[k][0]=Min(t,s+1);
     }
     
     s=Min(f[l][1],f[r][1]);
     t=f[l][1]+f[r][1];
     if (c[k]==0)
     {
        if (g[k]==0) f[k][1]=s;
        else f[k][1]=t;
     }
     else
     {
         if (g[k]==1) f[k][1]=Min(s+1,t);
         else f[k][1]=Min(s,t+1);
     }
}
int main()
{
    int test,ncase=1,i,j,k;
    freopen("Alarge.in","r",stdin);
    freopen("Alarge.out","w",stdout);
    scanf("%d",&test);
    while (ncase<=test)
    {
       scanf("%d%d",&n,&m);
       in=(n-1)/2;
       for (i=1;i<=in;i++) scanf("%d%d",g+i,c+i);
       for (i=in+1;i<=n;i++) scanf("%d",v+i);
       for (i=0;i<=n;i++)
        for (j=0;j<2;j++) f[i][j]=inf;
       dfs(1);
       k=f[1][m];
       printf("Case #%d: ",ncase++);
       if (k<n) printf("%d\n",k);
       else printf("IMPOSSIBLE\n");
    }
    return 0;
}
