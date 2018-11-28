#include <iostream>
using namespace std;

int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

int main() {
    int tot_t;
    cin >> tot_t;
    for (int cur_t = 0; cur_t < tot_t; ++cur_t) {
        int n, pd, pg;
        cin >> n >> pd >> pg;
        int d = 100 / gcd(pd, 100);
        cout << "Case #" << cur_t + 1 << ": ";
        if (d > n) {
            cout << "Broken" << endl;
        } else {
            bool ok = true;
            if (pd != 0 && pg == 0) {
                ok = false;
            }
            if (100 - pd != 0 && 100 - pg == 0) {
                ok = false;
            }
            cout << (ok ? "Possible" : "Broken") << endl;
        }
    }
    return 0;
}

