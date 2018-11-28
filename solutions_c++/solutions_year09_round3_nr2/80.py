#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main() {
    int t;
    scanf("%d\n", &t);
    for (int tt=1; tt<=t; tt++) {
        int n;
        scanf("%d", &n);
        double c1x = 0;
        double c1y = 0;
        double c1z = 0;
        double c2x = 0;
        double c2y = 0;
        double c2z = 0;
        for (int i=0; i<n ;i++) {
            int x, y, z, vx, vy, vz;
            scanf("%d%d%d%d%d%d", &x, &y, &z, &vx, &vy, &vz);
            c1x += x;
            c1y += y;
            c1z += z;
            c2x += vx;
            c2y += vy;
            c2z += vz;
        }
        c1x /= n;
        c1y /= n;
        c1z /= n;
        c2x /= n;
        c2y /= n;
        c2z /= n;

        double tm;
        double q = (c2x*c2x + c2y*c2y + c2z*c2z);
        if (q!=0) {
            tm = -(c1x*c2x+c1y*c2y+c1z*c2z)/q;
            if (tm <= 0) tm = 0;
        } else {
            tm = 0;
        }
        double xm = c1x + c2x*tm;
        double ym = c1y + c2y*tm;
        double zm = c1z + c2z*tm;
        double dm = sqrt(xm*xm + ym*ym + zm*zm);
        printf("Case #%d: %.8lf %.8lf\n", tt, dm, tm);

    }

}
