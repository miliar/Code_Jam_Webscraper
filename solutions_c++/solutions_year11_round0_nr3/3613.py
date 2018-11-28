#include <iostream>
using namespace std;

int tcase, n, sum, small, x, xo;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &tcase);
    for (int k = 1; k <= tcase; ++k) {
        scanf("%d", &n);
        sum = xo = 0, small = 1000000 + 10;
        for (int i = 1; i <= n; ++i) {
            scanf("%d", &x);
            sum += x, xo ^= x;
            small = min(small, x);
        }
        if (xo == 0) printf("Case #%d: %d\n", k, sum - small);
        else printf("Case #%d: NO\n", k);
    }
    return 0;
}

