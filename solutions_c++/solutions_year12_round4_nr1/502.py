#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdio>
#include <cmath>

using namespace std;

typedef long long llong;
typedef pair<int, int> pii;

const double INFTY = 2e9;
const double EPS = 1e-5;

inline double sqr(double x) { return x * x; }

void solve() 
{
  int n;
  cin >> n;
  vector<int> d(n), l(n);
  for (int i = 0; i < n; ++i) cin >> d[i] >> l[i];
  int target;
  cin >> target;
  vector<int> maxlen(n, 0);
  maxlen[0] = d[0];

  for (int i = 0; i < n - 1; ++i) {
    if (maxlen[i] == 0) continue;
    for (int j = i + 1; j < n && d[j] - d[i] <= maxlen[i]; ++j) {
      int len = min(d[j] - d[i], l[j]);
      maxlen[j] = max(maxlen[j], len);
    }
  }
  for (int i = n - 1; i >= 0; --i) {
    if (maxlen[i] >= target - d[i]) {
      printf("YES\n");
      return;
    }
  }
  printf("NO\n");
}

int main()
{
  int T;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}
