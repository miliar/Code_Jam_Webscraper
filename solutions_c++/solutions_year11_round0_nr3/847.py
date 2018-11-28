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

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
      cin >> a[i];
    }
    int xor = 0;
    for (int i = 0; i < n; ++i) {
      xor = (xor ^ a[i]);
    }
    if (xor != 0) {
      cout << "Case #" << test_index + 1 << ": NO" << endl;
      cerr << "Case #" << test_index + 1 << ": NO" << endl;
      continue;
    }
    int res = 0;
    for (int i = 0; i < n; ++i) {
      res += a[i];
    }
    res -= *min_element(a.begin(), a.end());
    cout << "Case #" << test_index + 1 << ": " << res << endl;
    cerr << "Case #" << test_index + 1 << ": " << res << endl;
  }
  return 0;
}
