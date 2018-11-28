#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        int n, pd, pg, d;
        cin >> n >> pd >> pg;
        try {
            if (n < 100) {
                for (d = n; d > 0; d--) {
                    if ((d * pd) % 100 == 0) break;
                }
                if (d == 0) throw 1;
            }
            if ((pg == 100 && pd != 100) || (pg == 0 && pd != 0)) throw 1;
            cout << "Case #" << tc << ": Possible\n";
        } catch (int err) {            
            cout << "Case #" << tc << ": Broken\n";
        }
    }
    return 0;
}
