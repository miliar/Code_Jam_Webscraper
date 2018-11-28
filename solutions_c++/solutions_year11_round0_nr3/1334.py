#include <iostream>
#include <cstdio>
#include <set>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int id = 1; id <= t; id++) {
        int a[1010], n;
        cin >> n;
        int val = 0;
        for(int i = 0; i < n; i++) {
            cin >> a[i];
            val ^= a[i];
        }
        cout << "Case #" << id << ": ";
        if(val) cout << "NO\n";
        else {
            sort(a, a + n);
            int ans = 0;
            for(int i = n - 1; i > 0; i--)
                ans += a[i];
            cout << ans << "\n";
        }
    }
    return 0;
}
