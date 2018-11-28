#include <iostream>
#include <stdio.h>

using namespace std;

int t, n, k, op, bp, ol, bl;
char w[3];

int main() {
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);
    scanf("%d", &t);
    for (int cas = 1; cas <= t; cas++) {
        scanf("%d", &n);
        op = bp = 1; 
        ol = bl = 0;
        for (int i = 0; i < n; i++) {
            scanf("%s", w);
            if (w[0] == 'O') {
                scanf("%d", &k);
                ol = max(bl, ol + abs(op - k)) + 1;
                op = k;
            }
            if (w[0] == 'B') {
                scanf("%d", &k);
                bl = max(ol, bl + abs(bp - k)) + 1;
                bp = k;
            }
        }
        printf("Case #%d: %d\n", cas, max(ol, bl));
    }
    return 0;
}