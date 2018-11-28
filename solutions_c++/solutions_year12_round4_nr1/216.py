#include <iostream>
#include <iomanip>
#include <queue>
#include <cassert>

using namespace std;

const int MAXN = 10005;

int n, d[MAXN], l[MAXN], D, low[MAXN];

void solve() {
  cin >> n;
  for (int i = 0; i < n; i++) cin >> d[i] >> l[i];
  cin >> D;

  for (int i = 0; i < n; i++) low[i] = 0;
  low[0] = d[0];

  for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
      if (d[j] - d[i] <= low[i]) {
        low[j] = std::max(low[j], std::min(d[j] - d[i], l[j]));
      } else {
        break;
      }
    }
  }

  bool ok = false;
  for (int i = 0; i < n; i++) {
    if (low[i] + d[i] >= D) ok = true;
  }

  cout << (ok ? "YES" : "NO") << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);

  int t;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    cout << "Case #" << i << ": ";
    solve();
  }
}





