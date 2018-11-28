#include<iostream>
#include<algorithm>
using namespace std;
const int maxn=10000+100;
const double zero=1e-8;
int n,m,ans;
double len,t,x[maxn],v[maxn];
void init()
{
    cin >>n>>m>>len>>t;
    for (int i=0;i<n;i++)
        cin >>x[i];
    for (int i=0;i<n;i++)
        cin >>v[i];
}
bool can(int i)
{
    return len-x[i]<t*v[i]+zero;
}
void solve()
{
    ans=0;
    if (!m)
        return;
    int x=0,s=0;
    for (int i=n-1;i>=0;i--)
        if (can(i))
        {
            ans+=x;
            s++;
            if (s==m)
                return;
        }
        else
            x++;
    ans=-1;
}
int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int t;
    cin >>t;
    for (int i=1;i<=t;i++)
    {
        init();
        solve();
        if (ans==-1)
            cout <<"Case #"<<i<<": IMPOSSIBLE"<<endl;
        else
            cout <<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
