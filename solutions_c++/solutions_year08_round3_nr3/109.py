#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long ll;
int n, m;
ll x,y,z;
ll a[1005];
ll b[1005];
ll res[1005];
int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int T, cnt = 0;
    scanf("%d", &T);
    while (T--) {
           scanf("%d%d%lld%lld%lld", &n, &m, &x, &y, &z);
           for (int i = 0; i < m; i++)
                scanf("%lld", &a[i]);
           int t = 0;
           for (int i = 0; i < n; i++) {
                b[t++] = a[i%m];
                a[i % m] = (x * a[i % m] + y * (i + 1)) % z;
           }
           for (int i = 0; i < n; i++) {
                res[i] = 1;
                for (int j = 0; j < i; j++) {
                     if (b[i] > b[j]) {
                         res[i] += res[j];
                         res[i] %= (1000000007ll);
                     }
                }
           }
           ll ans = 0;
           for (int i = 0; i < n; i++) {
                ans += res[i];
                ans %= (1000000007ll);
           }
           printf("Case #%d: %lld\n", ++cnt, ans);
    }
}
