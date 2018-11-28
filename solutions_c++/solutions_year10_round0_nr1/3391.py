#include <iostream>
#include <fstream>
using namespace std;
#define FOR(i, a, b) for (int i=int(a); i<=int(b); ++i)

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t, n, k;
    cin >> t;
    FOR(test, 1, t) {
          cin >> n >> k;
          string res = (k % (1 << n) == ((1 << n) - 1))?"ON" :"OFF";
          cout << "Case #" << test <<": " << res << endl;
    }
}
