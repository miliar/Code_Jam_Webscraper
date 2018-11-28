#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

const int maxN = 300;
const double inf = (long long) 1000 * 1000 * 1000 * 1000 * 1000 * 1000, eps = 0.001 * 0.001 * 0.001 * 0.001;
int n, h, i, t;
double d, l, r, m, x[maxN], cnt[maxN];
pair<double, double> a[maxN];

bool pr(double t) {
    double l = -inf;
    int i, j;
    for (i = 1; i <= n; ++i) {
        for (j = 1; j <= cnt[i]; ++j)
            if (l - x[i] + d <= t) {
                if (l < x[i]) l = max(l + d, x[i] - t);
                else l += d;
            } else return false;
    }
    return true;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> t;
    for (h = 1; h <= t; ++h) {
        cin >> n >> d;
        for (i = 1; i <= n; ++i)
            cin >> a[i].first >> a[i].second;
        sort(a + 1, a + n + 1);
        for (i = 1; i <= n; ++i) {
            x[i] = a[i].first;
            cnt[i] = a[i].second;
        }
        l = 0;
        r = inf;
        while((r - l) > eps) {
            m = (r + l) / 2;
            if (pr(m)) r = m;
            else l = m;
        }
        printf("Case #%d: %.7f\n", h, l);
    }

    return 0;
}
