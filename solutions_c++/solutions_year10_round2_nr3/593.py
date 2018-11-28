#include <iostream>
#include <cstring>
using namespace std;
const long maxn = 25 + 5;

long n, ans;
bool p[maxn];
long cnt[maxn];

bool check(void)
{
        memset(cnt, 0, sizeof(cnt));
        for (long i = 2; i <= n; i++)
                cnt[i] = cnt[i - 1] + int(p[i]);

        long s = n;
        while (s != 1 && s != 0) {
                if (p[s])
                        s = cnt[s];
                else
                        return false;
        }
        if (s == 0)
                return false;
        return true;
}

void dfs(long k)
{
        if (k == n) {
                p[k] = true;
                if (check())
                        ans = (ans + 1) % 100003;
                return;
        }
        p[k] = true;
        dfs(k + 1);
        p[k] = false;
        dfs(k + 1);
}

int main(void)
{
              freopen("c.in", "r", stdin);
              freopen("c.out", "w", stdout);
        long T;
        cin >> T;
        for (long loop = 1; loop <= T; loop++) {
                cin >> n;
                ans = 0;
                dfs(2);
                cout << "Case #" << loop << ": " << ans << endl;
        }
        return 0;
}
