#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int x, n;
int s, r;
double t;

int b[1005];
int e[1005];
int w[1005];

int nxt;
long long d[2005];
long long v[2005];
long long v2[2005];

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int tests;
    scanf("%d", &tests);
    for (int testId = 1; testId <= tests; ++testId) {
        scanf("%d%d%d%lf%d", &x, &s, &r, &t, &n);
        for (int i = 0; i < n; ++i)
            scanf("%d%d%d", &b[i], &e[i], &w[i]);
        for (int i = 0; i < n; ++i)
            for (int j = i + 1; j < n; ++j)
                if (b[i] > b[j]) {
                    swap(b[i], b[j]);
                    swap(e[i], e[j]);
                    swap(w[i], w[j]);
                }
        nxt = 0;
        d[nxt] = b[0];
        v[nxt] = s;
        v2[nxt] = r;
        ++nxt;
        for (int i = 1; i < n; ++i) {
            d[nxt] = b[i] - e[i - 1];
            v[nxt] = s;
            v2[nxt] = r;
            ++nxt;
        }
        d[nxt] = x - e[n - 1];
        v[nxt] = s;
        v2[nxt] = r;
        ++nxt;
        for (int i = 0; i < n; ++i) {
            d[nxt] = e[i] - b[i];
            v[nxt] = w[i] + s;
            v2[nxt] = w[i] + r;
            ++nxt;
        }
        for (int i = 0; i < nxt; ++i)
            for (int j = i + 1; j < nxt; ++j)
                if ((v2[i] - v[i]) * (v[j] * v2[j]) < (v2[j] - v[j]) * (v[i] * v2[i])) {
                    swap(v[i], v[j]);
                    swap(d[i], d[j]);
                    swap(v2[i], v2[j]);
                }
        double res = 0;
        for (int i = 0; i < nxt; ++i) {
            if (t < 1e-6) {
                res += d[i] / double(v[i]);
                continue;
            }
            if (d[i] == 0) continue;
            if (d[i] + 1e-6 > v2[i] * t) {
                res += t;
                res += (d[i] - v2[i] * t) / double(v[i]);
                t = 0;
            } else {
                res += d[i] / double(v2[i]);
                t -= d[i] / double(v2[i]);
            }
        }
        printf("Case #%d: %.9lf\n", testId, res);
    }
    return 0;
}
