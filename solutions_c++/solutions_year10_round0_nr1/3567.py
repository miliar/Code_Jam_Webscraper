#include <iostream>
#include <cmath>
using namespace std;

int main(int argc, char** argv) {
    long t, n, k;

    cin >> t;
    for (int i = 1; i <= t; i++) {
       bool on = false;
       long l = 1;

       cin >> n >> k;

       for (int j = 1; j <= n; j++) {
           l *= 2;
       }
       long q = (k + 1) % l;
       if (q == 0) {
           on = true;
       }
       cout << "Case #" << i << ": ";
       if (on) {
           cout << "ON";
       } else {
           cout << "OFF";
       }
       cout << endl;
    }

    return 0;
}

