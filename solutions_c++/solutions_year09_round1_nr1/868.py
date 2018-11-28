#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <set>
#include <cassert>
using namespace std;
#define debug(x) cerr << __LINE__ << ": " << #x << " = " << (x) << "\n"
#define debugf(x...) fprintf(stderr, x)

string tos(int x, int base) {
  string r;
  while (x > 0) {
    r += (x % base) + '0';
    x /= base;
  }
  return r;
}

set<int> seen;

bool solve(int x, int base) {
  if (seen.count(x)) return false;
  seen.insert(x);
  string s = tos(x, base);
  int n = 0, l = s.size();
  for (int i = 0; i < l; ++i) n += (s[i] - '0') * (s[i] - '0');
  if (n == 1) return true;
  return solve(n, base);
}

void solve() {
  char s[128];
  fgets(s, 128, stdin);
  int m = 0, a[9];
  for (int i = 0, c = 0; s[i] != '\0'; ++i) {
    if (s[i] < '0' || s[i] > '9') {
      if (c != 0) a[m++] = c;
      c = 0;
    } else {
      c = c * 10 + s[i] - '0';
    }
  }
  for (int i = 2; ; ++i) {
    for (int j = 0; j < m; ++j) {
      seen.clear();
      if (!solve(i, a[j])) goto bad;
    }
    printf("%d\n", i);
    return;
    bad: ;
  }
  assert(0);
}

int main() {
  int n;
  scanf("%d\n", &n);
  for (int i = 1; i <= n; ++i) printf("Case #%d: ", i), solve();
  return 0;
}

