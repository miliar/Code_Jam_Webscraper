#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <stdio.h>
#include <set>
#include <assert.h>
using namespace std;
double dp[1001];
long double derange[23] = {1, 0, 1, 2, 9, 44, 265, 1854, 14833, 133496, 1334961, 14684570, 176214841, 2290792932,
		      32071101049.0L, 481066515734.0L, 7697064251745.0L, 130850092279664.0L, 2355301661033953.0L, 
44750731559645106.0L, 895014631192902121.0L, 18795307255050944540.0L};
long double E = 2.718281828459045235360287471352662497757247093699959574966L;
double factorial[23];
inline long double f(int m, int t) {
  // return !t/(t! * (m-t)!)
  if (t >= 23) return 0;
  double ret;
  if (m-t < 23)
    ret = derange[m-t] / factorial[m-t];
  else
    ret = 1. / E;
  return ret / factorial[t];
}
double go(int x) {
  if (x == 0)
    return 0;
  double &ret = dp[x];
  if (ret > -.5)
    return ret;
  ret = 1;
  for (int y = 0; y < x; ++y)
    ret += f(x, x - y)*go(y);
  ret /= 1. - f(x, 0);
  return ret;
}
int main() {
  memset(dp, -1, sizeof(dp));
  int nocases;
  cin >> nocases;
  factorial[0] = 1;
  for (int i = 1; i < 23; ++i)
    factorial[i] = 1.*i * factorial[i-1];
  for (int rr = 1; rr <= nocases; ++rr) {
    int n;
    vector<int> w, v;
    cin >> n;
    for (int i = 0; i < n; ++i) {
      int t;
      cin >> t;
      w.push_back(t);
      v.push_back(t);
    }
    sort(w.begin(), w.end());
    int e = 0;
    for (int i = 0; i < w.size(); ++i)
      if (w[i] != v[i])
	++e;
    printf("Case #%d: %.6lf\n", rr, go(e));
  }
  return 0;
}
