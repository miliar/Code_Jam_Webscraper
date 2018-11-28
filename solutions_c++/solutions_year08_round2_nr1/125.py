#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;
int main() {
  int no_cases;
  cin >> no_cases;
  for (int rr = 1; rr <= no_cases; ++rr) {
    long long no_type[3][3], ret = 0, r2 = 0, n, A, B, C, D, x0, y0, M;
    memset(no_type, 0, sizeof(no_type));
    vector< pair<long long, long long> > points;
    cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
    long long X = x0, Y = y0;
    points.push_back(make_pair(X, Y));
    for (int i = 1; i < n; ++i) {
      X = (A*X + B) % M;
      Y = (C*Y + D) % M;
      points.push_back(make_pair(X, Y));
    }
    sort(points.begin(), points.end());
    points.erase(unique(points.begin(), points.end()), points.end());
    for (int i = 0; i < points.size(); ++i)
      no_type[points[i].first%3][points[i].second%3]++;

    for (int x1 = 0; x1 < 3; ++x1)
      for (int y1 = 0; y1 < 3; ++y1)
	if (no_type[x1][y1] >= 3)
	  ret += no_type[x1][y1]*(no_type[x1][y1]-1)*(no_type[x1][y1]-2) / 6;

    for (int x1 = 0; x1 < 3; ++x1)
      for (int y1 = 0; y1 < 3; ++y1)
	for (int x2 = 0; x2 < 3; ++x2)
	  for (int y2 = 0; y2 < 3; ++y2)
	    if ((x1!=x2) || (y1!=y2))
	      if (((x1+x2+x2) % 3 == 0) &&
		  ((y1+y2+y2) % 3 == 0))
		ret += no_type[x1][y1]*no_type[x2][y2]*(no_type[x2][y2]-1) / 2;

    for (int x1 = 0; x1 < 3; ++x1)
      for (int y1 = 0; y1 < 3; ++y1)
	for (int x2 = 0; x2 < 3; ++x2)
	  for (int y2 = 0; y2 < 3; ++y2)
	    for (int x3 = 0; x3 < 3; ++x3)
	      for (int y3 = 0; y3 < 3; ++y3)
		if (((x1+x2+x3) % 3 == 0) &&
		    ((y1+y2+y3) % 3 == 0)) {
		  set< pair< long long, long long > > S;
		  S.insert(make_pair(x1, y1));
		  S.insert(make_pair(x2, y2));
		  S.insert(make_pair(x3, y3));
		  if (S.size() == 3)
		    r2 += no_type[x1][y1] * no_type[x2][y2] * no_type[x3][y3];
		}
    ret += r2 / 6;
    printf("Case #%d: %lld\n", rr, ret);
  }
  return 0;
}
