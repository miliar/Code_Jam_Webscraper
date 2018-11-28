#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <queue>
#include <bitset>
#include <utility>
#include <list>
#include <numeric>

#include <cstdio>
#include <cmath>
#include <cctype>
using namespace std;

#define REP(i,n) for(__typeof(n) i=0; i<(n); ++i)
#define FOR(i,a,b) for(__typeof(b) i=a; i<(b); ++i)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

typedef long long ll;
typedef pair<int, int> PI;
double sqr(double a)
{
    return a * a;
}
double f, R, t, r, g;
const double pi = acos(0.0) * 2;
double vs(double x1, double y1, double x2, double y2)
{
    return abs(x1 * y2 - x2 * y1);
}
double area(double x, double y, double q)
{
    if (hypot(x, y) >= q) return 0;
    double a1 = asin(y / q), a2 = acos(x / q);
    double res = (a2 - a1) * q * q
        - vs(x, y, x, sqrt(q * q - x * x))
        - vs(x, y, sqrt(q * q - y * y), y);
//    cout << x << " " << y << " " << q << ": " << res / 2 << " -- " << a2 << " " << a1 << endl;
    return res / 2;
}
double zrataj(double x, double y, double q)
{
    return area(x, y, q) - area(x + g - 2 * f, y, q) - area(x, y + g - 2 * f, q);
}
int main() {
    int n; scanf("%d", &n);
    REP(sd,n)
    {
        double eps = 1e-9;
        scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
        double spolu = sqr(R) * pi / 4, plocha = 0;
        double sir = g + 2 * r;
        int poc = int((R - t) / sir + 4);
        if (g >= 2 * f) REP(i,poc) REP(j,poc)
        {
            if (hypot(i * sir + r + g - f, j * sir + r + g - f) < R - t - f + eps)
                plocha += sqr(g - 2 * f);
            else plocha += zrataj(i * sir + r + f, j * sir + r + f, R - t - f);
        }
//		cout << plocha << " " << spolu << endl;
        cout.setf(ios::fixed, ios::floatfield);
        cout.precision(6);
        cout << "Case #" << sd + 1 << ": " << 1 - plocha / spolu << endl;
    }
}
