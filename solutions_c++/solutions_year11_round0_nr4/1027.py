#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int n;
int a[1005];

int m[1005];

int go(int u) {
    if (m[u]) return 0;
    m[u] = 1;
    return go(a[u] - 1) + 1;
}

int main() {
    freopen("goro.in", "r", stdin);
    freopen("goro.out", "w", stdout);
    int tests; cin >> tests;
    for (int testID = 1; testID <= tests; ++testID) {
        cin >> n;
        for (int i = 0; i < n; ++i)
            cin >> a[i];
        int res = 0;
        memset(m, 0, sizeof(m));
        for (int i = 0; i < n; ++i)
            if (!m[i]) {
                int t = go(i);
                if (t > 1) res += t;
            }
        cout << "Case #" << testID << ": " << res << ".000000" << endl;
    }
    return 0;
}
