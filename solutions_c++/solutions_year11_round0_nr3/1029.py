#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int n;
int c[1005];

int main() {
    freopen("candy.in", "r", stdin);
    freopen("candy.out", "w", stdout);
    int tests; cin >> tests;
    for (int testID = 1; testID <= tests; ++testID) {
        cin >> n;
        for (int i = 0; i < n; ++i)
            cin >> c[i];
        sort(c, c + n);
        int x = 0;
        int s = 0;
        for (int i = 1; i < n; ++i) {
            x ^= c[i];
            s += c[i];
        }
        cout << "Case #" << testID << ": ";
        if (x != c[0]) cout << "NO" << endl;
        else cout << s << endl;
    }
    return 0;
}
