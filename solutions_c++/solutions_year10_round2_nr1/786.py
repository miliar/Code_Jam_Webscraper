#include <iostream>
#include <string>
using namespace std;
const long maxn = 2000 + 10;

string p[maxn], wait[maxn];
long n, m;
long ans;

long solve(long k)
{
        long maxk = 0;
        for (long i = 0; i < n; i++) {
                long j;
                for (j = 0; j < min(p[i].size(), wait[k].size()); j++)
                        if (p[i][j] != wait[k][j])
                                break;
                maxk = max(maxk, j - 1);
        }
        long ret = 0;
        for (long i = maxk + 1; i < wait[k].size(); i++)
                if (wait[k][i] == '/')
                        ++ret;
        return ret;
}

int main(void)
{
              freopen("a.in", "r", stdin);
              freopen("a.out", "w", stdout);
        long T;
        cin >> T;
        for (long loop = 1; loop <= T; loop++) {
                cin >> n >> m;
                ans = 0;
                for (long i = 0; i < n; i++) {
                        cin >> p[i];
                        if (p[i][p[i].size() - 1] != '/')
                                p[i] += string("/");
                }
                for (long i = 0; i < m; i++) {
                        cin >> wait[i];
                        if (wait[i][wait[i].size() - 1] != '/')
                                wait[i] += string("/");
                }

                for (long i = 0; i < m; i++) {
                        ans += solve(i);
                        p[n++] = wait[i];
                }
                cout << "Case #" << loop << ": " << ans << endl;
        }
        return 0;
}
