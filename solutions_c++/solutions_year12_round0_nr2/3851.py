#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int main() {
    freopen("b.in", "r", stdin);

    int tot_test, n, s, p, t[200];
    cin >> tot_test;
    for (int cur_test = 0; cur_test < tot_test; ++cur_test) {
        cin >> n >> s >> p;
        for (int i = 0; i < n; ++i) {
            cin >> t[i];
        }

        static int f[200][200];
        for (int i = 0; i < 200; ++i) {
            for (int j = 0; j < 200; ++j) {
                f[i][j] = -1000000000;
            }
        }
        f[0][0] = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j <= s; ++j) {
                if (f[i][j] < 0) continue;
                f[i + 1][j] = max(f[i + 1][j], f[i][j]);
                if (t[i] >= p + (p - 1) * 2) {
                    f[i + 1][j] = max(f[i + 1][j], f[i][j] + 1);
                }
                if (t[i] >= p + (p - 2) * 2 && t[i] >= 2 && j < s) {
                    f[i + 1][j + 1] = max(f[i + 1][j + 1], f[i][j] + 1);
                }
                if (t[i] >= 2 && j < s) {
                    f[i + 1][j + 1] = max(f[i + 1][j + 1], f[i][j]);
                }
            }
        }

        cout << "Case #" << cur_test + 1 << ": " << f[n][s] << endl;
    }
    return 0;
}
