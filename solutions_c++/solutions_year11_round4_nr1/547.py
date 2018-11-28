#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const double eps = 1e-7;

int main() {
  int T, C = 1, x, n;
  double w, r, t;
  cin >> T;
  while (T-- && cin >> x >> w >> r >> t >> n) {
    vector<pair<int, int> > A;
    int b, e, s;
    for (int i = 0; i < n && cin >> b >> e >> s; ++i)
      A.push_back(make_pair(s, e-b)), x -= (e-b);

    A.push_back(make_pair(0, x));
    double ans = 0;
    sort(A.begin(), A.end());

    for (int i = 0; i < int(A.size()); ++i) {
      double tt = (double)A[i].second/(A[i].first + r);
      if (tt < t+eps) {
        t -= tt, ans += tt;
        if (t < 0) t = 0;
      } else {
        double d = A[i].second - (A[i].first + r)*t;
        ans += t + d/(A[i].first + w);
        t = 0;
      }
    }

    cout.setf(ios::fixed);
    cout.precision(10);
    cout << "Case #" << C++ << ": " << ans << endl;
  }
}
