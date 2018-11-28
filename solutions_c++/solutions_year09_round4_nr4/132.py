#define _CRT_SECURE_NO_DEPRECATE
#pragma warning(disable:4530)
#include <string>
#include <vector>
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <set>
#include <cmath>
#include <map>
#include <cassert>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(it,x) for(typeof((x).begin())it=(x).begin();it!=(x).end();++it)
#define all(x) (x).begin(),(x).end()
#define CLR(x,v) memset(x,v,sizeof(x))
#define pb push_back
#define sz size()
#define exist(c,x) ((c).find(x)!=(c).end())
#define cexist(c,x) (find(all(c),x)!=(c).end())
#define SMIN(a, b) a = min((a),(b))
#define SMAX(a, b) a = max((a),(b))

#define S(x) ((x)*(x))

typedef long long ll;

/*
bool circumcenter(
    double ax, double ay,
    double bx, double by,
    double cx, double cy,
    double &sx, double &sy) {

    double D = 2 * (ay * cx + by * ax - by * cx - ay * bx - cy * ax + cy * bx);

    if (fabs(D) < 1e-10)  return false;

    sx = (by * S(ax) - cy * S(ax) - S(by) * ay + S(cy) * ay + 
          S(bx) * cy + S(ay) * by + S(cx) * ay - S(cy) * by - 
          S(cx) * by - S(bx) * ay + S(by) * cy - S(ay) * cy) / D;

    sy = (S(ax) * cx + S(ay) * cx + S(bx) * ax - S(bx) * cx +
          S(by) * ax - S(by) * cx - S(ax) * bx - S(ay) * bx - 
          S(cx) * ax + S(cx) * bx - S(cy) * ax + S(cy) * bx) / D;

    return true;
}
*/

double dist(double ax, double ay, double ar, double px, double py) {
    double pd = sqrt(S(ax - px) + S(ay - py));
    
    return ar + pd;

    //if (pd < ar) return ar + pd; else return pd - ar;
    
}

bool bicenter(
    double ax, double ay, double ar,
    double bx, double by, double br,

    double &sx, double &sy
    ) {

    double d = sqrt(S(ax - bx) + S(ay - by));

    if (d < 1e-8) return false;

    double togo = (ar + d + br) / 2.0 - ar;
    double t = togo / d;

    sx = ax * (1.0 - t) + bx * t;
    sy = ay * (1.0 - t) + by * t;

    return true;

}
int main(int argc, char *argv[]) {
    double sx, sy;


    freopen(argv[1], "r", stdin);
    int Tests;
    cin >> Tests;
    FOR(test, 1, Tests+1) {
        int n;
        vector<double> x, y, r;
        printf("Case #%d: ", test);
        cin >> n;

        vector< pair<double, double> > cands;

        REP(i, n) {
            double dx, dy, dr;
            cin >>dx >>dy >>dr;
            x.pb(dx);
            y.pb(dy);
            r.pb(dr);

            cands.pb(make_pair(dx, dy) );
        }
        REP(i, n) {
            FOR(j, i+1, n) {
                double sx, sy;
                if (bicenter(
                    x[i], y[i], r[i],
                    x[j], y[j], r[j],
                    sx, sy)) {

                    cands.pb( make_pair(sx, sy) );
                }
            }
        }
        int candno = cands.sz;
        double result = 1e10;
        REP(i, candno) {
            double px = cands[i].first, py = cands[i].second;
            FOR(j, i, candno) {
                double qx = cands[j].first, qy = cands[j].second;

                double max_d = 0.0;
                REP(k, n) {
                    double d1 = dist(x[k], y[k], r[k], px, py);
                    double d2 = dist(x[k], y[k], r[k], qx, qy);

                    max_d = max(max_d, min(d1, d2));
                }

                result = min(result, max_d);
            }
        }
        printf("%.7lf\n", result);
    }
    return 0;

}
