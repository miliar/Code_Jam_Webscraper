#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
const int maxn=10000+10;
int f[maxn],d[maxn],l[maxn],aim,n,T,tt;
bool cheak()
{
    //for (int i=1; i<=n; i++)
    //cout<<f[i]<<"   33333"<<endl;
    for (int i = 1; i<=n; i++)
    if (f[i]>0)
    if (f[i]+d[i]>=aim) return true;
    return false;
}
void init()
{
    cin>>n;
    f[0]=-1;
    for (int i=1; i<=n;i++)
    {
        f[i]=-1;
        cin>>d[i]>>l[i];
    }
    cin>>aim;
}
int main()
{
    freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
    cin>>T;
    for (tt= 1; tt<=T; tt++)
    {
        init();
        if (l[1]>=d[1]) f[1]=d[1];
        for (int i=1;i<=n-1; i++)
        if (f[i]>0)
        for (int j=i+1; j<=n; j++)
        {
            if (d[i]+f[i]<d[j]) break;
            //if (l[j]>=d[j]-d[i])
            f[j]=max(f[j],min(d[j]-d[i],l[j]));
        }
        if (cheak())
        printf("Case #%d: YES\n",tt);
        else
        printf("Case #%d: NO\n",tt);
    }
}
