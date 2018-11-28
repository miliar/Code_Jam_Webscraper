#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

int a[1001];

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int t, tt, i, n;
    cin >> t;
    for (tt = 1; tt <= t; tt++) {
        cin >> n;
        for (i = 0; i < n; i++) cin >> a[i];
        sort(a, a + n);
        int sum, tmp = 0;
        sum = 0;
        for (i = 0; i < n; i++) {
            sum += a[i];
            tmp ^= a[i];
        }
        cout << "Case #" << tt << ": ";
        if (tmp) cout  << "NO" << endl;
        else cout << sum - a[0] << endl;
    }
    return 0;
}
