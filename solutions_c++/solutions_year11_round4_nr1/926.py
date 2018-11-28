#include <cstdio>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

int main() {
  int T; scanf("%d", &T);
  for(int kase=1; kase<=T; ++kase) {
    int X, S, R, t, N; scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
    int Y      = 0;
    vector<pair<int, int> > a;
    for(int i=0; i<N; ++i) {
      int b, e, w; scanf("%d%d%d", &b, &e, &w);
      a.push_back(pair<int, int>(w, e-b));
      Y += e-b;
    }
    a.push_back(pair<int, int>(0, X-Y));
    sort(a.begin(), a.end());
    double ans = 0;
    double T   = t;
    for(int i=0; i<a.size(); ++i) {
      double run = a[i].second/(0.+R+a[i].first);
      if (run > T) {
	run = T;
      }
      T -= run;
      double walk = (a[i].second - (0.+R+a[i].first)*run)/(S+a[i].first);
      ans += run + walk;
    }
    printf("Case #%d: %.15lf\n", kase, ans);
  }
}
