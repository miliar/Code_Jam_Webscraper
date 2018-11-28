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

int main() {
  int nc; cin >> nc;
  for (int cur = 1; cur <= nc; ++cur) {
    int n; cin >> n;

    VP levels(n);
    for (int i = 0; i < n; ++i)
      levels[i].second = i;
    for (int i = 0; i < n; ++i) {
      int len; cin >> len;
      }
    for (int i = 0; i < n; ++i) {
      cin >> levels[i].first;
      levels[i].first = 100-levels[i].first;
      }

    sort(levels.begin(), levels.end());
    cout << "Case #" << cur << ":";
    for (int i = 0; i < n; ++i)
      cout << ' ' << levels[i].second;
    cout << '\n';
    }
  }

