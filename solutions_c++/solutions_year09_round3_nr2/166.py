#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

void opens(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
}

void openb(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
}

#define MAXN 501
int tes,x[MAXN],y[MAXN],z[MAXN],vx[MAXN],vy[MAXN],vz[MAXN],n;
double hi,lo,fhi,flo;

double sqr(double a){
    return a*a;
}

double cnt(double x,double y,double z){
    return sqrt(x*x+y*y+z*z);
}

double counts(double a){
    double xtot,ytot,ztot;
    xtot=0.0;
    ytot=0.0; 
    ztot=0.0;
    for (int j=0;j<n;j++){
        xtot+=(double)x[j]+(double)vx[j]*a;
        ytot+=(double)y[j]+(double)vy[j]*a;
        ztot+=(double)z[j]+(double)vz[j]*a;
    }
    xtot/=(double)n;
    ytot/=(double)n;
    ztot/=(double)n;
    return cnt(xtot,ytot,ztot);
}

int main(){
    //opens();
    openb();
    scanf("%d",&tes);
    for (int i=1;i<=tes;i++){
        scanf("%d",&n);
        for (int j=0;j<n;j++){
            scanf("%d %d %d %d %d %d",&x[j],&y[j],&z[j],&vx[j],&vy[j],&vz[j]);
        }
        lo=0.0;hi=1000000000.0;
        flo=counts(lo);fhi=counts(hi);
        while (fabs(hi-lo)>1e-9){
            double mid=(lo+hi)/2.0;
            double fmid=counts(mid);
            if (flo>fhi){
                flo=fmid;
                lo=mid;
            }
            else {
                fhi=fmid;
                hi=mid;
            }
        }
        printf("Case #%d: %lf %lf\n",i,flo,lo);
    }
    //system("pause");
    return 0;
}
