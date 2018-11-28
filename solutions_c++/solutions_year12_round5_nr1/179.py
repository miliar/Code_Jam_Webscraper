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
#define PROBLEM_ID "A"

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
    vector<int> L(n);
    for (int i = 0; i < n; ++i) {
      cin >> L[i];
    }
    vector<int> P(n);
    for (int i = 0; i < n; ++i) {
      cin >> P[i];
    }
    vector<vi> to_sort;
    for (int i = 0; i < n; ++i) {
      vector<int> a;
      a.push_back(-L[i] * P[i]);
      a.push_back(-P[i]);
      a.push_back(i);
      to_sort.push_back(a);
    }
    sort(to_sort.begin(), to_sort.end());
    cout << "Case #" << test_index + 1 << ":";
    for (int i = 0; i < to_sort.size(); ++i) {
      cout << ' ' << to_sort[i][2];
    }
    cout << endl;
  }
  return 0;
}
