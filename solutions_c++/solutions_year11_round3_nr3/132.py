#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <algorithm>

using namespace std;

const int N = 10000;
int f[N];

int main() {
  int t; cin >> t;
  for (int tt = 1; tt <= t; tt++) {
    int n, l, h; cin >> n >> l >> h;
    for (int i = 0; i < n; i++) cin >> f[i];

    int res = -1;
    while (l <= h) {
      bool v = true;
      for (int i = 0; v && i < n; i++) {
        if (max(l, f[i]) % min(l, f[i]) != 0) v = false;
      }
      if (v) {
        res = l;
        break;
      }
      l++;
    }
    cout << "Case #" << tt << ": ";
    if (res < 0) cout << "NO" << endl; else cout << res << endl;
  }

  return 0;
}

