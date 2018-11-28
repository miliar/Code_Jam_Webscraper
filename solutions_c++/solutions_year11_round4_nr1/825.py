#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>
#define sz(a) ((int)(a).size())

using namespace std;

int testcase;
int x, s, r, n, wi;
double t;
int a[1000][3];
vector< pair<int, pair<int, int> > > b;

int main(int argc, char *argv[]) {
  cin >> testcase;
  for (int tn = 1; tn <= testcase; ++tn) {
    cin >> x >> s >> r >> t >> n;
    b.clear();
    for (int i = 0; i < n; ++i) {
      cin >> a[i][0] >> a[i][1] >> a[i][2];
      if (i == 0 && a[i][0] != 0) {
        b.push_back(make_pair(s, make_pair(0, a[i][0])));
      } else if (i != 0 && a[i][0] != a[i-1][1]) {
        b.push_back(make_pair(s, make_pair(a[i-1][1], a[i][0])));
      }
      b.push_back(make_pair(s+a[i][2], make_pair(a[i][0], a[i][1])));
    }
    if (a[n-1][1] != x)
      b.push_back(make_pair(s, make_pair(a[n-1][1], x)));
    sort(b.begin(), b.end());
    double ans = 0;
    for (int i = 0; i < sz(b); ++i) {
      // cout << b[i].second.second << " " << b[i].second.first << "/ " <<  (double)b[i].first << endl;
      ans += (b[i].second.second - b[i].second.first) / (double)b[i].first;
    }
    // cout << ans << endl;
    for (int i = 0; i < sz(b); ++i) {
      // cout << b[i].first << ", " << b[i].second.first << " " << b[i].second.second <<endl;
      if ((b[i].first + r - s) * t >=  (b[i].second.second - b[i].second.first)) {
        // cout << (b[i].second.second - b[i].second.first) * (r-s) / (double)(b[i].first) / (double)(b[i].first + r - s) << endl;
        ans -= (b[i].second.second - b[i].second.first) * (r-s) / (double)(b[i].first) / (double)(b[i].first + r - s);
        t -= (b[i].second.second - b[i].second.first) / (double)(b[i].first + r - s);
      } else {
        // cout << "@#" << t << " " << (b[i].first + r - s) * t << endl;
        // cout << "!"<<((b[i].first + r - s) * t) * (r-s) / (double)(b[i].first) / (double)(b[i].first + r - s)<<endl;
        ans -= ((b[i].first + r - s) * t) * (r-s) / (double)(b[i].first) / (double)(b[i].first + r - s);
        break;
      }
    }
    printf("Case #%d: %.8lf\n", tn, ans);
    // cout << "Case #" << tn << ": " << ans << endl;
  }
  return 0;
}
