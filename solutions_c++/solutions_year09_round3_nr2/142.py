#include <iostream>
#include <cmath>

using namespace std;

long long vx[1000], vy[1000], vz[1000], x[1000], y[1000], z[1000];

int main() {

    long long c, n;

    cin >> c;
    for (int i = 1; i <= c; i++) {
        cin >> n;
        long long sum_x = 0, sum_y = 0, sum_z = 0, sum_vx = 0, sum_vy = 0, sum_vz = 0;
        for (int j = 0; j < n; j++) {
            cin >> x[j] >> y[j] >> z[j] >> vx[j] >> vy[j] >> vz[j];
            sum_x += x[j]; sum_y += y[j]; sum_z += z[j];
            sum_vx += vx[j]; sum_vy += vy[j]; sum_vz += vz[j];
        }
        double A = sum_vx*sum_vx + sum_vy*sum_vy + sum_vz*sum_vz;
        double B = 2*(sum_x*sum_vx + sum_y*sum_vy + sum_z*sum_vz);
        double C = sum_x*sum_x + sum_y*sum_y + sum_z*sum_z;
        
        double t = 0.0;
        if (A == 0) {
            if (B == 0) {
                
            } else {
                
            }
        } else {

            t = (-B) / (2*A);

        }
        if ( t < 0.0 ) t = 0.0;

               
        double p = sqrt( pow((sum_x+t*sum_vx)/n, 2.0) + pow( (sum_y+t*sum_vy)/n, 2.0) + pow((sum_z+t*sum_vz)/n, 2.0) );

        printf("Case #%d: %.12lf %.12lf\n", i, p, t);
    }

    return 0;
}
