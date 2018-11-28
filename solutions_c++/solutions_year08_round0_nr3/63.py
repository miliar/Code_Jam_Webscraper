#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iterator>
#include <functional>
#include <utility>
#include <numeric>
#include <complex>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) ((c).begin()), ((c).end())

typedef complex<double> P;

const double PI = acos(0.0) * 2;
const double EPS = 1.0e-8;

double integrate0(double r, double xs, double xt, double y0) {
    double ths = asin(xs/r);
    double tht = asin(xt/r);
    double s = r*r * ( (tht / 2 + sin(2*tht) / 4) - (ths / 2 + sin(2*ths) / 4) );
    return s - y0 * (xt-xs);
}

double integrate(double nx, double ny, double w, double r) {
    if (!(nx < ny))
        swap(nx, ny);
    P lb(nx, ny), rt(nx+w, ny+w), lt(nx, ny+w), rb(nx+w, ny);
    if (abs(rt) <= r-EPS)
        return w*w;
    if (abs(lt) <= r-EPS) {
        double y = ny + w;
        double x = sqrt(r*r-y*y);
        return integrate0(r, x, nx+w, ny) + (x-nx)*w;
    }
    if (abs(rb) <= r-EPS) {
        return integrate0(r, nx, nx+w, ny);
    }
    if (abs(lb) <= r-EPS) {
        double y = ny;
        double x = sqrt(r*r-y*y);
        return integrate0(r, nx, x, ny);
    }
    return 0;
}

void solve() {

    double f, R, t, r, g;
    cin >> f >> R >> t >> r >> g;

    double res = 0;

    if (f*2 < g - EPS && R-t-f > 0 + EPS) {
        double w = g - 2*f;
        for(int i = 0; ; i++) {
            double nx = (2*r + g) * i + r + f;
            if (nx > R)
                break;
            for(int j = 0; ; j++) {
                double ny = (2*r + g) * j + r + f;
                if (ny > R)
                    break;
                double s = integrate(nx, ny, w, R-t-f);
                res += s;
            }
        }
    }

    printf("%.6f\n", (PI * R * R - (res * 4)) / (PI * R * R));
}


int main() {

    int nCases;
    cin >> nCases >> ws;

    REP(iCase, nCases) {

        cout << "Case #" << iCase+1 << ": ";
        solve();

    }

    return 0;
}
