#include <algorithm>
#include <iostream>
#include <set>
#include <sstream>
#include <string>

using namespace std;

int len(int n) {
  int ret = 0;
  while (n > 0) {
    n /= 10;
    ++ret;
  }
  return ret;
}

int rotate(int n, int k) {
  stringstream ss;
  ss << n;
  string s = ss.str();
  ss.str("");
  rotate(s.begin(), s.begin() + k, s.end());
  ss << s;
  ss >> n;
  return n;
}

int main(void) {
  ios::sync_with_stdio(false);
  int tt; cin >> tt;
  for (int tc = 1; tc <= tt; ++tc) {
    int a, b;
    cin >> a >> b;
    int ans = 0;
    for (int n = a; n <= b; ++n) {
      int l = len(n);
      set<int> s;
      for (int i = 1; i < l; ++i) {
        int m = rotate(n, i);
        if (len(m) == l && n < m && m <= b)
          s.insert(m);         
      }
      ans += s.size();
    }
    cout << "Case #" << tc << ": " << ans << "\n";
  }
  return 0;
}
