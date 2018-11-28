#include <iostream>
using namespace std;
const long maxn = 1024 + 10, maxp = 10 + 5;
const long superbig = 2147483647;

long T;
long p, n, gu[maxn], cost[maxn * 2], f[maxn * 2][maxp];

int main(void)
{
              freopen("b.in", "r", stdin);
              freopen("b.out", "w", stdout);
        cin >> T;
        for (long loop = 1; loop <= T; loop++) {
                cin >> p;
                n = (1 << p);
                for (long i = 0; i < n; i++)
                        cin >> gu[i];
                for (long i = p - 1; i >= 0; i--) {
                        long j = (1 << i) - 1, k = (1 << (i + 1)) - 1;
                        while (j < k)
                                cin >> cost[j++];
                }

                for (long i = 0; i < n; i++) {
                        long k = (1 << p) - 1 + i;
                        for (long j = p; j > gu[i]; j--)
                                f[k][j] = superbig;
                        for (long j = gu[i]; j >= 0; j--)
                                f[k][j] = 0;
                }
                long ans = superbig;
                for (long i = n - 2; i >= 0; i--)
                        for (long j = 0; j <= p; j++) {
                                f[i][j] = superbig;
                                long lc = i * 2 + 1, rc = i * 2 + 2;
                                if (j + 1 <= p && f[lc][j + 1] < superbig && f[rc][j + 1] < superbig)
                                        f[i][j] = min(f[i][j], f[lc][j + 1] + f[rc][j + 1]);
                                if (f[lc][j] < superbig && f[rc][j] < superbig)
                                        f[i][j] = min(f[i][j], f[lc][j] + f[rc][j] + cost[i]);
                                if (!i)
                                        ans = min(ans, f[i][j]);
                        }
                cout << "Case #" << loop << ": " << ans << endl;
        }
        return 0;
}
