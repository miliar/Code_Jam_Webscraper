#include <iostream>
#include <cmath>
using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n, s, p, t1, t2;
        t1 = t2 = 0;
        cin >> n >> s >> p;
        for (int j = 0; j < n; j++) {
            int a;
            cin >> a;
            if ((a + 2) / 3 >= p) {
                t1++;
            } else if ((a + 4) / 3 >= p && a - 2 >= 0) {
                t2++;
            }
        }
        cout << "Case #" << i + 1 << ": " << t1 + min(t2, s) << endl;
    }
    return 0;
}
