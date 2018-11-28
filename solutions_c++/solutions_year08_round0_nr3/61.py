#include <math.h>
#include <iostream>

using namespace std;

double integrate(double px, double py, double dp, double lr) {
    int nx=1000;
    double dx = dp/nx;
    double x0 = px+.5*dx;
    double lrsq = lr*lr;
    double area = 0;
    for (int i=0; i<nx; i++) {
        double x = x0+i*dx;
        if (x > lr) break;
        double dy = sqrt(lrsq-x*x)-py;
        if (dy < 0) break;
        dy <?= dp;
        area += dx*dy;
    }
    return area;
}

main() {
    int nc;
    cin >> nc;
    for (int ic=0; ic<nc; ic++) {
        double f, br, t, r, g;
        cin >> f >> br >> t >> r >> g;
        double dp = g-2*f;
        double dpsq = dp*dp;
        if (dp <= 0) {
            cout << "Case #" << ic+1 << ": " << 1. << endl;
            continue;
        }
        double allarea = .25*M_PI*br*br;
        double area = 0;
        double p0 = r+f;
        double pstep = g+2*r;
        double lr = br-t-f;
        double lrsq = lr*lr;

        for (int iy=0; true; iy++) {
            double py = p0 + iy*pstep;
            double pysq = py*py;
            if (py > lr) break;
            double pyc = py+dp;
            double pye = pyc;
            pye <?= lr;
            double lrx = sqrt(lrsq-pye*pye);
            int nin = int((lrx-p0-dp)/pstep);
            nin >?= 0;
            area += nin*dpsq;
            for (int ix=nin; true; ix++) {
                double px = p0 + ix*pstep;
                if ( px*px + pysq > lrsq ) break;
                area += integrate(px, py, dp, lr);
            }
        }
        double prob = 1.-area/allarea;
        prob >?= 0;
        cout << "Case #" << ic+1 << ": " << prob << endl;
    }
}
