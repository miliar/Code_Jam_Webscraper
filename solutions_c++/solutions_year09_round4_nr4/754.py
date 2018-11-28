#include <iostream>
#include <vector>
#include <cmath>
#include <cstring>
#include <algorithm>
using namespace std;

struct circle
{
    double x,y,r;
};

vector <circle> c;
int used[32];
int n,cir;

struct pom
{
    double r,x;
};

pom fxx(int u,double t)
{
    pom ret;
    double l=1;
    double r=1000;
    double t1=0,t2=100000;
    double r1,r2;
    double max1,max2,max;
    double hm;
    for(int asd=0;asd<64;asd++)
    {
        t1=l+(r-l)/3;
        t2=l+((r-l)/3)*2;
        max1=max2=0;
        for(int i=0;i<cir;i++)
        {
            if(used[i]==u)
            {
                hm=sqrt((c[i].x-t1)*(c[i].x-t1)+(c[i].y-t)*(c[i].y-t))+c[i].r;
                if(max1 < hm)
                {
                    max1 = hm;
                }
            }
        }
        for(int i=0;i<cir;i++)
        {
            if(used[i]==u)
            {
                hm=sqrt((c[i].x-t2)*(c[i].x-t2)+(c[i].y-t)*(c[i].y-t))+c[i].r;
                if(max2 < hm)
                {
                    max2 = hm;
                }
            }
        }
        if(max1<max2)
        {
            r=t2;
            max=max1;
        }
        else
        {
            l=t1;
            max=max2;
        }
    }
    ret.x=t1;
    ret.r=max;
    return ret;
}

circle look(int u)
{
    circle ret;
    double l=1;
    double r=1000;
    double t1,t2;
    pom r1,r2;
    for(int asd=0;asd<64;asd++)
    {
        t1=l+(r-l)/3;
        t2=l+((r-l)/3)*2;
        r1=fxx(u,t1);
        r2=fxx(u,t2);
        if(r1.r<r2.r)
        {
            r=t2;
        }
        else
        {
            l=t1;
        }
    }
    ret.x=r1.x;
    ret.y=t1;
    ret.r=r1.r;
    return ret;
}


int main()
{
    scanf("%d",&n);
    for(int ii = 1;ii<=n;ii++)
    {
        c.clear();
        memset(used,0,sizeof(used));
        scanf("%d",&cir);
        for(int j=0;j<cir;j++)
        {
            circle nc;
            scanf("%lf %lf %lf",&nc.x,&nc.y,&nc.r);
            c.push_back(nc);
        }
        double mx=0;
        int f,s;
        for(int j=0;j<cir;j++)
        {
            for(int k=0;k<cir;k++)
            {
                if(j==k) continue;
                double hm =sqrt((c[j].x-c[k].x)*(c[j].x-c[k].x)+(c[j].y-c[k].y)*(c[j].y-c[k].y)) + c[j].r+c[k].r;
                if(hm > mx)
                {
                    mx=hm;
                    f=j;s=k;
                }
            }
        }
        used[s]=1;
        double ans = 1000000;
        if(cir>2)
        {
            for(int kk=0;kk<cir-1;kk++)
            {
                circle r0=look(0);
                circle r1=look(1);
                if(ans>max(r0.r,r1.r)) ans = max(r0.r,r1.r);
                double min = 1000000;
                int ix;
                for(int i=0;i<cir;i++)
                {
                    double br=10000000;
                    if(used[i]==0)
                    {
                        br = sqrt((c[i].x-r1.x)*(c[i].x-r1.x)+(c[i].y-r1.y)*(c[i].y-r1.y))+c[i].r;
                    }
                    if(br<min)
                    {
                        ix=i;
                        min = br;
                    }
                }
                used[ix]=1;
            }
        }
        else{
            if(cir==1) ans = c[0].r;
            if(cir==2)
            {
                ans = max(c[0].r,c[1].r);
            }
        }
        printf("Case #%d: %lf\n",ii,ans);
    }
    return 0;
}
