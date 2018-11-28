#include <cstdio>
#include <cmath>

#define ld long double

using namespace std;

int T, n, we=1;

int sX, sY, sZ, sA, sB, sC;
long double X, A, Y, B, Z, C;
long double a, b, c;

int main() {

    scanf("%d",&T);
    while (T--) {
        scanf("%d",&n);
        X = A = Y = B = Z = C = a = b = c = 0.0;
        sX = sY = sZ = sA = sB = sC = 0;
        for (int i=0;i<n;i++) {
            int x,y,z,vx1,vy1,vz1;
            scanf("%d %d %d %d %d %d",&x,&y,&z,&vx1,&vy1,&vz1);
            sX += x; sY += y; sZ += z;
            sA += vx1; sB += vy1; sC += vz1;
        }
        X = (ld)sX/(ld)n;
        Y = (ld)sY/(ld)n;
        Z = (ld)sZ/(ld)n;
        A = (ld)sA/(ld)n;
        B = (ld)sB/(ld)n;
        C = (ld)sC/(ld)n;
        a = A*A + B*B + C*C;
        b = 2.0*X*A + 2.0*Y*B + 2.0*Z*C;
        c = X*X + Y*Y + Z*Z;
        if (fabs(a) <= 10e-10) // a = 0
        { long double t = ((-1.0)*c)/b;
          if (fabs(b) > 10e-10)
          { printf("Case #%d: %.8Lf %.8Lf\n",we++,(long double)0.0,t); continue; }
          else // b = 0
          { printf("Case #%d: %.8Lf %.8Lf\n",we++,sqrt(c),(long double)0.0); continue; }
        }
        long double t = ((-1.0)*b)/(2.0*a);
        long double d = a*t*t + b*t + c;
        if (fabs(d) <= 10e-7) d = 0.0;
        if (fabs(t) <= 10e-7) t = 0.0;
        if (d > 0.0 and t > 0.0)
        { printf("Case #%d: %.8Lf %.8Lf\n",we++,sqrt(d),t); continue; }
        if (d > 0.0 and t < 0.0)
        { printf("Case #%d: %.8Lf %.8Lf\n",we++,sqrt(c),(long double)0.0); continue; }
        if (d < 0.0 and t > 0.0) {
            ld delta = b*b - 4*a*c;
            ld t1 = (-b + sqrt(delta))/(2*a);
            ld t2 = (-b - sqrt(delta))/(2*a);
            if (t1 < 0.0 and t2 < 0.0)
                { printf("Case #%d: %.8Lf %.8Lf\n",we++,sqrt(c),(ld)0.0); continue; }
            if (t1 < 0.0 and t2 > 0.0) t = t2;
            else if (t1 > 0.0 and t2 < 0.0) t = t1;
            else t = t1 < t2 ? t1 : t2;
            d = a*t*t + b*t + c;
            printf("Case #%d: %.8Lf %.8Lf\n",we++,sqrt(d),(ld)t); continue;
        }
        if (t < 0.0 and d < 0.0)
        { printf("Case #%d: %.8Lf %.8Lf\n",we++,sqrt(c),(long double)0.0); continue; }

        if (t < 0.0 and fabs(d) <= 10e-7)
        { printf("Case #%d: %.8Lf %.8Lf\n",we++,sqrt(c),(ld)0.0); continue; }
        
        { printf("Case #%d: %.8Lf %.8Lf\n",we++,sqrt(d),t); continue; }
    }

    return 0;
}
