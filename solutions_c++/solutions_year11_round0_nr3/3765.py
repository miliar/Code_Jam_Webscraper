#include <stdio.h>
#include <stdlib.h>
int n, a[10000];

int main() {
    FILE *ff = fopen("C-large.in", "r");
    FILE *gg = fopen("resenje.txt", "w");
    int t;
    fscanf(ff, "%d", &t);
    for (int tt = 1; tt <= t; tt++) {
        fscanf(ff, "%d", &n);
        for (int i = 1; i <= n; i++) fscanf(ff, "%d", &a[i]);
        int res = a[1];
        for (int i = 2; i <= n; i++) res = res^a[i];
        if (res == 0) {
            int sum = 0, min = 11111111;
            for (int i = 1; i <= n; i++) {
                if (min > a[i]) min = a[i];
                sum += a[i];
            }
            sum -= min;
            fprintf(gg, "Case #%d: %d\n", tt, sum);
        }
        else fprintf(gg, "Case #%d: NO\n", tt);
    }
}

