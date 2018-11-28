#include<cstdio>
#include<cstring>
#define MAXN 210
const double esp=1e-8;
using namespace std;

int p[MAXN],v[MAXN];
int n,d;
double low,high;
int t;
void input()
{
    high=0;
    scanf("%d%d",&n,&d);
    for(int i=0;i<n;i++)
    {
       scanf("%d%d",p+i,v+i);
    }
}
bool ok(double len)
{
    double last=-1e100;
    for(int i=0;i<n;i++)
    {
        int vn=v[i];
        if(last<p[i]-len)  last=p[i]-len;
            while(vn--)  last+=d;
            if(last-p[i]-d>len) return false;
    }
    return true;
}
void solve()
{
    double mid;
    low=0,high=1e12;
    for(int cnt=0;cnt<=200;cnt++)
    {
        mid=(low+high)/2;        
        if(ok(mid)) high=mid;
        else low=mid;
    }
    printf("%.8lf\n",low);
}
int main()
{
     freopen("B.out","w",stdout);
    int cs;
    scanf("%d",&cs);
    for(t=1;t<=cs;t++)
    {
        printf("Case #%d: ",t);
        input();
        solve();
    }
    return 0;
}
