#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int len[300], x, s, r, t, n;

int main() {
    int tot_t;
    scanf("%d", &tot_t);
    for (int cur_t = 0; cur_t < tot_t; ++cur_t) {
        scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
        memset(len, 0, sizeof len);
        len[s] = x;
        for (int i = 0; i < n; ++i) {
            int b, e, w;
            scanf("%d%d%d", &b, &e, &w);
            len[w + s] += e - b;
            len[s] -= e - b;
        }

        double available = t, ans = 0;
        for (int v = 1; v < 300; ++v) {
            double t1 = (double)len[v] / (v + r - s);
            if (t1 <= available) {
                available -= t1;
                ans += t1;
            } else {
                double dist = available * (v + r - s);
                ans += available + (double)(len[v] - dist) / v;
                available = 0;
            }
        }
        printf("Case #%d: %.15f\n", cur_t + 1, ans);
    }
    return 0;
}

