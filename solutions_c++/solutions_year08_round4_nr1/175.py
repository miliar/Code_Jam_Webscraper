#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
using namespace std;
const long N = 40000,INF=1<<28;
const double eps = 1e-6,pi=acos(-1);

long min(long a,long b)
{return a<b?a:b;}
long max(long a,long b)
{return a>b?a:b;}
void swap(long &a,long &b)
{long tt;tt=a,a=b,b=tt;}
long n,m,v;
long g[N],c[N],w[N][2];
void Init()
{
    scanf("%ld %ld",&m,&v);
    long i;
    n=(m-1)/2;
    for(i=0;i<=m;i++)
        w[i][1]=w[i][2]=INF;
    for(i=1;i<=n;i++)
        scanf("%ld%ld",g+i,c+i);
    for(;i<=m;i++)scanf("%ld",g+i);
}
long dfs(long a,long st)
{
    if(a>n)
    {
        if(g[a]==st)return 0;
        return INF;
    }
    if(w[a][st]!=INF)return w[a][st];
    if(st)
    {
        if(g[a])
        {
            w[a][st]<?=dfs(a*2,1)+dfs(a*2+1,1);
            if(c[a])
            {
                w[a][st]<?=dfs(a*2,1)+dfs(a*2+1,0)+1;
                w[a][st]<?=dfs(a*2,1)+dfs(a*2+1,1)+1;
                w[a][st]<?=dfs(a*2,0)+dfs(a*2+1,1)+1;
            }
        }
        else
        {
            w[a][st]<?=dfs(a*2,1)+dfs(a*2+1,0);
            w[a][st]<?=dfs(a*2,1)+dfs(a*2+1,1);
            w[a][st]<?=dfs(a*2,0)+dfs(a*2+1,1);
            if(c[a])
                w[a][st]<?=dfs(a*2,1)+dfs(a*2+1,1)+1;
        }
    }
    else
    {
        if(g[a])
        {
            w[a][st]<?=dfs(a*2,1)+dfs(a*2+1,0);
            w[a][st]<?=dfs(a*2,0)+dfs(a*2+1,0);
            w[a][st]<?=dfs(a*2,0)+dfs(a*2+1,1);
            if(c[a])
            {
                w[a][st]<?=dfs(a*2,0)+dfs(a*2+1,0)+1;
            }
        }
        else
        {
            w[a][st]<?=dfs(a*2,0)+dfs(a*2+1,0);
            if(c[a])
            {
                w[a][st]<?=dfs(a*2,1)+dfs(a*2+1,0)+1;
                w[a][st]<?=dfs(a*2,0)+dfs(a*2+1,0)+1;
                w[a][st]<?=dfs(a*2,0)+dfs(a*2+1,1)+1;
            }
        }
    }
   // printf("%ld %ld : %ld\n",a,st,w[a][st]);
    return w[a][st];

}
void Solve()
{
    dfs(1,v);
    if(w[1][v]!=INF)printf("%ld\n",w[1][v]);
    else printf("IMPOSSIBLE\n");
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long T,K=1;
    scanf("%ld",&T);
    while(T--)
    {
        printf("Case #%ld: ",K++);
        Init();
        Solve();
    }
    return 0;
}
