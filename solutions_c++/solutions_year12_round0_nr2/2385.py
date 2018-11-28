#include <iostream>
using namespace std;

int main() {
  int T, cas;
  cin >> T;
  cas = 1;
  while (cas <= T) {
    int n, s, p, sol; //minS = 3*p -2, minNS = 3*p - 4;
    cin >> n >> s >> p;
    sol = 0;
    for (int i = 0; i < n; ++i) {
      int t;
      cin >> t;
      if (t >= 3*p - 2) ++sol;
      else if (s > 0 and t >= 3*p - 4 and t > 0) {
        ++sol;
        --s;
      }
    }
    cout << "Case #" << cas << ": " << sol << endl;
    ++cas;
  }
}