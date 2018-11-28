#include<iostream>
using namespace std;
#define maxn 1100000
#define EPS 1e-8
long n,o,m,i,j,x,y,cas,tst;
double a[maxn],l,r,mid,w;
bool flag;
double max(double a,double b)
{
       if (a>b) return a;
       return b;
}
int main()
{
    freopen("b.in","r",stdin);
    freopen("b.txt","w",stdout);
    for (scanf("%ld",&cas),tst=1;tst<=cas;tst++)
    {
        n=0;
        for (scanf("%ld%ld",&o,&m);o>0;o--)
        {
            for (scanf("%ld%ld",&x,&y);y>0;y--) a[n++]=x;
        }
        l=0;
        r=1e20;
        while (l+EPS<r)
        {
              mid=(l+r)/2.0;
              w=-1e20;
              flag=0;
              for (i=0;i<n;i++)
              {
                  if (w>a[i]+mid) {flag=1;goto wa;}
                  w=max(w,a[i]-mid)+m;
              }
              wa:
              if (flag) l=mid;
                 else r=mid;
        }
        printf("Case #%ld: %.7lf\n",tst,l);
    }
//    system("PAUSE");
    return 0;
}
