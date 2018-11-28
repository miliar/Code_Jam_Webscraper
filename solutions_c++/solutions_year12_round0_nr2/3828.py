#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int n, s, p, a[150];
int b[150], c[150];
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int icase, i, tt = 0;
    scanf("%d", &icase);
    while (icase--) {
        int res;
        scanf("%d%d%d", &n, &s, &p);
        for (i = 0; i < n; i++) scanf("%d", &a[i]);
        for (i = 0; i < n; i++) {
            if (a[i] % 3 == 0) {
                b[i] = a[i] / 3;
                if (b[i] > 0) c[i] = b[i] + 1;
                else c[i] = b[i];
            } else if (a[i] % 3 == 1) {
                b[i] = a[i] / 3 + 1;
                c[i] = b[i];
            } else {
                b[i] = a[i] / 3 + 1;
                c[i] = b[i] + 1;
            }
        }
        res = 0;
        for (i = 0; i < n; i++) {
            if (b[i] >= p) res++;
            else if (c[i] >= p && s > 0) res++, s--;
        }
        printf("Case #%d: %d\n", ++tt, res);
    }
    return 0;
}
