#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        int n;
        cin >> n;
        int candies[n];
        for (int i = 0; i < n; i++) {
            cin >> candies[i];
        }
        int max_sum = -1;
        for (int mask = 1; mask < (1 << n) - 1; mask++) {
            int p = 0, o = 0, p_real = 0, s_real = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) > 0) {
                    p ^= candies[i];
                    p_real += candies[i];
                } else {
                    o ^= candies[i];
                    s_real += candies[i];
                }
            }
            if (p == o) {
                max_sum = max(max_sum, s_real);
            }
        }
        cout << "Case #" << tc << ": ";
        if (max_sum == -1) {
            cout << "NO";
        } else {
            cout << max_sum;
        }
        cout << endl;
    }
    return 0;
}
