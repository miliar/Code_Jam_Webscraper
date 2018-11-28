#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#define REP(i,n)	for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,s,k)	for(int i=(s),_k=(k);i<=_k;++i)
#define FORD(i,s,k)	for(int i=(s),_k=(k);i>=_k;--i)
#define FORE(it,q)	for(__typeof((q).begin())it=(q).begin();it!=(q).end();++it)
using namespace std;

int main()
{
	int TT;
	double R,t,r,g;
	double f1,R1,t1,r1,g1;
	scanf("%d",&TT);
	FOR(cs,1,TT) {
        scanf("%lf%lf%lf%lf%lf",&f1,&R1,&t1,&r1,&g1);
        R = R1;
        t = t1 + f1;
        g = g1 - 2*f1;
        r = r1 + f1;
        double P;
        if(g <= 0) P = 1.0;
        else {
            double full = g*g;
            double area = .0;
            int k = 0;
            while(r + k*(g + 2*r) <= R-t) {
                double x0 = r + k*(g+2*r);
                double x1 = g + r + k*(g+2*r);
                int ile = 0;
                if(R-t - x1 >= 0) 
                    ile = (int)(sqrt((R-t)*(R-t) - x1*x1)/(g+2*r));
                    
                //printf("k = %d, ile = %d\n", k, ile);                    
                
                area += ile*full;
                int m = 0;
                while(r + (ile+m)*(g+2*r) <= sqrt((R-t)*(R-t) - x0*x0)) {
                    double y0 = r + (ile+m)*(g+2*r);
                    double y1 = r + (ile+m)*(g+2*r) + g;
                    //printf("x0: %lf, x1: %lf, y0: %lf, y1: %lf\n", x0,x1,y0,y1);
                    double X0,X1,X2;
                    if((R-t) >= y1) {
                        double x2 = sqrt((R-t)*(R-t) - y1*y1);
                        if(x2 <= x0) X0 = X1 = x0, X2 = x1;
                        else if(x2 > x0 && x2 <= x1)
                            X0 = x0, X1 = x2, X2 = x1;
                        else    
                            X0 = x0, X1 = x1, X2 = x1;
                    } else {
                        X0 = X1 = x0;
                        X2 = x1;
                    }
                    
                    //printf("(1): X0: %lf, X1: %lf, X2: %lf\n", X0, X1, X2);
                    double x2 = sqrt((R-t)*(R-t)-y0*y0);
                    if(x2 >= x0 && x2 <= x1) 
                        X2 = x2;
                    else if(x2 > x1) 
                        X2 = x1;
                    
                    //printf("(2): X0: %lf, X1: %lf, X2: %lf\n", X0, X1, X2);
                    
                    
                    if(y1-y0 > 0 && X1-X0 > 0) {
                        //printf("tak\n");
                        area += (y1-y0)*(X1-X0);
                    }

                    if(X1 < X2) {
                        //printf("calkuje: %lf - %.10lf\n", X1, X2);
                        double a = R-t;
                        double z = (X2 * sqrt(a*a - X2*X2) + a*a*atan(X2/sqrt(a*a-X2*X2)))/2
                                - ((X1 * sqrt(a*a - X1*X1) + a*a*atan(X1/sqrt(a*a-X1*X1)))/2)
                                - (X2-X1)*y0;
                        //printf("z: %lf\n", z);
                        if(z > 0)
                            area += z;
                    }
                    ++m;
                }
                ++k;
            }
            P = 1. - 4.*area/(M_PI*R*R);
        }
        printf("Case #%d: %lf\n", cs, P);
    }
}
