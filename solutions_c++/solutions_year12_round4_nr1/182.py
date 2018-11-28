#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>
#include <cmath>
#include <complex>

using namespace std;

typedef long long int LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<PII> VP;

bool possible(int n, const VP &vines, int d) {
  VI bestR(n, -1); bestR[0] = vines[0].first;

  for (int i = 0; i < n; ++i) {
    if (bestR[i] == -1)
      return false;

    if (vines[i].first + bestR[i] >= d)
      return true;

    for (int j = i+1; (j < n) && (vines[j].first - vines[i].first <= bestR[i]); ++j)
      bestR[j] = max(bestR[j], min(vines[j].second, vines[j].first - vines[i].first));
    }

  return false;
  }

int main() {
  int nc; cin >> nc;
  for (int cur = 1; cur <= nc; ++cur) {
    int n; cin >> n;

    VP vines(n);
    for (int i = 0; i < n; ++i)
      cin >> vines[i].first >> vines[i].second;

    int d; cin >> d;

    cout << "Case #" << cur << ": ";
    if (possible(n, vines, d))
      cout << "YES\n";
    else
      cout << "NO\n";
    }
  }

