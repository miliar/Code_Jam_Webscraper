#include <vector>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
using namespace std;

#define N 1005
#define C 1000
#define eps 1e-8

const int ix[4] = {0, -1, 0, 1};
const int iy[4] = {-1, 0, 1, 0};
const double pi = acos(-1.0);

int n, w, h;
int r[N];
double x[N], y[N];

inline double sqr(double x) {
    return x * x;
}

bool ok(double nx, double ny, int k) {
    if (nx < eps || nx >= w - eps || ny < eps || ny >= h - eps) return false;
    for (int i = 0; i < k; ++i)
        if (sqrt(sqr(nx - x[i]) + sqr(ny - y[i])) < r[i] + r[k] + 0.8)
            return false;
    return true;
}

void cal(int k) {
    double alpha = 0, d = pi * 2 / C;
    for (int j = k - 1; j >= 0; --j) {
        double dis = r[j] + r[k] + 1;
        for (int i = 0; i < C; ++i, alpha += d) {
            double tx = x[j] + dis * cos(alpha);
            double ty = y[j] + dis * sin(alpha);
            if (ok(tx, ty, k)) {
                x[k] = tx;
                y[k] = ty;
                return;
            }
        }
    }
    while (1) {
        int g = k + 1;
    }
}

int main() {
    int t, cas = 0;
    scanf("%d", &t);
    while (t--) {
        scanf("%d %d %d", &n, &w, &h);
        for (int i = 0; i < n; ++i)
            scanf("%d", &r[i]);
        x[0] = y[0] = 0;
        for (int i = 1; i < n; ++i)
            cal(i);
        printf("Case #%d:", ++cas);
        for (int i = 0; i < n; ++i)
            printf(" %.10f %.10f", x[i], y[i]);
        puts("");
    }
    return 0;
}
