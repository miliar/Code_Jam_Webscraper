#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int main() {
  int T;
  cin >> T;
  for(int tc = 1; tc <= T; ++tc) {
    int X, S, R, N;
    double t;
    vector< pair<int, int> > v;
    cin >> X >> S >> R >> t >> N;
    int be = 0;
    for(int i = 0; i < N; ++i) {
      int s, e, w;
      cin >> s >> e >> w;
      if(be != s) {
	v.push_back(make_pair(0, s-be));
      }
      v.push_back(make_pair(w, e-s));
      if(i+1 == N && e != X)
	v.push_back(make_pair(0, X-e));
      be = e;
    }
    sort(v.begin(), v.end());
    double ans = 0;
    for(int i = 0; i < v.size(); ++i) {
      double d1, d2;
      d1 = (v[i].first+R)*t;
      d2 = v[i].second;
      if(d1 < d2) {
	ans += t + (d2-d1)/(v[i].first+S);
	t = 0;
      } else {
	double tmp = d2/(v[i].first+R);
	ans += tmp;
	t -= tmp;
      }
    }
    printf("Case #%d: %.9f\n", tc, ans);
  }
  return 0;
}
