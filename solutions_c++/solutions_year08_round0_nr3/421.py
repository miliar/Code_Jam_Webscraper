#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

namespace tip {
template<class F, class S> ostream& operator<< (ostream& out, const pair<F, S>& p) {
	return out << "<" << p.first << " : " << p.second << ">";
}
template<class T> ostream& operator<< (ostream& out, const vector<T>& v) {
	for (int i = 0; i < static_cast<int>(v.size()); ++i)
		out << (i == 0 ? "(" : ", ") << v[i];
	return out << ")";
}
inline string function() {
	return "";
}
template<class T> inline string function(const T& x) {
	ostringstream oss;
	oss << " = " << x << ", ";
	return oss.str();
}
}

#define TIP_0(x, ...) #x << tip::function(x) << endl
#define TIP_1(x, ...) #x << tip::function(x) << TIP_0(__VA_ARGS__)
#define TIP_2(x, ...) #x << tip::function(x) << TIP_1(__VA_ARGS__)
#define TIP_3(x, ...) #x << tip::function(x) << TIP_2(__VA_ARGS__)
#define TIP_4(x, ...) #x << tip::function(x) << TIP_3(__VA_ARGS__)
#define TIP_5(x, ...) #x << tip::function(x) << TIP_4(__VA_ARGS__)
#define TIP_6(x, ...) #x << tip::function(x) << TIP_5(__VA_ARGS__)
#define TIP_7(x, ...) #x << tip::function(x) << TIP_6(__VA_ARGS__)
#define TIP_8(x, ...) #x << tip::function(x) << TIP_7(__VA_ARGS__)
#define TIP_9(x, ...) #x << tip::function(x) << TIP_8(__VA_ARGS__)
#define TIP(...) (cerr << __LINE__ << ": " << TIP_9(__VA_ARGS__))

#define REP(i, N) for (int i = 0; i < (int)(N); ++i)
#define FOR(i, N, M) for (int i = (int)(N); i <= (int)(M); ++i)
#define ALL(x) (x).begin(), (x).end()
#define CLEAR(X) (memset(X, 0, sizeof(X)))
#define SZ(x) ( (int) x.size() )
#define PB push_back

#define FORD(i, N, M) for (int i = (int)(N); i >= (int)(M); --i)
#define FORI(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define MP make_pair
#define INF 0x3f3f3f3f
typedef long long LL;

#define FILE_NAME "c-small"

const double EPS = 1e-8;

inline bool gt(double x, double y) {
    return x - y >= EPS;
}

inline double dist(double x, double y) {
    return sqrt(x * x + y * y);
}

double rr;
inline double sector(double x, double y, double hx, double hy) {
    double a = y - hy, b = x - hx, c = hy * (hx - x) - x * (y - hy);
    double d = sqrt((hx - x) * (hx - x) + (hy - y) * (hy - y));
    double h = abs(c) / sqrt(a * a + b * b);
    double sinalfa = h * d  / rr / rr;
    TIP(sinalfa);
    return ((hx - x) * (hy - y)  + rr * rr * (asin(sinalfa) - sinalfa)) * 0.5;
}

int main() {
    freopen(FILE_NAME".in", "rt", stdin);
    freopen(FILE_NAME".out", "wt", stdout);
    int nrt, nrc;
    double f, R, t, r, g;

    for (scanf("%d", &nrt), nrc = 1; nrc <= nrt; ++nrc) {
        scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
        double area = 0, x, y;
        rr = R - t - f;
        for (x = r; x <= R; x += g + 2 * r) {
            for (y = r; y <= R; y += g + 2 * r) {
                double jx = x + f, jy = y + f, sx = x + g - f, sy = y + g - f;
                if (gt(jx, sx) || gt(jy, sy)) continue;
                if (gt(dist(jx, jy), rr)) continue;

                if (gt(rr, dist(sx, sy))) {
                    area += (sy - jy) * (sx - jx);
                    continue;
                }

                vector<pair<double, double> > inter;
                double tx, ty;
                tx = sqrt(rr * rr - jy * jy);
                if (gt(tx, jx) && gt(sx, tx)) inter.PB(MP(tx, jy));
                tx = sqrt(rr * rr - sy * sy);
                if (gt(tx, jx) && gt(sx, tx)) inter.PB(MP(tx, sy));
                ty = sqrt(rr * rr - jx * jx);
                if (gt(ty, jy) && gt(sy, ty)) inter.PB(MP(jx, ty));
                ty = sqrt(rr * rr - sx * sx);
                if (gt(ty, jy) && gt(sy, ty)) inter.PB(MP(sx, ty));
                assert(SZ(inter) == 2);

                tx = min(inter[0].first, inter[1].first);
                ty = min(inter[0].second, inter[1].second);
                double mx, my;
                mx = max(inter[0].first, inter[1].first);
                my = max(inter[0].second, inter[1].second);
                area += (tx - jx) * (sy - jy) + (sx - tx) * (ty - jy);
                area += sector(tx, ty, mx, my);
            }
        }
        printf("Case #%d: %lf\n", nrc, 1. - 4 * area / (M_PI * R * R));
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}

