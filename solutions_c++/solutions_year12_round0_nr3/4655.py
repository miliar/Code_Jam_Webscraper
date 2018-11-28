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
#define PROBLEM_ID "B"

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

vector<int> get_digs(int n) {
  vi res;
  while (n) {
    res.push_back(n % 10);
    n /= 10;
  }
  return res;
}

bool AreRecycled(int n, int m) {
  vector<int> digs_n = get_digs(n);
  vector<int> digs_m = get_digs(m);
  if (digs_n.size() != digs_m.size()) {
    return false;
  }
  if (n == m) {
    return true;
  }
  for (int k = 1; k < digs_n.size(); ++k) {
    bool ok = true;
    for (int i = 0; i < k; ++i) {
      if (digs_n[i] != digs_m[digs_n.size() - k + i]) {
        ok = false;
        break;
      }
    }
    for (int i = 0; i < digs_n.size() - k; ++i) {
      if (digs_n[i + k] != digs_m[i]) {
        ok = false;
        break;
      }
    }
    if (ok) {
      return true;
    }
  }
  return false;
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    cerr << "Case #" << test_index + 1 << ": ";
    int A, B;
    cin >> A >> B;
    int result = 0;
    for (int n = A; n < B; ++n) {
      for (int m = n + 1; m <= B; ++m) {
        if (AreRecycled(n, m)) {
          ++result;
        }
      }
    }
    cout << "Case #" << test_index + 1 << ": " << result << endl;
  }
  return 0;
}
