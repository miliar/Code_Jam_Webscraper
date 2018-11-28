#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
const int maxn=30000+100;
const int maxl=100+10;
int n,m,tot,tot2,g[maxn],d[maxn],next[maxn],t,ans;
string name[maxn],a[maxl],s;
void work()
{
    int u=0;
    for (int i=0;i<t;i++)
    {
        int x=g[u];
        while (x>=0 && name[d[x]]!=a[i])
            x=next[x];
        if (x==-1)
        {
            d[tot2]=tot;
            name[tot++]=a[i];
            next[tot2]=g[u];
            g[u]=tot2;
            x=tot2++;
            ans++;
        }
        u=d[x];
    }
}
void init()
{
    cin >>n>>m;
    tot=1;
    tot2=0;
    ans=0;
    for (int i=0;i<n;i++)
    {
        cin >>s;
        t=1;
        int j=1;
        a[0]="";
        while (j<s.size())
        {
            if (s[j]=='/')
            {
                a[t]="";
                t++;
            }
            else
                a[t-1]+=s[j];
            j++;
        }
        work();
    }
}
void solve()
{
    ans=0;
    for (int i=0;i<m;i++)
    {
        cin >>s;
        t=1;
        int j=1;
        a[0]="";
        while (j<s.size())
        {
            if (s[j]=='/')
            {
                a[t]="";
                t++;
            }
            else
                a[t-1]+=s[j];
            j++;
        }
        work();
    }
    for (int i=0;i<tot;i++)
        g[i]=-1;
}
int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int t;
    cin >>t;
    memset(g,-1,sizeof(g));
    for (int i=1;i<=t;i++)
    {
        init();
        solve();
        cout <<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
