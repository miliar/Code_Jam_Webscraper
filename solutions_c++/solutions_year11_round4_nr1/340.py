#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

int len, s, r, n;
double tt;
int aa[1001], bb[1001], ss[1001];
struct node {
    int a, b, s;
    node() {}
    node(int x, int y, int w) : a(x), b(y), s(w) {}
    bool operator < (const node &w) const {
        return s < w.s;
    }
};
node dd[10000];
int dn;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%d%d%d%lf%d", &len, &s, &r, &tt, &n);
        dn = 0;
        for (int i = 0; i < n; ++i) {
            scanf("%d%d%d", &aa[i], &bb[i], &ss[i]);
        }
        dd[dn++] = node(0, aa[0], 0);
        dd[dn++] = node(aa[0], bb[0], ss[0]);
        for (int i = 1; i < n; ++i) {
            dd[dn++] = node(bb[i - 1], aa[i], 0);
            dd[dn++] = node(aa[i], bb[i], ss[i]);
        }
        dd[dn++] = node(bb[n - 1], len, 0);
        sort(dd, dd + dn);
        double ans = 0;
        for (int i = 0; i < dn; ++i) {
            double t = min(tt, double(dd[i].b - dd[i].a) / (dd[i].s + r));
            ans += t;
            ans += double(dd[i].b - dd[i].a - t * (dd[i].s + r)) / (s + dd[i].s);
            tt -= t;
        }
        printf("Case #%d: %lf\n", ca, ans);
    }
    return 0;
}
