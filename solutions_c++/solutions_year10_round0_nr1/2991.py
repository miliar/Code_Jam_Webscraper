#include <iostream.h>
#include <math.h>

int main() {
    unsigned int n, k, t;

    cin >> t;

    for(double i = 0; i < t; i++) {
        cin >> n >> k;
        unsigned int p = pow(2, n);
        if(k % p == p - 1) cout << "Case #" << i+1 << ": ON\n";
        else cout << "Case #" << i+1 << ": OFF\n";
    }

    return 0;
}
