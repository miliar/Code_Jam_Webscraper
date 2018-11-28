#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int main() {
    unsigned int t, n, k;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        cin >> n >> k;
        int m = pow<int>(2, n);
        if ((k % m) == (m - 1))
            printf("Case #%d: ON\n", i);
        else
            printf("Case #%d: OFF\n", i);
    }
    return (0);
}

