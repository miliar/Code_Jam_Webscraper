#include <iostream>
#include <vector>

using namespace std;

int main() {
  int nt;
  cin >> nt;
  for (int t = 1; t <= nt; ++t) {
    int r, k, n;
    cin >> r >> k >> n;

    vector<int> g(2 * n);
    vector<int> sums(n);
    vector<int> next(n);

    for (int i = 0; i < n; ++i) {
      cin >> g[i];
      g[i + n] = g[i];
    }

    for (int i = 0; i < n; ++i) {
      int total = 0;
      int j = i;
      for (; j < i + n; ++j) {
        if (total + g[j] <= k) {
          total += g[j];
        } else {
          break;
        }
      }
      sums[i] = total;
      next[i] = j % n;
    }

    unsigned long long res = 0;
    int x = 0;
    for (int i = 0; i < r; ++i) {
//      cout << "(" << sums[x] << " " << next[x] << ")\n";
      res += sums[x];
      x = next[x];
    }
    cout << "Case #" << t << ": " << res << endl;
  }
  return 0;
}
