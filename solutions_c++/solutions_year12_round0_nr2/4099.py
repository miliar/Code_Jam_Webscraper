#include <cstdio>
#include <iostream>
using namespace std;

int n, s, p, ans, T, x;

void solve() {
    ans = 0;
    cin >> n >> s >> p;
    for (int i = 0; i < n; ++i) {
        cin >> x;
        if (p == 1) {
            if (x >= 1)
                ++ans;
            continue;
        }
        if (x >= p * 3 - 2) {
            ++ans;
            continue;
        }
        if ((s > 0) && (x >= p * 3 - 4)) {
            ++ans;
            --s;
        }
    }
    cout << ans << endl;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d\n", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        solve();
    }
    return 0;

}
