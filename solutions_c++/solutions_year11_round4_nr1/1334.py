#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <climits>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>

#define FOR(i, m, n) for (int i=m; i<n; i++)

using namespace std;

int X, S, R, T, N;
long double pole[2000000];

void solve() {
  long double ret = 0;
  scanf("%d%d%d%d%d", &X, &S, &R, &T, &N);
  long double t = (long double)T;
  FOR (i, 0, X+10)
    pole[i] = 0.0;
  FOR (i, 0, N) {
    int l, r, w; scanf("%d%d%d", &l, &r, &w);
    FOR (j, l, r)
      pole[j] = w;
  }
  sort(pole, pole+X);
  FOR (i, 0, X) {
    long double x = 1.0/(long double)(pole[i]+R);
    long double y = 1.0/(long double)(pole[i]+S);
    if (t>x) {
      ret += x;
      t -= x;
    }
    else if (t!=0.0) {
      ret += t; ret += (1.0 - t*(pole[i]+R))/(pole[i]+S);
      t = 0.0;
    }
    else ret += y;
  }
  printf("%.7Lf\n", ret);
}

int main()
{
  int q; scanf("%d", &q);
  FOR (i, 0, q) {
    printf("Case #%d: ", i+1);
    solve();
  }
  return 0;
}
