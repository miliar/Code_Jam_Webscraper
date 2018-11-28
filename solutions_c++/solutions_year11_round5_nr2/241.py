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

int StupidSolution(int n, const vector<int>& cards) {
  vector<int> min_length(1 << n, 0);
  min_length[0] = n;
  for (int mask = 0; mask < (1 << n); ++mask) {
    for (int submask = mask; submask > 0; submask = (mask & (submask - 1))) {
      vector<int> values;
      for (int i = 0; i < n; ++i) {
        if ((submask & (1 << i)) != 0) {
          values.push_back(cards[i]);
        }
      }
      sort(values.begin(), values.end());
      bool straight = true;
      for (int i = 0; i + 1 < values.size(); ++i) {
        if (values[i + 1] != values[i] + 1) {
          straight = false;
          break;
        }
      }
      if (straight) {
        min_length[mask] = max(min_length[mask], min(min_length[mask ^ submask], (int)values.size()));
      }
    }
  }
  return min_length[(1 << n) - 1];
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int n;
    cin >> n;
    vector<int> cards(n);
    for (int i = 0; i < n; ++i) {
      cin >> cards[i];
      --cards[i];
    }
    int min_length = StupidSolution(n, cards);
    cout << "Case #" << test_index + 1 << ": " << min_length << endl;
    cerr << "Case #" << test_index + 1 << ": " << min_length << endl;
  }
  return 0;
}
