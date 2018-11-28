#include <cstdio>
#include <algorithm>
using namespace std;

int T, n;
long long a[1000], b[1000], ans;

int main() {
        scanf("%d", &T);
        for (int r = 1; r <= T; ++r) {
                printf("Case #%d: ", r);
                scanf("%d", &n);
                for (int i = 0; i < n; ++i)
                        scanf("%lld", a + i);
                for (int i = 0; i < n; ++i)
                        scanf("%lld", b + i);
                sort(a, a + n);
                sort(b, b + n);
                ans = 0;
                for (int i = 0; i < n; ++i)
                        ans += a[i]*b[n - i - 1];
                printf("%lld\n", ans);
        }
        return 0;
}
