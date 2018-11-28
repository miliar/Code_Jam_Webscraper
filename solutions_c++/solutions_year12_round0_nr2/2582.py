#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main(void) {
  ios::sync_with_stdio(false);
  int tt; cin >> tt;
  for (int tc = 1; tc <= tt; ++tc) {
    int n, s, p;
    cin >> n >> s >> p;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      int t, a, b;
      cin >> t;
      a = b = t / 3;
      int r = t % 3;
      switch (r) {
        case 0: break;
        case 1: ++a; break;
        case 2: ++a; ++b; break;
      }
      if (s > 0 && r != 1 && a + 1 == p && b > 0) {
        ++a; --b; --s;
      }
      if (a >= p)
        ++ans;
    }
    cout << "Case #" << tc << ": " << ans << "\n";
  }
  return 0;
}
