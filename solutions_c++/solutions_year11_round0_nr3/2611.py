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
const int oo = 0x7fffffff;

const int max_n = 1024;

int n, T, I;
int a[max_n];

void input() {
  cin >> n;
  for (int i = 0; i < n; ++i)
    cin >> a[i];
}

void solve() {
}

void output() {
  cout << "Case #" << I + 1 << ": ";
  int sum = 0;
  int tot = 0;
  for (int i = 0; i < n; ++i) {
    tot += a[i];
    sum ^= a[i];
  }
  if (sum != 0) {
    cout << "NO\n";
    return;
  }
  int ans = oo;
  for (int i = 0; i < n; ++i)
    ans = min(ans, a[i]);
  ans = tot - ans;
  cout << ans << endl;
}

int main() {
  cin >> T;
  for (I = 0; I < T; I++) {
    input();
    solve();
    output();
  }
	return 0;
}

