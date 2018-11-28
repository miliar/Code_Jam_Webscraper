#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<map>
#include<iostream>
#include<cmath>
using namespace std;

int n,t;

double dist (double a,double b,double c) {
    return sqrt(a*a+b*b+c*c);
}

int main() {
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&t);
    for (int i=0; i<t; i++) {
        scanf("%d",&n);
        vector<double> ix,iy,iz,vx,vy,vz;
        ix.resize(n); iy.resize(n); iz.resize(n);
        vx.resize(n); vy.resize(n); vz.resize(n);
        for (int j=0; j<n; j++)
            scanf("%lf%lf%lf%lf%lf%lf",&ix[j],&iy[j],&iz[j],&vx[j],&vy[j],&vz[j]);
        double mi=0.0,mx=1e7,mt,md;
        while (mx-mi>1e-8) {
           double m1=mi+(mx-mi)/3,m2=mi+(mx-mi)/3*2;
           //printf("m:%0.3lf %0.3lf\n",m1,m2);
           double err1=0.0,err2=0.0,ex1,ex2,ey1,ey2,ez1,ez2;
           ex1=ex2=ey1=ey2=ez1=ez2=0.0;
           for (int j=0; j<n; j++) {
               ex1+=ix[j]*1.0+vx[j]*1.0*m1; ex2+=ix[j]+vx[j]*1.0*m2;
               ey1+=iy[j]*1.0+vy[j]*1.0*m1; ey2+=iy[j]+vy[j]*1.0*m2;
               ez1+=iz[j]*1.0+vz[j]*1.0*m1; ez2+=iz[j]+vz[j]*1.0*m2;
               //printf("%0.3lf %0.3lf %0.3lf   %0.3lf %0.3lf %0.3lf\n",ix[j]*1.0+vx[j]*1.0*m1,iy[j]+vy[j]*1.0*m1,iz[j]+vz[j]*1.0*m1,ix[j]+vx[j]*1.0*m2,iy[j]+vy[j]*1.0*m2,iz[j]+vz[j]*1.0*m2);
               //printf(" %0.3lf %0.3lf %0.3lf   %0.3lf %0.3lf %0.3lf\n",ex1,ey1,ez1,ex2,ey2,ez2);
               }
           //printf("    %0.3lf %0.3lf %0.3lf   %0.3lf %0.3lf %0.3lf\n",ex1,ey1,ez1,ex2,ey2,ez2);
           ex1/=n; ex2/=n;
           ey1/=n; ey2/=n;
           ez1/=n; ez2/=n;
           err1=dist(ex1,ey1,ez1);
           err2=dist(ex2,ey2,ez2);
           //printf("    %0.3lf %0.3lf %0.3lf   %0.3lf %0.3lf %0.3lf\n",ex1,ey1,ez1,ex2,ey2,ez2);
           //printf("%0.3lf: %0.9lf  %0.3lf: %0.9lf\n",m1,err1,m2,err2);
           if (err1<=err2) { mx=m2; mt=m1; md=err1; }
              else { mi=m1; mt=m2; md=err2; }
           if (m2-m1>=10000 && abs(err1-err2)<1e-7) { mx=1e-7; mi=0; }
           }
        printf("Case #%d: %0.8lf %0.8lf\n",i+1,md,mt);
        }
    
}
