#include<iostream>
#include<algorithm>
using namespace std;
const int maxn=100;
int n,ans,p[maxn],d[maxn],p0[maxn];
void init()
{
    cin >>n;
    memset(p,0,sizeof(p));
    char ch;
    for (int i=0;i<n;i++)
        for (int j=0;j<n;j++)
        {
            cin >>ch;
            if (ch=='1')
                p[i]=j;
        }
}
bool can(int m)
{
    int tot=0;
    for (int i=0;i<m;i++)
        d[tot++]=p[i];
    sort(d,d+tot);
    for (int i=m;i<n;i++)
        d[tot++]=p[i];
    for (int i=0;i<n;i++)
        if (d[i]>i)
            return false;
    return true;
}
void solve()
{
    ans=0;
    int tmp;
    for (int i=n-1;i>=0;i--)
        for (int j=i;j>=0;j--)
        {
            for (int k=0;k<n;k++)
                p0[k]=p[k];
            for (int k=j;k<i;k++)
            {
                tmp=p[k];
                p[k]=p[k+1];
                p[k+1]=tmp;
            }
            if (can(i))
                break;
            ans++;
            for (int k=0;k<n;k++)
                p[k]=p0[k];
        }
}
int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
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
