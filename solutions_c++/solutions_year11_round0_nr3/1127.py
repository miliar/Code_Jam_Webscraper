#include <iostream>
#include <cstdio>
#include <cstring>

#define MAX 1010
#define INF 1000000000

using namespace std;

int val[MAX];

int main() {
    int t, cnt = 1, n, i, sum, sxor, m;

//    freopen("C-large.in", "r", stdin);
//    freopen("C-large.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        m = INF;
        sum = sxor = 0;
        for (i = 0; i < n; i++) {
            scanf("%d", &val[i]);
            sum += val[i];
            sxor ^= val[i];
            m = min(m, val[i]);
        }

        if (sxor) printf("Case #%d: NO\n", cnt++);
        else printf("Case #%d: %d\n", cnt++, sum - m);
    }

    return 0;
}
