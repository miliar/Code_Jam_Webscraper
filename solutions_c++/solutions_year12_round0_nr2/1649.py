#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        int n, s, p;
        cin >> n >> s >> p;
        vector <int> t(n);
        for (int i = 0; i < n; ++i)
            cin >> t[i];
        sort(t.begin(), t.end());
        reverse(t.begin(), t.end());

        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int pp = t[i] / 3 + int(t[i] % 3 > 0);
            if (pp >= p) ++ans;
            else if (s && t[i] >= 2) {
                --s;
                pp = (t[i] - 2) / 3 + 2;
                if (pp >= p) ++ans;
            }
        }

        cout << "Case #" << tt << ": " << ans << '\n';
    }

    return 0;
}
