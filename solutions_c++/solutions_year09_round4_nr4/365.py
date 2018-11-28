#include<iostream>
#include<cmath>
using namespace std;
const int maxn=10;
const double maxnum=1e30;
int n;
double x[maxn],y[maxn],r[maxn],ans;
void init()
{
    cin >>n;
    for (int i=0;i<n;i++)
        cin >>x[i]>>y[i]>>r[i];
}
double sqr(double x)
{
    return x*x;
}
double dis(int i,int j)
{
    return sqrt(sqr(x[i]-x[j])+sqr(y[i]-y[j]));
}
void solve()
{
    if (n>3)
    {
        ans=0;
        return;
    }
    if (n<3)
    {
        ans=r[0];
        if (n==2 && r[1]>ans)
            ans=r[1];
        return;
    }
    ans=maxnum;
    for (int i=0;i<n;i++)
        for (int j=i+1;j<n;j++)
        {
            double x=(r[i]+r[j]+dis(i,j))/2;
            if (r[3-i-j]>x)
                x=r[3-i-j];
            if (x<ans)
                ans=x;
        }
}
int main()
{
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    int t;
    cin >>t;
    for (int i=1;i<=t;i++)
    {
        init();
        solve();
        printf("Case #%d: %.6lf\n",i,ans);
    }
    return 0;
}
