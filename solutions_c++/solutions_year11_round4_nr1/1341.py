#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

double x,r,s,t;
int n;
struct walk
{
    double s,e,w;
}a[1001];

bool cmp(walk a,walk b)
{
    if (a.w == b.w) return a.e-a.s > b.e-b.s;
    return a.w < b.w;
}

int main()
{
    freopen("A-large (3).in","r",stdin);
    freopen("A.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for (int ft = 1;ft <= T;ft++)
    {
        scanf("%lf%lf%lf%lf%d",&x,&s,&r,&t,&n);
        a[0].e = 0.0;
        for (int i = 1;i <= n;i++)
        {
            scanf("%lf%lf%lf",&a[2*i].s,&a[2*i].e,&a[2*i].w);
            a[2*i-1].s = a[2*i-2].e;
            a[2*i-1].e = a[2*i].s;
            a[2*i-1].w = 0.0;
        }
        a[2*n+1].s = a[2*n].e;
        a[2*n+1].e = x;
        a[2*n+1].w = 0;
        double res = 0.0;
        sort(a+1,a+1+2*n+1,cmp);
        //for (int i = 1;i <= 2*n+1;i++)
        //    cout << a[i].s << ' ' << a[i].e << ' ' << a[i].w << endl;
        for (int i = 1;i <= 2*n+1;i++)
        {
            double len = a[i].e-a[i].s;
            if (res < t)
            {
                if ((t-res)*(r+a[i].w) >= len)
                    res += len/(r+a[i].w);
                else
                    res += t-res+(len-(t-res)*(r+a[i].w))/(s+a[i].w);
            }
            else
                res += len/(s+a[i].w);
            //cout << res << ' ' << len << ' ' << r+a[i].w << ' ' << s+a[i].w << endl;
        }
        printf("Case #%d: %.9f\n",ft,res);
    }
}
