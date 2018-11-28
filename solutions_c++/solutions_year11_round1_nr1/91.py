#include <iostream>
#include <cstdio>

using namespace std;

long long n;
long long a1, b1;
long long a2, b2;

long long gcd(long long a, long long b) {
    return b == 0 ? a : gcd(b, a % b);
}

int main() {
    freopen("bla.in", "r", stdin);
    freopen("bla.out", "w", stdout);
    int tests;
    cin >> tests;
    for (int testID = 1; testID <= tests; ++testID) {
        cin >> n >> a1 >> a2;
        long long tmp1 = a1;
        long long tmp2 = a2;
        b1 = 100;
        long long t1 = gcd(a1, b1);
        a1 /= t1;
        b1 /= t1;
        a1 = tmp1;
        a2 = tmp2;
        cout << "Case #" << testID << ": ";
        if (b1 > n || (a1 < 100 && a2 == 100) || (a1 > 0 && a2 == 0)) cout << "Broken" << endl;
        else cout << "Possible" << endl;
    }
    return 0;
}
