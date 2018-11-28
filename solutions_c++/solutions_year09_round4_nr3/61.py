#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "C"

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

bool Less(const vector<int>& a, const vector<int>& b) {
  for (int i = 0; i < a.size(); ++i) {
    if (a[i] >= b[i]) {
      return false;
    }
  }
  return true;
}

bool comparable(const vector<int>& a, const vector<int>& b) {
  return Less(a, b) || Less(b, a);
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int lines, points;
    cin >> lines >> points;
    vector< vector<int> > charts(lines, vector<int>(points));
    for (int line = 0; line < lines; ++line) {
      for (int point = 0; point < points; ++point) {
        cin >> charts[line][point];
      }
    }
    int result = 1;
    for (int mask = 0; mask < (1 << lines); ++mask) {
      vector< vector<int> > charts_subset;
      for (int i = 0; i < lines; ++i) {
        if ((mask >> i) & 1) {
          charts_subset.push_back(charts[i]);
        }
      }
      bool ok = true;
      for (int i = 0; i < charts_subset.size(); ++i) {
        for (int j = i + 1; j< charts_subset.size(); ++j) {
          if (comparable(charts_subset[i], charts_subset[j])) {
            ok = false;
            break;
          }
        }
      }
      if (ok) {
        result = max(result, (int)charts_subset.size());
      }
    }
    cout << "Case #" << test_index + 1 << ": " << result << endl;
    cerr << "test " << test_index + 1 << " of " << test_count << endl;
  }
  return 0;
}
