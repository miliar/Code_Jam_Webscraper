#include <iostream>
using namespace std;

long l, p, c;

int main(void)
{
        freopen("b.in", "r", stdin);
        freopen("b.out", "w", stdout);
        long T;
        cin >> T;
        for (long loop = 1; loop <= T; loop++) {
                cin >> l >> p >> c;
                for (long ans = 0, i = 1; ; i += i, ans++) {
                        long long k = 1;
                        for (long j = 0; j < i; j++)
                                k *= c;
                        if (l * k >= p) {
                                cout << "Case #" << loop << ": " << ans << endl;
                                break;
                        }
                }
        }
        return 0;
}
