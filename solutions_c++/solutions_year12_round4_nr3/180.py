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

bool getHeights(int n, const VI &peaks, VI &heights) {
  heights.resize(n);
  for (int i = 0; i < n; ++i)
    heights[i] = i;

  for (int i = 0; i < n-1; ++i) {
    if (peaks[i] > i+1) {
      for (int j = i+1; j < peaks[i]; ++j) 
        if (peaks[j] > peaks[i]) return false;

      int dh = heights[peaks[i]] - heights[peaks[i]-1] + 1;
      for (int j = peaks[i]-1; j > i; --j)
        heights[j] = heights[j+1] - dh;
      }
    }

  int sea = *min_element(heights.begin(), heights.end());
  for (int i = 0; i < n; ++i)
    heights[i] -= sea;

  return true;
  }

int main() {
  int nc; cin >> nc;
  for (int cur = 1; cur <= nc; ++cur) {
    int n; cin >> n;

    VI peaks(n-1);
    for (int i = 0; i < n-1; ++i) {
      cin >> peaks[i];
      --peaks[i];
      }

    cout << "Case #" << cur << ":";
    VI heights;
    if (getHeights(n, peaks, heights)) {
      for (int i = 0; i < n; ++i)
        cout << ' ' << heights[i];
      cout << '\n';
      }
    else
      cout << " Impossible\n";
    }
  }

