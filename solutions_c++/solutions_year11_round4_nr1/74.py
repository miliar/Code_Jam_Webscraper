#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int nt;
  assert(scanf("%d", &nt) == 1);
  for (int tt = 1; tt <= nt; tt++) {
    printf("Case #%d: ", tt);
    double x, s, r, t;
    int n;
    assert(scanf("%lf%lf%lf%lf%d", &x, &s, &r, &t, &n) == 5);
    r -= s;
    vector <pair <double, double> > a;
    double la = 0.0;
    for (int i = 0; i < n; i++) {
      double b, e, w;
      scanf("%lf%lf%lf", &b, &e, &w);
      a.push_back(make_pair(s, b - la));
      a.push_back(make_pair(s + w, e - b));
      la = e;
    }
    a.push_back(make_pair(s, x - la));
    sort(a.begin(), a.end());
    double ans = 0.0;
    for (int i = 0; i < (int)a.size(); i++) {
      double tt = a[i].second / (a[i].first + r);
      double t1 = min(tt, t);
      double t2 = (a[i].second - t1 * (a[i].first + r)) / a[i].first;
      ans += t1 + t2;
      t -= t1;
    }
    printf("%.9lf\n", ans);
  }
  return 0;
}
