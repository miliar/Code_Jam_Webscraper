#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int main() {
    int tests;
    cin >> tests;

    for (int cn = 1; cn <= tests; cn++) {
        int t, n, xr = 0, sum = 0, min = 10000000;
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> t;
            xr ^= t;
            sum += t;
            if (min > t)
                min = t;
        }
        if (xr == 0) 
            cout << "Case #" << cn << ": " << sum - min << endl;
        else 
            cout << "Case #" << cn << ": NO" << endl;
    }
}