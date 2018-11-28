#include <iostream>
#include <stdio.h>

using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, pd, pg, tt, i;
    __int64 n;
    scanf("%d", &t);
    for (tt = 1; tt <= t; tt++) {
        scanf("%I64d%d%d", &n, &pd, &pg);
        printf("Case #%d: ", tt);
        bool flag = 0;
        if (n >= 100 || pd == 100) flag = 1;
        for (i = 1; i <= n; i++) {
            if (i == 101) break;
            if (i * pd % 100 == 0) flag = 1;
        }
        if (flag == 0 ||((n * pd / 100 < 1 && pd != 0) ||
             (pd == 100 && pg == 0)||
             (pd < 100 && pg == 100) ||
             (pd > 0 && pg == 0)
            )) printf("Broken\n");
        else printf("Possible\n");
    }
    return 0;
}
