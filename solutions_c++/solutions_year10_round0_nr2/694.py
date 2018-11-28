// compiled with gmp c++ wrappers
// -lgmpxx -lgmp

#include <iostream>
#include <string>

#include <gmpxx.h>

using namespace std;

int T;
int N;
mpz_class a[1000];

mpz_class gcd(mpz_class a, mpz_class b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}

int main() {
    cin >> T;
    int t = 1;
    while (t <= T) {
        int N;
        cin >> N;
        for (int i = 0; i < N; i++) {
            string str;
            cin >> str;
            a[i] = str;
        }
        mpz_class res = 0;
        for (int i = 1; i < N; i++) {
            res = gcd(res, a[i] - a[i - 1]);
        }
        if (res < 0) {
            res = - res;
        }
        cout << "Case #" << t << ": ";
        if (a[0] % res == 0) {
            cout << 0 << endl;
        } else {
            cout << res - (a[0] % res) << endl;
        }
        t++;
    }
    return 0;
}

