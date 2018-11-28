#include <iostream>
#include <fstream>
using namespace std;
#define FOR(i, a, b) for (int i=int(a); i<=int(b); ++i)
#define FORD(i, a, b) for (int i=int(a); i>=int(b); i--)
int main() {
    freopen("C.in1", "r", stdin);
    freopen("C.ou1", "w", stdout);
    int t, a1, a2, b1, b2;
    cin >> t;
    FOR(test, 1, t) {
              cin >> a1 >> a2 >> b1 >> b2;
              int res = 0;
              FOR(i, a1, a2)
                     FOR(j, b1, b2) {
                            int x = i, y = j, k = 0;
                            while (true) {
                                  if (x < y) swap(x, y);
                                  if (x == y) {
                                        if (k == 1) res++;
                                        break;
                                  }
                                  if (x >= 2*y) {
                                        if (k == 0) res++;
                                        break;
                                  }
                                  x -= y;
                                  k = 1 - k;
                            }
                     }
              cout << "Case #" << test <<": " << res << endl;       
    }
}
