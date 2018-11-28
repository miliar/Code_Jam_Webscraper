#include<iostream>
using namespace std;
const int maxn=10010;
int maxx=20000;
int n,m,v,test,t,f[maxn][2],g[maxn],c[maxn];
void init()
{
     int i,x;
     scanf("%d%d",&n,&v);
     for (i=1;i<=n;i++)
     {
         f[i][0]=maxx;
         f[i][1]=maxx;
     }
     m=(n-1)/2;
     for (i=1;i<=m;i++) scanf("%d%d",&g[i],&c[i]);
     for (i=m+1;i<=n;i++)
     {
         scanf("%d",&x);
         f[i][x]=0;
     }
}

void work()
{
     int i,j,k;
     for (i=m;i>0;i--)
         for (j=0;j<2;j++)
             for (k=0;k<2;k++)
             {
                if (g[i]==1) f[i][j&k]<?=f[i*2][j]+f[i*2+1][k];
                else f[i][j|k]<?=f[i*2][j]+f[i*2+1][k];
                if (c[i])
                if (g[i]==1) f[i][j|k]<?=f[i*2][j]+f[i*2+1][k]+1;
                else f[i][j&k]<?=f[i*2][j]+f[i*2+1][k]+1;
             }
}

void print()
{
     printf("Case #%d: ",t);
     if (f[1][v]==maxx) printf("IMPOSSIBLE\n");
     else printf("%d\n",f[1][v]);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d",&test),t=1;t<=test;t++)
    {
        init();
        work();
        print();
    }
}
