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
#define PROBLEM_ID "D"

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

vector<int> get_cycle_lengths(const vector<int>& perm) {
  vector<int> res;
  vector<bool> done(perm.size(), false);
  for (int i = 0; i < perm.size(); ++i) {
    if (!done[i]) {
      int cycle_length = 1;
      done[i] = true;
      int cur = i;
      while (!done[perm[cur]]) {
        cur = perm[cur];
        done[cur] = true;
        ++cycle_length;
      }
      res.push_back(cycle_length);
    }
  }
  return res;
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  int MAXN = 1000;
  vector<double> steps(MAXN + 1, 0);
  steps[0] = steps[1] = 0;
  for (int length = 2; length <= MAXN; ++length) {
    /*cerr << "length = " << length << endl;
    vector<int> l;
    vector<int> perm;
    for (int i = 0; i < length; ++i) {
      perm.push_back(i);
    }
    steps[length] = 1;
    do {
      vector<int> cycle_lengths = get_cycle_lengths(perm);
      if (cycle_lengths.size() == 1) {
        continue;
      }
      double res = 0;
      for (int i = 0; i < cycle_lengths.size(); ++i) {
        res += steps[cycle_lengths[i]];
      }
      for (int i = 1; i <= length; ++i) {
        res /= i;
      }
      steps[length] += res;
    } while (next_permutation(perm.begin(), perm.end()));
    steps[length] *= double(length) / double(length - 1);*/
    steps[length] = length;
  }
  /*for (int length = 0; length <= MAXN; ++length) {
    cerr << "steps[" << length << "] = " << steps[length] << endl;
  }*/
  cerr << "begin tests" << endl;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int n;
    cin >> n;
    vector<int> perm(n);
    for(int i = 0; i < n; ++i) {
      cin >> perm[i];
      --perm[i];
    }
    vector<int> cycle_length = get_cycle_lengths(perm);
    double res = 0;
    for (int i = 0; i < cycle_length.size(); ++i) {
      res += steps[cycle_length[i]];
    }
    cout << "Case #" << test_index + 1 << ": " << res << endl;
    cerr << "Case #" << test_index + 1 << ": " << res << endl;
  }
  return 0;
}
