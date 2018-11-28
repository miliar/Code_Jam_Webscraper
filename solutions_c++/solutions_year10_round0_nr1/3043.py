#include <iostream>

using namespace std;

int main() {
    int c;
    cin >> c;
    for (int i = 0; i < c; i ++) {
        int n, k;
        cin >> n;
        cin >> k;
        // just divide k+1 it by 2^n and then multiple by 2^n if k+1 returns it is divisable by 2^n
        // k + 1 % 2^n = 0
        k ++;
        int k2 = k >> n;
        int k3 = k2 << n;
        if (k3 == k) {
            cout << "Case #" << (i+1) << ": " << "ON" << endl;
        } else {
            cout << "Case #" << (i+1) << ": " << "OFF" << endl;
        }
    }
    return 0;
}
