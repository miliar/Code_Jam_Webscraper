#include <iostream>
#include <vector>
using namespace std;
typedef long double ld;

int main() {
  int T, C = 1, np, d;
  cin >> T;
  while (T-- && cin >> np >> d) {
    vector<ld> P;
    int x, p;
    for (int i = 0; i < np && cin >> x >> p; ++i) {
      for (int j = 0; j < p; ++j)
        P.push_back(x);
    }

    ld mn = 0, mx = 1e50;
    while (mx-mn > 1e-7) {
      ld md = (mx+mn)/2.0;

      //cout << mx-mn << endl;
      //cout << bool(mx-mn > 1e-6) << endl;

      ld prev = -1e50;
      bool f = true;
      for (int i = 0; f && i < int(P.size()); ++i) {
        if (P[i] - prev + 1e-9 > d)
          prev = max(prev + d, P[i] - md);
        else if (prev + d - P[i] + 1e-9 > md)
          f = false;
        else
          prev = prev + d;
      }

      if (f) mx = md; else mn = md;
    }

    cout.setf(ios::fixed);
    cout.precision(2);
    cout << "Case #" << C++ << ": " << mx << endl;
  }
}
