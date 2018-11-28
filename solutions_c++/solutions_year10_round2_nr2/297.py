#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

int x[100], v[100];

int main() {
  int _t; cin >> _t;
  for (int _tt = 1; _tt <= _t; _tt++) {
    cout << "Case #" << _tt << ": ";

    int n, k, b, t;
    cin >> n >> k >> b >> t;
    for (int i = 0; i < n; i++)
      cin >> x[i];
    for (int i = 0; i < n; i++)
      cin >> v[i];

    int result = 0, can = 0, bad = 0;
    for (int j = n - 1; j >= 0 && can != k; j--) {
      int xj = x[j];
      int vj = v[j];

      int need = b - xj;
      if (t * vj >= need) {
        result += bad;
        can++;
      } else {
        bad++;
      }
    }

    if (can != k)
      cout << "IMPOSSIBLE" << endl;
    else
      cout << result << endl;

  }

  return 0;
}
