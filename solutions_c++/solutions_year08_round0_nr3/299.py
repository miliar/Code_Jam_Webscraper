#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iomanip>
using namespace std;

#define ALL(a) (a).begin(), (a).end()
#define PB push_back
#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); (i)++)
#define FORD(i, a, b) for(int (i) = (a); (i) >= (b); (i)--)
#define REP(i, n) for (int (i) = 0; (i) < n; (i)++)
#define SIZE(a) (int)(a).size()
#define DBG(x) cout << #x << " = " << (x) << endl
#define DBGARR(x, n) REP(i, n) cout << #x << '[' << i << "] = " << x[i] << endl
#define DBGTBL(x, a, b) REP(i, a) REP(j, b) cout << #x << '[' << i << "][" << j << "] = " << x[i][j] << endl

#define PI 3.14159265358979
#define EPS 1e-8

#define FIN "test.in"
#define FOUT "test.out"

double f, R, t, r, g;

double pif(double x, double y) {
    return sqrt(x * x + y * y);
}

double area() {
    if (g < 2*f + EPS) return 0.0;
    double x = r + g / 2;
    double y = x;
    double res = 0.0;
    while (1) {
        //DBG(x); DBG(y);
        double x1 = x - g / 2 + f;
        double y1 = y - g / 2 + f;
        double x2 = x + g / 2 - f;
        double y2 = y + g / 2 - f;
        double Rin = R - t - f;
        if (pif(x2, y2) < Rin + EPS) {
            res += (g - 2 * f) * (g - 2 * f);
            y += g + 2 * r;
        } else if (pif(x1, y1) > Rin - EPS) {
            if (abs(y - r - g/2) < EPS) break;
            y = r + g / 2;
            x += g + 2 * r;
        } else {
            double poly_area = 0.0;
            double segm_area = 0.0;
            if (pif(x1, y2) > Rin - EPS) {
                double yx1 = sqrt(Rin * Rin - x1 * x1);
                if (pif(x2, y1) > Rin - EPS) {
                    double xy1 = sqrt(Rin * Rin - y1 * y1);
                    poly_area = (yx1 - y1) * (xy1 - x1) * 0.5;
                    double cross = (xy1 * yx1 - x1 * y1) / (pif(xy1, y1) * pif(x1, yx1));
                    segm_area = 0.5 * Rin * Rin * (asin(cross) - cross);
                } else {
                    double yx2 = sqrt(Rin * Rin - x2 * x2);
                    poly_area = 0.5 * (g - 2*f) * (yx1 + yx2 - 2 * y1);
                    double cross = (x2 * yx1 - x1 * yx2) / (pif(x2, yx2) * pif(x1, yx1));
                    segm_area = 0.5 * Rin * Rin * (asin(cross) - cross);
                }
            } else {
                double xy2 = sqrt(Rin * Rin - y2 * y2);
                if (pif(x2, y1) > Rin - EPS) {
                    double xy1 = sqrt(Rin * Rin - y1 * y1);
                    poly_area = 0.5 * (g - 2*f) * (xy1 + xy2 - 2 * x1);
                    double cross = (xy1 * y2 - xy2 * y1) / (pif(xy1, y1) * pif(xy2, y2));
                    segm_area = 0.5 * Rin * Rin * (asin(cross) - cross);
                } else {
                    double yx2 = sqrt(Rin * Rin - x2 * x2);
                    poly_area = (g - 2*f) * (g - 2*f) - 0.5 * (y2 - yx2) * (x2 - xy2);
                    double cross = (x2 * y2 - xy2 * yx2) / (pif(x2, yx2) * pif(xy2, y2));
                    segm_area = 0.5 * Rin * Rin * (asin(cross) - cross);
                }
            }
            res += poly_area + segm_area;
            y += g + 2 * r;
        }
    }
    return res;
}

int main()
{
    freopen(FIN, "r", stdin);
    freopen(FOUT, "w", stdout);

    int tests;
    cin >> tests;
    FOR(ttt, 1, tests) {
        cin >> f >> R >> t >> r >> g;
        double res = 1.0 - 4 * area() / (PI * R * R);
        if (res < EPS) res = 0.0;
        cout << "Case #" << ttt << ": " << fixed << setprecision(10) << res << endl;
    }

    return 0;
}
