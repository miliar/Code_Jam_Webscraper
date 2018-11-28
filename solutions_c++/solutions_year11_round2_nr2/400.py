#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <cmath>
using namespace std;

const int MAXN = 1000010;

int pos[MAXN];
int dist, n;

void init()
{
  int c;
  scanf("%d%d", &c, &dist);

  n = 0;
  for (int p, v, i = 0; i < c; ++i) {
    scanf("%d%d", &p, &v);
    for (int j = 0; j < v; ++j) pos[n++] = p;
  }
}

void solve()
{
  if (n == 1) { puts("0.0"); return; }
  sort(pos, pos+n);

  int lti, rti;
  double ans = 0.0;

  for (int l = 0, r = n-1; l < r; ) {
    if (l + 1 == r) {
      ans += dist > (pos[r] - pos[l]) ? ((dist - (pos[r] - pos[l]))/2.0) : 0;
      break;
    }
    
    lti = dist > (pos[l+1] - pos[l]) ? (dist - (pos[l+1] - pos[l])) : 0;
    rti = dist > (pos[r] - pos[r-1]) ? (dist - (pos[r] - pos[r-1])) : 0;
    if (lti > rti) {
      ans += rti;
      pos[l] -= rti;
      --r;
    } else if (rti > lti) {
      ans += lti;
      pos[r] += lti;
      ++l;
    } else {
      ans += lti;
      ++l;
      --r;
    }
  }

  printf("%.1lf\n", ans);
}

int main()
{
  int t;
  scanf("%d", &t);
  for (int l = 1; l <= t; ++l) {
    printf("Case #%d: ", l);
    init();
    solve();
  }
  return 0;
}
