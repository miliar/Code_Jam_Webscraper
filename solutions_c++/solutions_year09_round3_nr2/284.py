#include<iostream>
#include<math.h>
double pos[500][3];
double vel[500][3];
using namespace std;
int main()
{
int t,p;
cin>>t;
for(int j=1;j<=t;j++)
{
    int n;
    cin>>n;
    //double x[500],vx[500],y[500],z[500],vy[500],vz[500];
    double inx=0,vx=0,iny=0,inz=0,vz=0,vy=0,pp,vv,pv,time;
    double d;
    for(int i=0;i<n;i++)
    {
        cin>>pos[i][0]>>pos[i][1]>>pos[i][2]>>vel[i][0]>>vel[i][1]>>vel[i][2];
        inx+=pos[i][0];
        vx+=vel[i][0];
        iny+=pos[i][1];
        vy+=vel[i][1];
        inz+=pos[i][2];
        vz+=vel[i][2];
    }
    inx/=n;vx/=n;
    iny/=n;vy/=n;
    inz/=n;vz/=n;
    pp=inx*inx+iny*iny+inz*inz;
    vv=vx*vx+vy*vy+vz*vz;
    pv=inx*vx+iny*vy+inz*vz;
    if(vv!=0)
    time=(pv/vv)*(-1);
    else
    time=0;
    if(time<0)
    {
    time=0;
    }
    d=pow((inx+vx*time),2.0)+pow((iny+vy*time),2.0)+pow((inz+vz*time),2.0);
    
    d=sqrt(d);
    printf("Case #%d: %0.8lf %0.8lf\n",j,d,time);
// cout<<d<<" "<<t;
}
return 0;
}
