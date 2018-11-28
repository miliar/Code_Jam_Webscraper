#include <cstdio>
#include <cmath>

const double eps=1e-11;
const double PI=3.1415926535897932384626433832795;
double f,R,t,r,g;

inline double len(double x,double y){
    return sqrt(x*x+y*y);
}
double calc(double x,double y){
    double a=g-2*f;
    double area;
	double rr=R-t-f;
    if(len(x+a,y+a)<rr-eps) area=a*a;
    else if(len(x,y)>rr+eps) area=0;
    else if(len(x,y+a)<rr-eps&&len(x+a,y)<rr-eps){
        double xx=sqrt((rr)*(rr)-(y+a)*(y+a));
        double yy=sqrt((rr)*(rr)-(x+a)*(x+a));
        area=(yy-y)*a+(xx-x)*(y+a-yy)+calc(xx,yy);
    }
    else if(len(x,y+a)>rr+eps&&len(x+a,y)<rr-eps){
        double yy=sqrt((rr)*(rr)-(x+a)*(x+a));
        area=(yy-y)*a+calc(x,yy);
    }
    else if(len(x,y+a)<rr-eps&&len(x+a,y)>rr+eps){
        double xx=sqrt((rr)*(rr)-(y+a)*(y+a));
        area=(xx-x)*a+calc(xx,y);
    }
    else{
        double a1=acos(x/(rr));
        double a2=asin(y/(rr));
        double a3=atan2(y,x);
        area=0.5*(rr)*(rr)*(a1-a2)-0.5*(rr)*len(x,y)*sin(a1-a3)-0.5*(rr)*len(x,y)*sin(a3-a2);
    }
    return area;
}
double sol(){
    if(fabs(f*2-g)<eps) return 1;
    double i,j,area;
    area=0;
    for(i=r+f;i<R-t+eps;i+=g+2*r){
        for(j=r+f;j<R-t+eps;j+=g+2*r){
            area+=calc(i,j);
        }
    }
    return 1-4*area/PI/R/R;
}
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);
    int cas,ic;
    scanf("%d",&cas);
    for(ic=1;ic<=cas;ic++){
        scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
        printf("Case #%d: %lf\n",ic,sol());
    }
    return 0;
}
