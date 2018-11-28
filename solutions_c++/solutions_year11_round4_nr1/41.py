#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

int main(void)
{
  int T; cin >> T;
  for (int test = 1; test <= T; test++) {
    double d, r, R, t; int N;
    cin >> d >> r >> R >> t >> N;
    vector < pair <double, double> > walkways(N);
    for (int i = 0; i < N; i++) {
      double B, E, w; cin >> B >> E >> w;
      walkways[i] = make_pair(w+r, E-B);
      d -= E-B;
    }
    walkways.push_back(make_pair(r, d));
    sort(walkways.begin(), walkways.end());
    double ans = 0;
    for (int i = 0; i <= N; i++) {
      double t_R = min(walkways[i].second / (walkways[i].first + R-r), t);
      ans += t_R;
      t -= t_R;
      double d_R = walkways[i].second - t_R * (walkways[i].first + R-r);
      ans += d_R / walkways[i].first;
    }
    printf("Case #%d: %.6lf\n", test, ans);
  }
}
