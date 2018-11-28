#include <iostream>
using namespace std;

const int maxn = 1005;

long long a[maxn], v1[maxn], v2[maxn], r, k, n, ret, s;

int main()
{
    freopen("c2.in", "r", stdin);
    freopen("c2.out", "w", stdout);

    int t1;
    cin >> t1;
    for (int t2 = 1; t2 <= t1; ++t2) {
        cin >> r >> k >> n;
        ret = s = 0;
        for (int i = 1; i <= n; ++i) {
            cin >> a[i]; s += a[i];
        }
        if (k >= s) ret = s * r;
        else {
            long long i = 1;
            memset(v1, 0, sizeof(v1));
            while (r--) {
                v1[i] = r + 1; v2[i] = ret;
                long long s2 = 0, j = i;
                while ((s2 += a[j]) <= k)
                    if (++j > n) j = 1;
                ret += s2 - a[j];
                if (v1[j]) {
                    ret += r / (v1[j] - r) * (ret - v2[j]);
                    r %= v1[j] - r;
                    memset(v1, 0, sizeof(v1));
                }
                i = j;
            }
        }
        printf("Case #%d: ", t2);
        cout << ret << endl;
    }

    return 0;
}
