#include <iostream>
#include <vector>

using namespace std;

typedef long double ld;

int main() {
  cout.setf(ios::fixed);
  cout.precision(9);
  int T;
  cin >> T;
  for (int ca = 1; T--; ++ca) {
    cerr << "ca: " << ca << endl;
    int x, s, r, n;
    ld t;
    cin >> x >> s >> r >> t >> n;
    vector<int> v(x, s);
    for (int i = 0; i < n; ++i) {
      int b, e, w;
      cin >> b >> e >> w;
      for (int j = b; j < e; ++j) {
        v[j] += w;
      }
    }
    sort(v.begin(), v.end());
    ld ans = 0.0;
    for (int i = 0; i < int(v.size()); ++i) {
      ld cur = 1.0/ld(v[i]+r-s);
      if (t > cur) {
        ans += cur;
        t -= cur;
      }
      else if (t > 0.0) {
        ld distleft = 1.0-ld(v[i]+r-s)*t;
        ans += t+distleft/ld(v[i]);
        t = 0.0;
      }
      else {
        ans += 1.0/ld(v[i]);
      }
    }
    cout << "Case #" << ca << ": " << ans << endl;
  }
}
