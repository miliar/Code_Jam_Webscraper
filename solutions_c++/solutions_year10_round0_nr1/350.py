#include <iostream>

using namespace std;
typedef long long LL;

bool solve() {
    int n, k;
    cin >> n >> k;
    int w = (1 << n);
    return ((k + 1) % w == 0);
}

int main() {
    int te;
    cin >> te;
    for (int l = 1; l <= te; l++) {
        if (solve()) {
            cout << "Case #" << l << ": ON" << endl;
        }
        else {
            cout << "Case #" << l << ": OFF" << endl;
        }
    }
}

