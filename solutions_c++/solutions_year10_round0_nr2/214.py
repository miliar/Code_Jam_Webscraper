#include <cstdio>
#include <string>
#include <vector>

using namespace std;

inline int gcd (int a, int b) {
  if (a && b)
    return gcd(max(a,b)-min(a,b), min(a,b));
  return a+b;
}

int main () {
  int tests;
  int n, i, j;
  vector<int> t;
  scanf("%d", &tests);
  for (int test = 0; test < tests; ++test) {
    scanf("%d", &n);
    t.resize(n, 0);
    for (i = 0; i < n; ++i)
      scanf("%d", &t[i]);
    int cur = abs(t[1]-t[0]);
    for (i = 0; i < n; ++i)
      for (j = 0; j < i; ++j)
        cur = gcd(cur, abs(t[i]-t[j]));
    int rem = t[0]%cur;
    int ans = 0;
    if (rem)
      ans = cur - rem;
    printf("Case #%d: %d\n", test+1, ans);
  }
};

