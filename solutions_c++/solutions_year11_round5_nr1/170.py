#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <vector>
#include <cstdio>
#include <deque>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <map>
#include <set>

using namespace std;

int w, l, u, g;
vector<pair<double, double> > up;
vector<pair<double, double> > down;

double f(pair<double, double> p1, pair<double, double> p2) {
    return (p1.second + p2.second) / 2.0 * (p2.first - p1.first);
}

pair<double, double> calc(pair<double, double> p1, pair<double, double> p2, double x) {
    double k = (p1.second - p2.second) / (p1.first - p2.first);
    double n = p1.second - k * p1.first;
    return make_pair(x, x * k + n);
}

int main() {
//    freopen("A-small.in", "r", stdin); freopen("A-small.out", "w", stdout);
    freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
    int tests; scanf("%d", &tests);
    for (int testId = 1; testId <= tests; ++testId) {
        printf("Case #%d:\n", testId);
        scanf("%d%d%d%d", &w, &l, &u, &g);
        down.clear();
        up.clear();
        for (int i = 0; i < l; ++i) {
            int x, y; scanf("%d %d", &x, &y);
            down.push_back(make_pair(x, y));
        }
        for (int i = 0; i < u; ++i) {
            int x, y; scanf("%d %d", &x, &y);
            up.push_back(make_pair(x, y));
        }
        double P = 0.0;
        for (int i = 0; i < l - 1; ++i)
            P += f(down[i], down[i + 1]);
        for (int i = 0; i < u - 1; ++i)
            P -= f(up[i], up[i + 1]);
        if (P < 0) P = -P;
        for (int i = 1; i < g; ++i) {
            double low = 0;
            double high = w;
            double need = P / double(g) * double(i);
            while (high - low > 1e-8) {
                double mid = (low + high) / 2;
                double nP = 0.0;
                for (int i = 1; i < l; ++i) {
                    if (down[i].first - mid > 0) {
                        nP += f(down[i - 1], calc(down[i - 1], down[i], mid));
                        break;
                    }
                    nP += f(down[i - 1], down[i]);
                }
                for (int i = 1; i < u; ++i) {
                    if (up[i].first - mid > 0) {
                        nP -= f(up[i - 1], calc(up[i - 1], up[i], mid));
                        break;
                    }
                    nP -= f(up[i - 1], up[i]);
                }
                if (nP < 0) nP = -nP;
                if (nP < need) low = mid;
                else high = mid;
            }
            printf("%.6lf\n", low);
        }
    }
    return 0;
}
