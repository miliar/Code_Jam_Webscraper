#include <iostream>
#include <cstdio>

using namespace std;

int T, tc;
int n, h, l;
int f[200];

int main() {
    int i, ans;
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small.out", "w", stdout);
    cin >> T;
    for (tc = 1; tc <= T; tc++) {
        cin >> n >> l >> h;
        for (i = 0; i < n; i++) cin >> f[i];
        cout << "Case #" << tc << ": ";
        for (ans = l; ans <= h; ans++) {
            for (i = 0; i < n; i++) {
                if ((f[i] % ans) > 0 && (ans % f[i]) > 0) break;
            }
            if (i >= n) {
                cout << ans << endl;
                break;
            }
        }
        if (ans > h) cout << "NO" << endl;
    }

    return 0;
}
