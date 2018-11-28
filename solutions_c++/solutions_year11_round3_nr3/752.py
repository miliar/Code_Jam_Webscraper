#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
#include <utility>

using namespace std;

int main() {
    int tests;
    cin >> tests;
    int numbers[1000];
    
    for (int cn = 1; cn <= tests; cn++) {
        int n, l, h;
        cin >> n >> l >> h;
        for (int i = 0; i < n; i++) {
            cin >> numbers[i];
        }
        int ans = -1;
        for (int i = l; i <= h; i++) {
            bool possible = true;
            for (int j = 0; j < n; j++) {
                if (i % numbers[j] != 0 && numbers[j] % i != 0) {
                    possible = false;
                    break;
                }
            }
            if (possible) {
                ans = i;
                break;
            }
        }
        if (ans > 0) {
            cout << "Case #" << cn << ": " << ans << endl;        } else {
            cout << "Case #" << cn  << ": NO" << endl;
        }
    }
}