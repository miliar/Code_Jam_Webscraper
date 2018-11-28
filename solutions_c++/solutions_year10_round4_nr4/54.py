#include<iostream>
#include<cmath>
using namespace std;
double pi=acos(-1.0);
double eps=1e-9;
struct point
{
       double x,y;
};
point p[3];
int n,m,cases,tt;
void init()
{
     scanf("%d%d",&n,&m);
     int i;
     for (i=0;i<n;i++)
         scanf("%lf%lf",&p[i].x,&p[i].y);
}

double dis(point p1,point p2)
{
       return hypot(p1.x-p2.x,p1.y-p2.y);
}

double yxdl(double l1,double l2,double l3)
{
       return acos((l1*l1+l2*l2-l3*l3)/2/l1/l2);
}

void work()
{
     printf("Case #%d:",tt+1);
     double r1,r0,d,ans,ang0,ang1;
     for (;m;m--)
     {
         scanf("%lf%lf",&p[2].x,&p[2].y);
         r0=dis(p[0],p[2]);
         r1=dis(p[1],p[2]);
         d=dis(p[0],p[1]);
         if (r0<r1)
         {
            swap(r0,r1);
            swap(p[0],p[1]);
         }
         if (d+r1+eps<r0) ans=r1*r1*pi;
         else
         if (r1+r0+eps<d) ans=0;
         else
         {
             ang0=yxdl(r0,d,r1);
             ang1=yxdl(r1,d,r0);
             ang0*=2;
             ang1*=2;
             ans=ang0*r0*r0-r0*r0*sin(ang0)+r1*r1*ang1;
             if (r0>d)
               ans+=r1*r1*sin(2*pi-ang1);
             else ans-=r1*r1*sin(ang1);
             ans/=2;
         }
         printf(" %.8lf",ans);
     }
     printf("\n");
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d",&cases),tt=0;tt<cases;tt++)
    {
        init();
        work();
    }
    return 0;
}
