#include <iostream>
#include <string>
using namespace std;
const long maxn = 32 + 5;

long m, n;
int p[maxn][maxn];
long ans[maxn];

long getnum(char x)
{
        if ('0' <= x && x <= '9')
                return long(x - '0');
        return 10 + long(x - 'A');
}

bool check(long x, long y, long ll)
{
        if (x + ll > m + 1 || y + ll > n + 1)
                return false;
        for (long i = x; i < x + ll; i++)
                for (long j = y; j < y + ll; j++) {
                        if (p[i][j] < 0)
                                return false;
                        if (i > x && p[i - 1][j] == p[i][j])
                                return false;
                        if (j > y && p[i][j - 1] == p[i][j])
                                return false;
                }
        return true;
}

int main(void)
{
              freopen("c.in", "r", stdin);
              freopen("c.out", "w", stdout);
        long T;
        cin >> T;
        for (long loop = 1; loop <= T; loop++) {
                cin >> m >> n;
                for (long i = 1; i <= m; i++) {
                        string s;
                        cin >> s;
                        for (long j = 0; j < n / 4; j++) {
                                long k = getnum(s[j]);
                                for (long t = 4; t >= 1; t--) {
                                        p[i][j * 4 + t] = k % 2;
                                        k /= 2;
                                }
                        }
                }

                long total = 0;
                for (long i = min(n, m); i >= 1; i--) {
                        ans[i] = 0;
                        for (long x = 1; x <= m; x++)
                                for (long y = 1; y <= n; y++)
                                        if (check(x, y, i)) {
                                                ++ans[i];
                                                for (long u = x; u < x + i; u++)
                                                        for (long v = y; v < y + i; v++)
                                                                p[u][v] = -1;
                                        }
                        if (ans[i])
                                ++total;
                }
                cout << "Case #" << loop << ": " << total << endl;
                for (long i = min(n, m); i >= 1; i--)
                        if (ans[i])
                                cout << i << ' ' << ans[i] << endl;
        }
}
