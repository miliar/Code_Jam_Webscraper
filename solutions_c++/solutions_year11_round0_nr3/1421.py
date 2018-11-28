#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t--) {
        int n;
        int sum = 0, mn = 0x7fffffff, s = 0;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            int x;
            scanf("%d", &x);
            sum += x;
            mn = min(mn, x);
            s ^= x;
        }
        if (s == 0)
            printf("Case #%d: %d\n", ++cas, sum - mn);
        else
            printf("Case #%d: NO\n", ++cas);
    }
    return 0;
}
