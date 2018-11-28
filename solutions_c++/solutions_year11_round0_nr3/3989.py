#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int n;
int candy[2000];

int main() {
    int tests, cases;
    int i, k, m;
    scanf("%d", &tests);
    for (cases = 1; cases <= tests; ++cases) {
        scanf("%d", &n);
        for (i = 0; i < n; ++i)
            scanf("%d", &candy[i]);
        int res = -1;
        for (int mask = 1; mask < (1 << n) - 1; ++mask) {
            int asum = 0;
            int axor = 0;
            int bxor = 0;
            for (i = 0; i < n; ++i) {
                if (mask & (1 << i)) {
                    asum += candy[i];
                    axor ^= candy[i];
                } else {
                    bxor ^= candy[i];
                }
            }
            if (axor == bxor) {
                res = max(res, asum);
            }
        }
        if (res == -1)
            printf("Case #%d: NO\n", cases);
        else
            printf("Case #%d: %d\n", cases, res);
    }
    return 0;
}
