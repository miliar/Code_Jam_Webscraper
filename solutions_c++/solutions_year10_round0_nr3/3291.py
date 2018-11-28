#include <iostream>
#include <fstream>
using namespace std;
#define FOR(i, a, b) for (int i=int(a); i<=int(b); ++i)

int main() {
    freopen("C-small-attempt3.in", "r", stdin);
    freopen("C.out", "w", stdout);
    unsigned long long n, r, k;
    unsigned long long g[1000], sum[1000], last[1000];
    int t;
    cin >> t;
    FOR(test, 1, t) {
              cin >> r >> k >> n;
              FOR(i, 0, n-1) cin >> g[i];
              unsigned long long res = 0;
              FOR(i, 1, r) {
                     unsigned long long s = 0;
                     FOR(j, 0, n-1)
                            if (s + g[j] <= k) s += g[j];
                            else {
                                 int gg[1001];
                                 int q = 0;
                                 FOR(p, j, n-1) gg[q++] = g[p];
                                 FOR(p, 0, j-1) gg[q++] = g[p];
                                 copy(gg, gg+n, g);
                                 break;
                            }
                     res += s;       
              }
              cout << "Case #" << test <<": " << res;
              if (test != t) cout << endl;
    }
}
