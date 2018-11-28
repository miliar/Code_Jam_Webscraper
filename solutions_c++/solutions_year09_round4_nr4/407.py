#include <iostream>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <cstdio>

using namespace std;
int N;
int x[4], y[4], r[4];

double dist(int x, int y, int p, int q) {
  int sqr = (x-p) * (x-p) + (y-q) * (y-q);
  return sqrt(sqr);
}

int main() {
  int numcase;
  cin >> numcase;
  for (int ncase = 1; ncase <= numcase; ++ncase) {
    cin >> N;
    for (int i = 0; i < N; ++i) {
      cin >> x[i] >> y[i] >> r[i];
    }

    double ans = 0;
    if (N == 1) {
      ans = r[0];
    } else if (N == 2) {
      ans = max(r[0], r[1]);
    } else {
      assert(N == 3);
      ans = 1000000000;
      for (int i = 0; i < N; ++i) {
	for (int j = i+1; j < N; ++j) {
	  // place one sprinkler between plants[i] and plants[j]
	  double totalDist = r[i] + r[j] + dist(x[i], y[i], x[j], y[j]);
	  int idx = 0;
	  for (; idx < N; ++idx) {
	    if (idx != i && idx != j) 
	      break;
	  }
	  ans = min(ans, max((double)r[idx], totalDist/2.0));
	}
      }
    }
    cout << "Case #" << ncase << ": ";
    printf("%.6f\n", ans);
  }
}
