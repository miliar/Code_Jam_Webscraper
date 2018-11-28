#define eps 1e-10
#include <iostream>
#include <cmath>
using namespace std;
double a,b,c,d,e,f,ax,ay,az,vx,vy,vz;
int n;
double sqr(double x){
    return x*x;
}
double dcmp(double x){
    return (x<-eps)?-1:(x>eps);
}
int main(){
    int test; scanf("%d",&test);
    for (int Case = 1 ; Case <= test ; Case++){
        scanf("%d",&n); ax=ay=az=vx=vy=vz=0;
        for (int i=0;i<n;i++){
            scanf("%lf%lf%lf%lf%lf%lf",&a,&b,&c,&d,&e,&f);
            ax+=a, ay+=b, az+=c, vx+=d, vy+=e, vz+=f;
        }
        ax/=n, ay/=n, az/=n, vx/=n, vy/=n, vz/=n;
        double A=sqr(vx)+sqr(vy)+sqr(vz);
        double B=(ax*vx+ay*vy+az*vz)*2;
        double C=sqr(ax)+sqr(ay)+sqr(az);
        double t = 0;
        if (dcmp(A)!=0) t -= B / (2*A);
        if (dcmp(t)<0) t = 0;
        double ans=sqrt(sqr(ax+t*vx)+sqr(ay+t*vy)+sqr(az+t*vz));
        printf("Case #%d: %.8lf %.8lf\n",Case,ans,t);
    }
}
