#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
using namespace std;
#define SZ(v) ((int)(v).size())
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define repf(i, a, b) for (int i = (a); i <= (b); ++i)
#define repd(i, a, b) for (int i = (a); i >= (b); --i)
const int maxint = -1u>>1;
typedef long long lint;
const int maxn = 10000 + 4;

int n;
int d[maxn], l[maxn], rec[maxn];
int dest;

int main() {
    freopen("a.out", "w", stdout);
    int ca = 0, t;
    scanf("%d", &t);
    while (scanf("%d", &n) == 1) {
        printf("Case #%d: ", ++ca);
        for (int i = 0; i < n; ++i) {
            scanf("%d%d", &d[i], &l[i]);
        }
        scanf("%d", &dest);
        int now1 = 0, now2 = 1;
        rec[0] = d[0];
        lint mx = 0;
        while (now1 < now2) {
            mx = max(mx, (lint)d[now1] + min(rec[now1], l[now1]));
            while (now2 < n && d[now2] <= (lint)d[now1] + min(rec[now1], l[now1])) {
                rec[now2] = d[now2] - d[now1];
                ++now2;
            }
            ++now1;
        }
        if (mx >= dest) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}

