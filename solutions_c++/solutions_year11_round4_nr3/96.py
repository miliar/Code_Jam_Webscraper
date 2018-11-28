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
const int max_m = 1000010;

long long n;
long long ans;
bool is_prime[max_m];
int T, I;

void input() {
  cin >> n;
}

void solve() {
  if (n == 1) {
    ans = 0;
    return;
  }
  ans = 0;
  for (int p = 2; (long long)p * p <= n; ++p) {
    if (!is_prime[p])
      continue;
    int e = 0;
    long long q = 1;
    while (q * p <= n) {
      q *= p;
      ++e;
    }
    ans += e - 1;
  }
  ans++; // The first 1
}

void output() {
  printf("Case #%d: %lld\n", I + 1, ans);
}

void init() {
  for (int i = 0; i < max_m; ++i)
    is_prime[i] = true;
  for (int i = 2; i * i < max_m; ++i) {
    if (is_prime[i]) {
      int j = i * i;
      while (j < max_m) {
        is_prime[j] = false;
        j += i;
      }
    }
  }
}

int main() {
  init();
  cerr << "!!!!!!!\n";
  cin >> T;
  for (I = 0; I < T; ++I) {
    input();
    solve();
    output();
  }
	return 0;
}

