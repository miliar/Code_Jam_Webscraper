#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
using namespace std;

const double pi=2.0*acos(0.0);

struct Point
{
    double x;
    double y;
    friend double dist(const Point &a,const Point &b)
    {
        return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
    }
    friend double dot_product(const Point &a,const Point &b)
    {
        return a.x*b.x+a.y*b.y;
    }
    friend double cross_product(const Point &a,const Point &b)
    {
        return a.x*b.y-b.x*a.y;
    }
};

Point lx,rx,ls,xs,xx,zero;
double f,R,t,r,g,sp,st,R2,r2,Rf2;
int n;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int k;
    double x,y,limit,delta;
    zero.x=zero.y=0.0;
    scanf("%d",&n);
    for(k=0;k<n;k++)
    {
        scanf("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
        printf("Case #%d: ",k+1);
        if((2.0*f>=g)||(f+t>=R))
        {
            printf("1.000000\n");
            continue;
        }
        st=0.25*pi*R*R;
        sp=0.0;
        R=R-t;
        R2=R*R;
        r2=r*r;
        Rf2=(R-f)*(R-f);
        limit=sqrt(R2-r2);
        delta=(2.0*r+g);
        for(x=r;x<limit;x=x+delta)
        {
            for(y=r;y<limit;y=y+delta)
            {
                if(x*x+y*y<R2)
                {
                    if((x+g)*(x+g)+(y+g)*(y+g)<R2)
                    {
                        sp=sp+(g-2.0*f)*(g-2.0*f);
                    }
                    else
                    {
                        lx.x=x+f;
                        lx.y=y+f;
                        if(lx.x*lx.x+lx.y*lx.y<Rf2)
                        {
                            rx.y=lx.y;
                            rx.x=min(lx.x+g-2.0*f,sqrt(max(Rf2-rx.y*rx.y,0.0)));
                            ls.x=lx.x;
                            ls.y=min(lx.y+g-2.0*f,sqrt(max(Rf2-ls.x*ls.x,0.0)));
                            xs.y=ls.y;
                            xs.x=sqrt(max(Rf2-xs.y*xs.y,0.0));
                            xx.x=rx.x;
                            xx.y=sqrt(max(Rf2-xx.x*xx.x,0.0));
                            sp=sp+(xs.x-lx.x)*(xs.y-lx.y)+(xx.x-xs.x)*(xx.y-lx.y)+0.5*(xx.x-xs.x)*(xs.y-xx.y)+0.5*(acos(fabs(dot_product(xs,xx)/(dist(xs,zero)*dist(xx,zero))))*Rf2-fabs(cross_product(xs,xx)));
                        }
                    }
                }
            }
        }
        printf("%.6f\n",1.0-(sp/st));
    }
    return 0;
}
