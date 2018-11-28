#include <iostream>
#include <stdio.h>

using namespace std;

int t, n, res, k;
int in[20];

int main() {
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);
    scanf("%d", &t);
    for (int cas = 1; cas <= t; cas++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) scanf("%d", &in[i]);
        res = 0;
        k = 1 << n;
        for (int i = 1; i < k - 1; i++) {
            int a = 0, b = 0, sres = 0;
            for (int j = 0; j < n; j++) {
                if ((i >> j) & 1) {
                    a ^= in[j];
                    sres += in[j];
                } else {
                    b ^= in[j];
                }
            }
            if (a == b) res = max(res, sres);
        }
        if (res == 0) printf("Case #%d: NO\n", cas);
        else printf("Case #%d: %d\n", cas, res);
    }
    return 0;
}