#include <cstdio>
#include <math.h>
#include <vector>
#include <string.h>
using namespace std;

int main(){
        int T, ca=0;
        scanf("%d", &T);
        while (T--){
                int n;
                scanf("%d", &n);
                double xc, yc, zc, xt, yt, zt, xt2, yt2, zt2;
                xc = yc = zc = xt = yt = zt = xt2 = yt2 = zt2 = 0;
                for (int i=0; i<n; i++){
                        int x, y, z, vx, vy, vz;
                        scanf("%d%d%d%d%d%d", &x, &y, &z, &vx, &vy, &vz);
                        xc += x;
                        yc += y;
                        zc += z;
                        xt += vx;
                        yt += vy;
                        zt += vz;
                }
                xc /= n;
                yc /= n;
                zc /= n;
                xt /= n;
                yt /= n;
                zt /= n;

                xt2 = xt*xt;
                yt2 = yt*yt;
                zt2 = zt*zt;
                xt = 2*xc*xt;
                yt = 2*yc*yt;
                zt = 2*zc*zt;
                xc = xc*xc;
                yc = yc*yc;
                zc = zc*zc;
/*
                printf("%lf %lf %lf\n", xc, yc, zc);
                printf("%lf %lf %lf\n", xt, yt, zt);
                printf("%lf %lf %lf\n", xt2, yt2, zt2);
                printf("===\n");
*/
                double ac, at, at2;
                ac = xc + yc + zc;
                at = xt + yt + zt;
                at2 = xt2 + yt2 + zt2;

                double sec;
                if (at2==0) sec = 0;
                else
                 sec = -at/(at2*2);
                if (sec<0) sec = 0;
                //printf("OPPS\n");
                double tmp = fabs(ac+at*sec+at2*sec*sec);
                double dis;
                dis = sqrt(tmp);
                printf("Case #%d: %.8lf %.8lf\n", ++ca, dis, sec+1e-12);

        }

        return 0;
}
