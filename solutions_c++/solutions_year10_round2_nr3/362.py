#include <iostream>

using namespace std;

int f[501][501];

int get(int n, int m) {
    if ((n == 0) && (m >= 0)) return 1;
    if (n < 0) return 0;
    if ((n > 0) && (m == 0)) return 0;
    return f[n][m];
}

int a[501];

int main() {
    for (int i = 1; i <= 500; i++) {
        for (int j = 1; j <= 500; j++) {
            f[i][j] = 0;
            for (int k = i - 1; k >= i - j; k--) {
                f[i][j] += get(k, j);
                f[i][j] %= 100003;
            }
        }
    }
    for (int i = 0; i <= 500; i++) {
        a[i] = 0;
        for (int j = 0; j <= i; j++) {
            a[i] += get(j, i - j);
            a[i] %= 100003;
        }
    }
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        int n;
        cin >> n;
        cout << "Case #" << i << ": " << a[n - 1] << endl;
    }
    return 0;
}

