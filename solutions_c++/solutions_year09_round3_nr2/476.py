#include<iostream>
#include<cmath>
using namespace std;

int main() {
    FILE* fin = freopen("input.in", "r", stdin);
    int T;
    cin >> T;

    for (int tt=0;tt<T;++tt) {
        int N;
        cin >> N;

        double x=0, y=0, z=0, a=0, b=0, c=0;
        for (int i=0;i<N;++i) {
              double xi, vx, yi, vy, zi, vz;
              cin >> xi >> yi >> zi >> vx >> vy >> vz;
              x += xi;
              y += yi;
              z += zi;
              a += vx;
              b += vy;
              c += vz;
        }
        x /= N;
        y /= N;
        z /= N;
        a /= N;
        b /= N;
        c /= N;

        double A = a*a + b*b + c*c;
        double B = 2*a*x + 2*b*y + 2*c*z;
        double C = x*x + y*y + z*z;

        double d, t;
        if (abs(A) < 1e-12) {
            t = 0;
            d = sqrt(C);
        }
        else {
            t = - B / (2 * A);
            if (t < 1e-12) t = 0;
            d = A*t*t + B*t + C; 
            if (d < 1e-12)
                d = 0;
            else
                d = sqrt(d);
        }

        printf("Case #%d: %.8lf %.8lf\n", tt+1, d, t);
    }
    return 0;
}
