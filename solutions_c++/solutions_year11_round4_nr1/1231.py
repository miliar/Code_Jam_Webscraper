#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

struct way
{
    int a,b,c;
}a[2000];
int cmp(way a, way b)
{
    return a.a<b.a;
}
int cmp2(way a, way b)
{
    return a.c<b.c;
}
double s,x,r,t;
int n;
int i,j;
int main()
{
    freopen("C:\\Users\\¼Ó·ÆÃ¨\\Downloads\\A-large (1).in", "r", stdin);
    freopen("D:OUTPUT.txt", "w", stdout);
    int pp,test;
    scanf("%d",&test);
    double ans;
    for (pp=1; pp<=test; pp++)
    {
        scanf("%lf%lf%lf%lf%d",&s,&x,&r,&t,&n);
        for (i=0;i<n;i++)
        scanf("%d%d%d",&a[i].a,&a[i].b,&a[i].c);
        sort(a,a+n,cmp);
        double ans=0;
        double S=s;
        for (i=0;i<n;i++)
        {
            ans+=(a[i].b-a[i].a)*1.0/(a[i].c+x);
            S-=(a[i].b-a[i].a);
        }
        ans+=S/x;
        if (S/r>=t) ans=ans-1.0*t*r/x+t;
        else
        {
            ans=ans-S/x+S/r;
            t-=S/r;
            sort(a,a+n,cmp2);
            i=0;
            while (t>0)
            {
                if (1.0*(a[i].b-a[i].a)/(a[i].c+r)<=t)
                {
                    ans=ans-1.0*(a[i].b-a[i].a)/(a[i].c+x)+1.0*(a[i].b-a[i].a)/(a[i].c+r);
                    t-=1.0*(a[i].b-a[i].a)/(a[i].c+r);
                }
                else
                {
                    ans=ans-1.0*t*(a[i].c+r)/(a[i].c+x)+t;
                    t=0;
                }
                i++;
                if (i>=n) break;
            }
        }
        printf("Case #%d: %.8lf\n",pp,ans);
    }
}
