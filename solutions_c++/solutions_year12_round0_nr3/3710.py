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
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPF(i, a, b) for (int i = (a); i <= (b); ++i)
#define REPD(i, a, b) for (int i = (a); i >= (b); --i)
const int maxint = -1u>>1;

int mi[8];
int a, b;

int next(int now, int n) {
    int rec = now % 10;
    return now / 10 + rec * mi[n - 1];
}
int getlen(int x) {
    int len = 0;
    while (x) {
        ++len;
        x /= 10;
    }
    return max(1, len);
}
int main() {
    freopen("c.out", "w", stdout);
    mi[0] = 1;
    for (int i = 1; i <= 7; ++i) mi[i] = mi[i - 1] * 10;
    int t, ca = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: ", ++ca);
        scanf("%d%d", &a, &b);
        int n = getlen(a);
        int ans = 0;
        for (int i = a; i <= b; ++i) {
            for (int now = next(i, n); now != i; now = next(now, n)) {
                if (i < now && now <= b) {
                    //printf("%d %d\n", i, now);
                    ++ans;
                }
            }
        }
        printf("%d\n", ans);
    }
    return 0;
}

