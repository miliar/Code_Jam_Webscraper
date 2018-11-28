#include <iostream>
using namespace std;

const int maxn = 55;

int t2, n, k, b, t, x[maxn];
bool a[maxn];

int main()
{
    freopen("b2.in", "r", stdin);
    freopen("b2.out", "w", stdout);

    cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        cin >> n >> k >> b >> t;
        for (int i = 1; i <= n; ++i)
            cin >> x[i];
        for (int i = 1; i <= n; ++i) {
            int v; cin >> v;
            a[i] = v * t >= b - x[i];
        }
        printf("Case #%d: ", t1);
        int ret = 0;
        for (int i = n, j = 0; k && i; --i)
            if (a[i]) --k, ret += j;
            else ++j;
        if (k) printf("IMPOSSIBLE\n");
        else printf("%d\n", ret);
    }

    return 0;
}
