#include<iostream>
using namespace std;
#define maxn 1100
struct Fock
{
       long l,r,w;
}a[maxn];
long cas,tst,n,i,j,x,r,s,t;
double ans,d,tmp;
bool comp(Fock a,Fock b)
{
     return a.w<b.w;
}
int main()
{
    freopen("A.in","r",stdin);
    freopen("out.txt","w",stdout);
    double tm;
    for (scanf("%ld",&cas),tst=1;tst<=cas;tst++)
    {
        scanf("%ld%ld%ld%ld%ld",&x,&s,&r,&t,&n);
        for (i=0;i<n;i++)
        {
            scanf("%ld%ld%ld",&a[i].l,&a[i].r,&a[i].w);
            x-=a[i].r-a[i].l;
        }
        a[n].l=0;
        a[n].r=x;
        a[n].w=0;
        n++;
        sort(a,a+n,comp);
        tm=t;
        ans=0;
        for (i=0;i<n;i++)
        {
            d=a[i].r-a[i].l;
            if (tm>0)
            {
               if (d>=tm*(a[i].w+r))
               {
                  ans+=tm;
                  ans+=(d-tm*(a[i].w+r))/(a[i].w+s);
                  tm=0;
               }
               else
               {
                  tmp=d/(a[i].w+r);
                  tm-=tmp;
                  ans+=tmp;
               }
            }
            else
            {
               tmp=d/(double)(a[i].w+s);
               tm-=tmp;
               ans+=tmp;
            }
        }
        printf("Case #%ld: %.9lf\n",tst,ans);
    }
//    system("PAUSE");
    return 0;
}
