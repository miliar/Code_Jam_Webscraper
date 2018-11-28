#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

double solve() {
  int X, S, R, N, tot = 0;
  double t;

  vector<pair<int, double> > vec;
  cin >> X >> S >> R >> t >> N;
  for (int i = 0; i < N; ++i) {
    int b, e, w;
    cin >> b >> e >> w;
    vec.push_back(make_pair(w, e-b));
    tot += e - b;
  }
  vec.push_back(make_pair(0, X - tot));
  sort(vec.begin(), vec.end());
  double ans = 0;
  for (int i = 0; i < vec.size(); ++i) {
    if (t > 0) { // still run
      double u = min<double>(t * (vec[i].first + R), vec[i].second);
      double dt = u / (vec[i].first + R);
      ans += dt;
      vec[i].second -= u;
      t -= dt;
    }
    ans += vec[i].second / (double)(vec[i].first + S);
  }
  return ans;
}

int main() {
  freopen("input.txt" , "r", stdin);
  int T;
  cin >> T;
  for (int tc = 1; tc <= T; ++tc) {
    printf("Case #%d: %.9f\n", tc, solve());
  }
}
