#include<iostream>
#include<algorithm>
using namespace std;
const int maxn=16;
const int maxm=25;
const int maxnum=1000000;
int n,m,ans,p[maxn][maxm],f[1<<maxn];
bool g[maxn][maxn],mark[1<<maxn];
void init()
{
    cin >>n>>m;
    for (int i=0;i<n;i++)
        for (int j=0;j<m;j++)
            cin >>p[i][j];
}
int getmin(int a,int b)
{
    if (a<b)
        return a;
    return b;
}
int getans(int d,int k,int x)
{
    if (mark[x])
        return maxnum;
    if (k==n)
    {
        if (!x)
            return maxnum;
        return f[d-x];
    }
    int dmin=getans(d,k+1,x);
    if (d&(1<<k))
        dmin=getmin(dmin,getans(d,k+1,x+(1<<k)));
    return dmin;
}
void solve()
{
    memset(g,0,sizeof(g));
    for (int i=0;i<n;i++)
        for (int j=0;j<n;j++)
        {
            for (int k=0;k<m;k++)
                if (p[i][k]==p[j][k])
                    g[j][i]=g[i][j]=true;
            for (int k=0;k<m-1;k++)
                if (p[i][k]<p[j][k] && p[i][k+1]>p[j][k+1])
                    g[i][j]=g[j][i]=true;
        }
    memset(mark,0,sizeof(mark));
    for (int k=0;k<1<<n;k++)
        for (int i=0;i<n;i++)
            if (k&(1<<i))
                for (int j=i+1;j<n;j++)
                    if ((k&(1<<j)) && g[i][j])
                        mark[k]=true;
    f[0]=0;
    for (int i=1;i<1<<n;i++)
        f[i]=getans(i,0,0)+1;
    ans=f[(1<<n)-1];
}
int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int t;
    cin >>t;
    for (int i=1;i<=t;i++)
    {
        init();
        solve();
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
