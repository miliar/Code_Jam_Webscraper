#include <iostream>
using namespace std;
const long maxn = 1000 + 10;

long n, a[maxn], b[maxn];

int main(void)
{
              freopen("a.in", "r", stdin);
              freopen("a.out", "w", stdout);
        long T;
        cin >> T;
        for (long loop = 1; loop <= T; loop++) {
                cin >> n;
                for (long i = 1; i <= n; i++)
                        cin >> a[i] >> b[i];
                for (long i = 1; i < n; i++)
                        for (long j = 1; j < n; j++)
                                if (a[j] > a[j + 1]) {
                                        swap(a[j], a[j + 1]);
                                        swap(b[j], b[j + 1]);
                                }
                
                long ans = 0;
                for (long i = 1; i <= n; i++)
                        for (long j = i + 1; j <= n; j++)
                                if (b[j] < b[i])
                                        ++ans;
                cout << "Case #" << loop << ": " << ans << endl;
        }
        return 0;
}
