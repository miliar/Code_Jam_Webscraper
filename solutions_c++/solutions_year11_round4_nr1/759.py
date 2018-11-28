#include <stdio.h>
#include <algorithm>
#include <vector>
#include <cassert>
#include <utility>
using namespace std;
#define FOR(q, n) for(int q=0; q<n; q++)

void solve() {
  double x,s,r,t;
  int n;
  scanf("%lf %lf %lf %lf %d", &x, &s, &r, &t, &n);
  vector<pair<int, int> > data;
  int total = 0;
  FOR(q, n) {
    int b,e,w;
    scanf("%d %d %d", &b, &e, &w);
    data.push_back(make_pair(w, e - b));
    total += e - b;
  }
  assert(total <= x);
  data.push_back(make_pair(0, (int) x - total));
  sort(data.begin(), data.end());
  double res = 0;
  FOR(q, (int) data.size()) {
//    printf("speed %d dist %d\n", data[q].first, data[q].second);
    double tt = data[q].second / (data[q].first + r);
    tt = std::min(t, tt);
//    printf("use %lf run\n", tt);
    t -= tt;
    res += tt;
    double distance = data[q].second - tt * (data[q].first + r);
//    printf("remaining %lf walk \n", distance);
    res += distance / (data[q].first + s);
  }
  printf("%.9lf\n", res);
}

int main() {
  int t;
  scanf("%d", &t);
  FOR(q, t) {
    printf("Case #%d: ", q+1);
    solve();
//    printf("\n\n\n");
  }

}
