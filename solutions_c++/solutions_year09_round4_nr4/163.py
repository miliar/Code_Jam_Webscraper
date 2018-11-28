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
typedef pair<double, int> PI;
template <class T> void zlepsi(T &a, T b)
{
    a = max(a, b);
}
vector<double> x(100), y(100), r(100);
int n;
const double pi = acos(0.0) * 2;
bool ok(double m)
{
    if (n < 3) return true;
    REP(j,n) REP(i,j)
    {
        double d = hypot(x[i] - x[j], y[i] - y[j]);
        if (r[i] + r[j] + d <= 2 * m)
            return true;
    }
    return false;
}
int main() {
    int tt; scanf("%d", &tt);
    REP(sd,tt)
    {
        scanf("%d", &n);
        REP(i,n) scanf("%lf %lf %lf", &x[i], &y[i], &r[i]);

        double ma = 0, mb = 8000;
        REP(i,n) ma = max(ma, r[i]);
        REP(k,65)
        {
            double m = (ma + mb) / 2;
            if (ok(m)) mb = m;
            else ma = m;
        }

        printf("Case #%d: %.10lf\n", sd+1, ma);
    }
}
