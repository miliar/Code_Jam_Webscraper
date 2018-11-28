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

const int max_n = 128;

int a[max_n], c[max_n][max_n];
int n, s, p;
int T, I;

void input() {
  cin >> n >> s >> p;
  for (int i = 0; i < n; ++i)
    cin >> a[i];
}

bool can_s(int k) {
  return k >= 2 && k <= 28;
}

bool can_s_wp(int k) {
  return can_s(k) && k >= p + max(0, p - 2) * 2;
}

bool can_ns(int k) {
  return true;
}

bool can_ns_wp(int k) {
  return can_ns(k) && k >= p + max(0, p - 1) * 2;
}

void solve() {
  memset(c, -1, sizeof c);
  for (int i = -1; i < n - 1; ++i) {
    int low_j = 0, high_j = n;
    if (i == -1) {
      low_j = 0;
      high_j = 0;
    }
    for (int j = low_j; j <= high_j; ++j) {
      int k = (i == -1 ? 0 : c[i][j]);
      if (c[i][j] >= 0) {
        if (can_s(a[i + 1]))
          c[i + 1][j + 1] = max(c[i + 1][j + 1], k + can_s_wp(a[i + 1]));
        if (can_ns(a[i + 1]))
          c[i + 1][j] = max(c[i + 1][j], k + can_ns_wp(a[i + 1]));
      }
    }
  }
}

void output() {
  assert(c[n - 1][s] >= 0);
  cout << "Case #" << (I + 1) << ": " << c[n - 1][s] << "\n";
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

