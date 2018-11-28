#include <stdio.h>
#include <iostream>
#include <string.h>
#include <math.h>

using namespace std;

const double err = 1e-9;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);

    int T,Ti,N,Ni;
    cin >> T;
    int x,y,z,vx,vy,vz;
    double cx,cy,cz,dx,dy,dz;
    for (Ti=0; Ti<T; ++Ti) {
        cin >> N;
        cx = cy = cz = dx = dy = dz = 0.0;
        for (Ni=0; Ni<N; Ni++) {
            cin >> x >> y >> z >> vx >> vy >> vz;
            cx += x;
            cy += y;
            cz += z;
            dx += vx;
            dy += vy;
            dz += vz;
        }
        cx /= N;
        cy /= N;
        cz /= N;
        dx /= N;
        dy /= N;
        dz /= N;

        double speed = sqrt( dx*dx + dy*dy + dz*dz );
        double dis = sqrt( cx*cx + cy*cy + cz*cz );
        if (dis < err || speed < err) {
            // printf("  case = %d\n", Ti+1);
            // printf("  x,y,z = (%.2lf, %.2lf, %.2lf), dx,dy,dz = (%.2lf, %.2lf, %.2lf)\n", cx,cy,cz,dx,dy,dz);
            printf("Case #%d: %.8lf %.8lf\n", Ti+1, dis, 0.0);
            continue;
        }

        double thecos = (dx*cx + dy*cy + dz*cz) / sqrt( (dx*dx + dy*dy + dz*dz) * (cx*cx + cy*cy + cz*cz) );

        if (thecos > -err) {
            // printf("  case = %d, cos = %.2lf\n", Ti+1, thecos);
            // printf("  x,y,z = (%.2lf, %.2lf, %.2lf), dx,dy,dz = (%.2lf, %.2lf, %.2lf)\n", cx,cy,cz,dx,dy,dz);
            printf("Case #%d: %.8lf %.8lf\n", Ti+1, dis, 0.0);
            continue;
        }

        if (thecos + 1 < err) {
            // printf("  case = %d, cos = %.2lf\n", Ti+1, thecos);
            // printf("  x,y,z = (%.2lf, %.2lf, %.2lf), dx,dy,dz = (%.2lf, %.2lf, %.2lf)\n", cx,cy,cz,dx,dy,dz);
            printf("Case #%d: %.8lf %.8lf\n", Ti+1, 0.0, dis/speed);
            continue;
        }

        double L = thecos * sqrt( cx*cx + cy*cy + cz*cz );
        if (L<0) L = -L;
        double ans = sqrt( cx*cx + cy*cy + cz*cz - L*L );

        printf("Case #%d: %.8lf %.8lf\n", Ti+1, ans, L/speed);
    }

    return 0;
}
