#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <cassert>
#include <queue>
#include <cctype>
using namespace std;

typedef long double Real;

const Real o = 1e-8;
const Real pi = acos(-1.0);
const int max_n = 1024;

int n;
int idx[2];
vector<int> a[2];
int d[2][max_n], t[2][max_n];
vector<int> c;
int T, I;

void input() {
  cin >> n;
  a[0].clear(); a[1].clear();
  c.clear();
  for (int i = 0; i < n; ++i) {
    char ch;
    int x;
    cin >> ch >> x;
    if (ch == 'O')
      a[0].push_back(x);
    else
      a[1].push_back(x);
    c.push_back(ch == 'O' ? 0 : 1);
  }
}

int dist(int a, int b) {
  return abs(a - b) + 1;
}

void solve() {
  for (int p = 0; p < 2; ++p) {
    for (size_t j = 0; j < a[p].size(); ++j) {
      d[p][j] = dist(j == 0 ? 1 : a[p][j - 1], a[p][j]);
    }
  }
  idx[0] = idx[1] = 0;
  for (size_t k = 0; k < c.size(); ++k) {
    int p = c[k];
    int i = idx[p];
    int self = (i == 0 ? 0 : t[p][i - 1]) + d[p][i];
    int last;
    if (k == 0)
      last = 1;
    else {
      int last_p = c[k - 1];
      assert(idx[last_p] > 0);
      last = t[last_p][idx[last_p] - 1] + 1;
    }
    t[p][i] = max(self, last);
    ++idx[p];
  }
#if 0
  for (int p = 0; p < 2; ++p) {
    for (size_t i = 0; i < a[p].size(); ++i) {
      cerr << t[p][i] << " ";
    }
    cerr << endl;
  }
#endif
}

void output() {
  int ans = 0;
  for (int p = 0; p < 2; ++p) {
    if (a[p].size() > 0)
      ans = max(ans, t[p][a[p].size() - 1]);
  }
  cout << "Case #" << I + 1 << ": " << ans << endl;
}

int main() {
  cin >> T;
  for (I = 0; I < T; ++I) {
    input();
    solve();
    output();
  }
	return 0;
}

