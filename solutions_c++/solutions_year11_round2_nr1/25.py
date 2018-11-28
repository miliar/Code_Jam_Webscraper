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

int n;
char a[max_n][max_n];
Real owp[max_n], wp[max_n], oowp[max_n], rpi[max_n];
int T, I;

void input() {
  cin >> n;
  for (int x = 0; x < n; x++) {
    for (int y = 0; y < n; y++) {
      cin >> a[x][y];
    }
  }
}

Real compute_wp(int x) {
  int n_wins = 0, n_matches = 0;
  for (int y = 0; y < n; y++) {
    if (a[x][y] == '1') {
      n_wins++;
      n_matches++;
    } else if (a[x][y] == '0') {
      n_matches++;
    }
  }
  return (Real)n_wins / n_matches;
}

Real compute_wp_throw(int x, int t) {
  int n_wins = 0, n_matches = 0;
  for (int y = 0; y < n; y++) {
    if (y == t)
      continue;
    if (a[x][y] == '1')
      n_wins++;
    if (a[x][y] != '.')
      n_matches++;
  }
  return (Real)n_wins / n_matches;
}

Real compute_owp(int x) {
  Real owp = 0;
  int n_matches = 0;
  for (int y = 0; y < n; ++y) {
    if (a[x][y] != '.') {
      owp += compute_wp_throw(y, x);
      n_matches++;
    }
  }
  owp /= n_matches;
  return owp;
}

Real compute_oowp(int x) {
  Real oowp = 0;
  int n_matches = 0;
  for (int y = 0; y < n; y++) {
    if (a[x][y] != '.') {
      oowp += owp[y];
      n_matches++;
    }
  }
  oowp /= n_matches;
  return oowp;
}

Real compute_rpi(int x) {
  return wp[x] * 0.25 + owp[x] * 0.50 + oowp[x] * 0.25;
}

void solve() {
  for (int x = 0; x < n; ++x)
    wp[x] = compute_wp(x);
  for (int x = 0; x < n; ++x)
    owp[x] = compute_owp(x);
  for (int x = 0; x < n; ++x)
    oowp[x] = compute_oowp(x);
  for (int x = 0; x < n; ++x)
    rpi[x] = compute_rpi(x);
}

void output() {
  printf("Case #%d:\n", I + 1);
  for (int x = 0; x < n; ++x) {
    printf("%.10Lf\n", rpi[x]);
  }
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

