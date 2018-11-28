#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main() {
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int t, tt, i, a[1001];
    scanf("%d", &t);
    for (tt = 1; tt <= t; tt++) {
        int n;
        scanf("%d", &n);
        int tmp = 0;
        for (i = 1; i <= n; i++) {
            scanf("%d", &a[i]);
            if (a[i] == i) tmp++;
        }
        double sum = 0;
        sum = n - tmp;
        printf("Case #%d: %lf\n", tt, sum);
    }
    return 0;
}
