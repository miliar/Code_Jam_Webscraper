#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <utility>
#include <functional>
#include <sstream>
#include <climits>
#include <cfloat>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstring>
#include <cstdio>
using namespace std;

const int N=200;
const double eps=1e-10;
int w,l,u,g;

struct tpoint
{
    double x,y;
    tpoint(double x=0,double y=0)
    {
        this->x=x;
        this->y=y;
    }
};

struct tvect
{
    double x,y;
    tvect(const tpoint &start,const tpoint &finish)
    {
        x=finish.x-start.x;
        y=finish.y-start.y;
    }
};

tvect operator*(double k, const tvect &v)
{
    tvect res(v);
    res.x*=k;
    res.y*=k;
    return res;
}

tpoint operator+(const tpoint &p, const tvect &v)
{
    return tpoint(p.x+v.x,p.y+v.y);
}

tpoint up[N],low[N];

double vect_mul(const tvect &v1, const tvect &v2)
{
    return v1.x*v2.y-v1.y*v2.x;
}

double f(double x)
{
    tpoint p(up[0]);
    int t=1;
    double res=vect_mul(tvect(tpoint(),low[0]),tvect(tpoint(),up[0]));
    while(t<u && up[t].x<=x)
    {
        tvect v1(tpoint(),p);
        tvect v2(tpoint(),up[t]);
        res+=vect_mul(v1,v2);
        p=up[t++];
    }
    if(t<u)
    {
        double k=(x-p.x)/(up[t].x-p.x);
        tvect v(p,up[t]);
        v=k*v;
        tpoint np=p+v;
        tvect v1(tpoint(),p);
        tvect v2(tpoint(),np);
        res+=vect_mul(v1,v2);
        p=np;
    }
    tpoint p2(low[0]);
    t=1;
    while(t<l && low[t].x<=x)
    {
        tvect v2(tpoint(),p2);
        tvect v1(tpoint(),low[t]);
        res+=vect_mul(v1,v2);
        p2=low[t++];
    }
    if(t<l)
    {
        double k=(x-p2.x)/(low[t].x-p2.x);
        tvect v(p2,low[t]);
        v=k*v;
        tpoint np=p2+v;
        tvect v2(tpoint(),p2);
        tvect v1(tpoint(),np);
        res+=vect_mul(v1,v2);
        p2=np;
    }
    res+=vect_mul(tvect(tpoint(),p),tvect(tpoint(),p2));
    return fabs(res);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int Tests;
    scanf("%d",&Tests);
    for(int Test=1;Test<=Tests;Test++)
    {
        printf("Case #%d:\n", Test);
        //
        scanf("%d%d%d%d",&w,&l,&u,&g);
        for(int i=0;i<l;i++)
        {
            int x,y;
            scanf("%d%d",&x,&y);
            low[i]=tpoint(x,y);
        }
        for(int i=0;i<u;i++)
        {
            int x,y;
            scanf("%d%d",&x,&y);
            up[i]=tpoint(x,y);
        }
        //
        double d=f(w+1)/g;
        for(int i=1;i<g;i++)
        {
            double l=0,r=w;
            while(r-l>=eps)
            {
                double c=(l+r)/2;
                if(f(c)>i*d)
                    r=c;
                else
                    l=c;
            }
            printf("%.10lf\n",(l+r)/2);
        }
    }
}
