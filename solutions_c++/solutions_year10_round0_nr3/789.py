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
    int rides, capacity, group_count;
    cin >> rides >> capacity >> group_count;
    vector<int> group_sizes(group_count);
    for (int i = 0; i < group_count; ++i) {
      cin >> group_sizes[i];
    }
    for (int i = 0; i < group_count; ++i) {
      group_sizes.push_back(group_sizes[i]);
    }
    vector<int> next(group_count);
    for (int i = 0; i < group_count; ++i) {
      int sum = group_sizes[i];
      int last = i;
      while (last + 1 < i + group_count && sum + group_sizes[last + 1] <= capacity) {
        ++last;
        sum += group_sizes[last];
      }
      next[i] = (last + 1) % group_count;
    }
    int current = 0;
    int full_circles = 0;
    for (int i = 0; i < rides; ++i) {
      if (next[current] <= current) {
        ++full_circles;
      }
      current = next[current];
    }
    vector<ll> sums(group_count);
    sums[0] = group_sizes[0];
    for (int i = 1; i < group_count; ++i) {
      sums[i] = sums[i - 1] + group_sizes[i];
    }
    ll result = ll(full_circles) * sums.back();
    if (current > 0) {
      result += sums[current - 1];
    }
    cerr << "Case #" << test_index + 1 << " done" << endl;
    cout << "Case #" << test_index + 1 << ": " << result << endl;
  }
  return 0;
}
