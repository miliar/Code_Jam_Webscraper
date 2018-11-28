#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

const double zero = 1e-7;
const double pi = 3.1415926535897932384626433832795;
double p[10][2],r[10];

double dis(double x1,double y1,double x2,double y2){
    return sqrt((x1-x2) * (x1-x2) + (y1-y2) * (y1-y2));
}

double calc_abs(double k){
    if (k > 0) return k; return -k;
}

double solve(double x1,double y1,double r1,double x2,double y2,double r2){
    double d = dis(x1,y1,x2,y2);
    if (d<=calc_abs(r1-r2)){
        if (r1<r2) return pi*r1*r1;
            else return pi*r2*r2;
    }
    if (d>=r1+r2) return 0;
    double A = 2*(x2-x1), B = 2*(y2-y1), C = x1*x1-x2*x2+y1*y1-y2*y2-r1*r1+r2*r2;
    double d1 = calc_abs(A*x1+B*y1+C)/sqrt(A*A+B*B), d2 = calc_abs(A*x2+B*y2+C)/sqrt(A*A+B*B);
    double k = sqrt(r1*r1-d1*d1);
    double thet;
    if (calc_abs(d1) < zero)
        thet = pi/2 ;
    else thet = atan(k/d1);
    k = 0.5*r1*r1*sin(2*thet);
    double s;
    if (calc_abs(d2-d1-d) < zero)
        s = (2*pi-2*thet)/2*r1*r1+k;
    else s = thet*r1*r1-k;
    k = sqrt(r2*r2-d2*d2);
    if (calc_abs(d2) <zero)
        thet = pi/2 ; else thet = atan(k/d2);
    k = 0.5*r2*r2*sin(2*thet);
    if (calc_abs(d1-d2-d) < zero)
        s = s+(2*pi-2*thet)/2*r2*r2+k;
    else s = s+thet*r2*r2-k;
    return s;
}

int main()
{
    freopen("D.in","r",stdin); freopen("D.out","w",stdout);
    int t; scanf("%d",&t);
    for (int casenum=1; casenum<=t; ++casenum){
        printf("Case #%d:",casenum);
        int n,m; scanf("%d %d",&n,&m);
        for (int i=0; i<n; ++i)
            cin >> p[i][0] >> p[i][1];
        for (int i=1; i<=m; ++i){
            double t1,t2;
            cin >> t1 >> t2;
            for (int j=0; j<n; ++j)
                r[j] = dis(p[j][0],p[j][1],t1,t2);
            printf(" %.7f",solve(p[0][0],p[0][1],r[0],p[1][0],p[1][1],r[1]));
        }
        printf("\n");
    }
    return 0;
}
