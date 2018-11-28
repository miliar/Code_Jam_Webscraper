#include <iostream>
using namespace std;
const long maxN = 1000 + 10;

long long r, kk, n;
long long queue[maxN], nu[maxN], ttt[maxN], hh, tt;
long long hash[maxN];

int main(void)
{
              freopen("c2.in", "r", stdin);
              freopen("c3.out", "w", stdout);
        long long T, ans;
        cin >> T;
        for (long i = 1; i <= T; i++) {
                ans = 0;
                cin >> r >> kk >> n;
                memset(hash, -1, sizeof(hash));
                for (long j = 0; j < n; j++) {
                        cin >> queue[j];
                        nu[j] = j;
                }
                hash[0] = 0;
                ttt[0] = 0;
                tt = 0;
                hh = n - 1;
                for (long j = 1; j <= r; j++) {
                        long long cnt = 0;
                        long long stop = hh;
                        while (tt != (stop + 1) % maxN) {
                                if (cnt + queue[tt] <= kk) {
                                        ans += queue[tt];
                                        cnt += queue[tt];
                                        hh = (hh + 1) % maxN;
                                        queue[hh] = queue[tt];
                                        nu[hh] = nu[tt];
                                        tt = (tt + 1) % maxN;
                                } else
                                        break;
                        }
                        if (hash[nu[tt]] >= 0) {
                               ans += (long long)((r - j) / (j - hash[nu[tt]])) * (ans - ttt[nu[tt]]);
                               j = r - (r - j) % (j - hash[nu[tt]]);
                        } else {
                                hash[nu[tt]] = j;
                                ttt[nu[tt]] = ans;
                        }
                }
                cout << "Case #" << i << ": " << ans << endl;
        }
        return 0;
}
