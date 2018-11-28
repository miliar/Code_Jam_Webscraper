#include <vector>
#include <cmath>
#include <fstream>
#include <iomanip>
using namespace std;

#define pb push_back
#define mp make_pair

ifstream in("C.in");
ofstream out("C.out");

inline bool inside(const double &R, const double &x, const double &y) {
    return x * x + y * y <= R * R;
}

inline double intersection(const double &R, const double &x, const double &y, const double &l) {
    if(inside(R, x + l, y + l))
        return l * l;

    vector < pair <double, double> > P;
    pair <double, double> C1, C2;
    if(inside(R, x, y + l))
        if(inside(R, x + l, y)) {
            P.pb(mp(x, y + l));
            P.pb(mp(x, y));
            P.pb(mp(x + l, y));
            C1 = mp(x + l, sqrt(R * R - (x + l) * (x + l)));
            P.pb(C1);
            C2 = mp(sqrt(R * R - (y + l) * (y + l)), y + l);
            P.pb(C2);
        }
        else {
            P.pb(mp(x, y + l));
            P.pb(mp(x, y));
            C1 = mp(sqrt(R * R - y * y), y);
            P.pb(C1);
            C2 = mp(sqrt(R * R - (y + l) * (y + l)), y + l);
            P.pb(C2);
        }
    else
        if(inside(R, x + l, y)) {
            P.pb(mp(x, y));
            P.pb(mp(x + l, y));
            C1 = mp(x + l, sqrt(R * R - (x + l) * (x + l)));
            P.pb(C1);
            C2 = mp(x, sqrt(R * R - x * x));
            P.pb(C2);
        }
        else {
            P.pb(mp(x, y));
            C1 = mp(sqrt(R * R - y * y), y);
            P.pb(C1);
            C2 = mp(x, sqrt(R * R - x * x));
            P.pb(C2);
        }

    double area = 0.;
    for(size_t i = 0; i + 1 < P.size(); ++i) {
        area += P[i].first * P[i + 1].second - P[i + 1].first * P[i].second;
    }
    area += P.back().first * P[0].second - P[0].first * P.back().second;
    area = fabs(area) / 2.;

    double a = sqrt((C1.first - C2.first) * (C1.first - C2.first) + (C1.second - C2.second) * (C1.second - C2.second));
    double b = sqrt(C1.first * C1.first + C1.second * C1.second);
    double c = sqrt(C2.first * C2.first + C2.second * C2.second);
    double alfa = acos((b * b + c * c - a * a) / (2. * b * c));

    area += (R * R / 2. * alfa) - (b * c * sin(alfa) / 2.);

    return area;
}

double solve(double f, double R, double t, double r, double g) {
    double R_ini = R, l;
    R -= t;
    R -= f;
    if(R <= 0.)
        return 1.;

    l = g - 2. * f;
    if(l <= 0.)
        return 1.;

    double area = 0.;
    for(double x = r + f; x < R; x += g + 2. * r)
        for(double y = r + f; x * x + y * y < R * R; y += g + 2. * r)
            area += intersection(R, x, y, l);

    return 1. - (4. * area) / (M_PI * R_ini * R_ini);
}


int main() {
    int T;
    double f, R, t, r, g;
    in >> T;
    out << fixed << setprecision(6);
    for(int i = 1; i <= T; ++i) {
        in >> f >> R >> t >> r >> g;
        out << "Case #" << i << ": " << solve(f, R, t, r, g);
        if(i < T)
            out << "\n";
    }
    return 0;
}
