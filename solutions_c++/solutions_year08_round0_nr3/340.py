#include<cstdio>
#include<cmath>
using namespace std;
double f,R,t,r,g;
double dbg;
double s(double x) {
    return x*x;
}
double integral(double x,double a, double b, double r) {
  double t1=sqrt(s(r)-s(a-x) )*(a-x)/(s(a-x)-s(r));
  double t2=1/2.0*atan(t1)*s(r);
  double t3=1/2.0*sqrt(s(r)-s(a-x))*(a-x)-b*x;
  return t2-t3;
}
double integral2(double x,double r) {
    double xxx= 1/2.0*(atan(x/sqrt(r*r-x*x))*r*r+x*sqrt(r*r-x*x) );
    return xxx;
}
double square(double x1,double y1,double x2,double y2) {
    if(x1>=x2) return 0;
    double tmp=R-t-f;
    if(x1*x1+y1*y1>=tmp*tmp) return 0;
    if(x2*x2+y2*y2<=tmp*tmp) return (x2-x1)*(x2-x1);
    double u=sqrt(tmp*tmp-y1*y1);
    double w;
    if(u>x2) u=x2;
    if(x1*x1+y2*y2>=tmp*tmp)w=x1; else w=sqrt(tmp*tmp-y2*y2);
//    printf("%lf %lf\n",u,w);
    return integral2(u,tmp)-integral2(w,tmp)-y1*(u-w)+(w-x1)*(y2-y1);
}
int main() {
    int n;
    scanf("%d",&n);
    for(int xxx=0;xxx<n;++xxx) {
        dbg=0;
        scanf("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
        double res=0;
        for (double x=0;x<R-t-f;x+=r+r+g) {
          for (double y=0;y<R-t-f;y+=r+r+g) {
              res+=square(x+f+r,y+f+r,x+r+g-f,y+r+g-f);
          }
        }
        double pi=3.141592653589;
        double obsah=pi*R*R;
  //      printf("res=%.10lf\n",res*4.0);
   //     printf("obs=%.10lf\n",obsah);
        printf("Case #%d: %.7lf\n",xxx+1,(obsah-4.0*res)/obsah);
    } //end case
}

