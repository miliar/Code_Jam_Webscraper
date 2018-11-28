#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

double x[40],y[40],r[40];
int n;
const double epsi=1e-6;

bool inside(double x1,double y1,double r1,double x,double y,double r)
{
    if (r-r1>epsi)  return 0;
    return ((r1-r)*(r1-r)-(x1-x)*(x1-x)-(y1-y)*(y1-y))>-epsi;
}

int cal(double x1,double y1,double x2,double y2,double range)
{
    int ret=0;
    for (int i=0;i<n;i++)
        ret+=(inside(x1,y1,range,x[i],y[i],r[i])|inside(x2,y2,range,x[i],y[i],r[i]));
    return ret;
}

int mcount(double x1,double y1,double r1)
{
    return cal(x1,y1,x1,y1,r1);  
}

void get(double x1,double y1,double r1,double x2,double y2,double r2,double &px1,double &py1,double &px2,double &py2)
{
    px1=py1=px2=py2=0;
    double mx=x2-x1,sx=x2+x1,mx2=mx*mx;
    double my=y2-y1,sy=y2+y1,my2=my*my;
    double sq=mx2+my2,d=-(sq-(r1-r2)*(r1-r2))*(sq-(r1+r2)*(r1+r2));
    if (d+epsi<0)    return ;
    if (d<epsi)
        d=0;
    else
        d=sqrt(d);
    double x=mx*((r1+r2)*(r1-r2)+mx*sx)+sx*my2;
    double y=my*((r1+r2)*(r1-r2)+my*sy)+sy*mx2;
    double dx=mx*d,dy=my*d;sq*=2;
    px1=(x-dy)/sq;py1=(y+dx)/sq;
    px2=(x+dy)/sq;py2=(y-dx)/sq;
    //cout<<(px1-x1)*(px1-x1)+(py1-y1)*(py1-y1)-r1*r1<<endl;
    //cout<<(px1-x2)*(px1-x2)+(py1-y2)*(py1-y2)-r2*r2<<endl;
}

bool check(double range)
{
    if (n==1)   return range-r[0]>epsi;
    if (n==2)   return range-max(r[0],r[1])>epsi;
    for (int i=0;i<n;i++)
        if (range-r[i]>epsi)
        {
            for (int j=0;j<n;j++)
                if (j!=i&&range-r[j]>epsi)
                    for (int k=0;k<n;k++)
                        if (k!=i&&k!=j&&range-r[k]>epsi)
                        {
                            /*
                            x[j],y[j],range-r[j]
                            x[k],y[k],range-r[k]
                            */
                            double px1,px2,py1,py2;
                            get(x[j],y[j],range-r[j],x[k],y[k],range-r[k],px1,py1,px2,py2);
                            //cout<<inside(px1,py1,range,x[j],y[j],r[j])<<endl;
                            if (mcount(px1,py1,range)-inside(px1,py1,range,x[i],y[i],r[i])==n-1) return 1;
                            if (mcount(px2,py2,range)-inside(px2,py2,range,x[i],y[i],r[i])==n-1) return 1;
                        }   
        }   
    for (int i=0;i<n;i++)
        if (range-r[i]>epsi)
            for (int j=0;j<n;j++)
                if (j!=i&&range-r[j]>epsi)
                    for (int a=0;a<n;a++)
                        if (a!=i&&a!=j&&range-r[a]>epsi)
                            for (int b=0;b<n;b++)
                                if (b!=i&&b!=j&&b!=a&&range-r[b]>epsi)
                                {
                                    double px1,px2,py1,py2,qx1,qx2,qy1,qy2;
                                    get(x[i],y[i],range-r[i],x[j],y[j],range-r[j],px1,py1,px2,py2);
                                    get(x[a],y[a],range-r[a],x[b],y[b],range-r[b],qx1,qy1,qx2,qy2);
                                    if (cal(px1,py1,qx1,qy1,range)==n) return 1;   
                                    if (cal(px1,py1,qx2,qy2,range)==n) return 1;
                                    if (cal(px2,py2,qx1,qy1,range)==n) return 1;
                                    if (cal(px2,py2,qx2,qy2,range)==n) return 1;
                                }
    return 0;
}

main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int task;
    cin>>task;
    for (int t=0;t<task;t++)
    {
        cin>>n;
        for (int i=0;i<n;i++)
            cin>>x[i]>>y[i]>>r[i];
        double l=0,r=1e4,m;
        while (r-l>epsi)
        {
            m=(l+r)/2;
            if (check(m))
                r=m;
            else 
                l=m;   
        }        
        printf("Case #%d: %.6lf\n",t+1,l);
    }   
}
