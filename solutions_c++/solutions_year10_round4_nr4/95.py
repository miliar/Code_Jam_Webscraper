#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

const double pi=2.0*acos(0.0);

struct Point
{
    double x;
    double y;
    friend double getdist2(const Point &p1,const Point &p2)
    {
        return (p1.x-p2.x)*(p1.x-p2.x)+(p1.y-p2.y)*(p1.y-p2.y);
    }
    friend double getdist(const Point &p1,const Point &p2)
    {
        return sqrt(getdist2(p1,p2));
    }
};

struct Circle
{
    Point o;
    double r;
    friend double CircleCircle(Circle c1,Circle c2)
    {
        double dist,acos1,acos2;
        if(c1.r<c2.r)
        {
            swap(c1.r,c2.r);
        }
        dist=getdist(c1.o,c2.o);
        if(dist>=c1.r+c2.r)
        {
            return 0.0;
        }
        if(dist<=c1.r-c2.r)
        {
            return pi*c2.r*c2.r;
        }
        acos1=acos(0.5*(c1.r*c1.r+dist*dist-c2.r*c2.r)/(c1.r*dist));
        acos2=acos(0.5*(c2.r*c2.r+dist*dist-c1.r*c1.r)/(c2.r*dist));
        return (acos1-0.5*sin(2.0*acos1))*c1.r*c1.r+(acos2-0.5*sin(2.0*acos2))*c2.r*c2.r;
    }
};

Circle c1,c2;
Point p0;
int n,m;

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int i,c,t;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%d %d",&n,&m);
        scanf("%lf %lf",&c1.o.x,&c1.o.y);
        scanf("%lf %lf",&c2.o.x,&c2.o.y);
        printf("Case #%d:",c+1);
        for(i=0;i<m;i++)
        {
            scanf("%lf %lf",&p0.x,&p0.y);
            c1.r=getdist(c1.o,p0);
            c2.r=getdist(c2.o,p0);
            printf(" %.7f",CircleCircle(c1,c2));
        }
        printf("\n");
    }
    return 0;
}
