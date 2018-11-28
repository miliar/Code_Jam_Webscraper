#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int po[8];
int aa[100];
int tot;

void init() {
    po[0] = 1;
    for (int i = 1; i < 8; i++) {
        po[i] = po[i - 1] * 10;
    }
}

void solve() {
    int A, B;
    cin >> A >> B;
    long long ans = 0;
    for (int m = A + 1; m <= B; m++) {
        int len = 1;
        while (po[len] <= m) len++;
        tot = 0;
        for (int l = 1; l < len; l++) {
            int n = m % po[l] * po[len - l] + m / po[l];
            if (n >= A && n < m) aa[tot++] = n;
        }
        sort(aa, aa + tot);
        int prev = -1;
        for (int i = 0; i < tot; i++) {
            if (aa[i] == prev) continue;
            ans++;
            prev = aa[i];
        }
    }
    cout << ans << endl;
}
        
int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    init();
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}
