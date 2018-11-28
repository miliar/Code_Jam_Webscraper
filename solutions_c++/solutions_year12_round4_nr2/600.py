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
double LengthSq(double a, double b) { return a*a+b*b; }
int main() {
  srand(628);
  int nocases, t;
  int x[1000], y[1000], xx[1000], yy[1000];
  cin >> nocases;
  for (int rr = 1; rr <= nocases; ++rr) {
    int N, W, L;
    cin >> N >> W >> L;
    vector< pair<int, int> > r;
    for (int i = 0; i < N; ++i) {
      cin >> t;
      r.push_back(make_pair(t, i));
    }
    if (N == 1)
      printf("Case #%d: 0 0\n", rr);
    else if (N == 2)
      printf("Case #%d: 0 0 %d %d\n", rr, W, L);
    else {
      sort(r.begin(), r.end());
      reverse(r.begin(), r.end());
      while (1) {
	x[0] = 0, y[0] = 0;
	x[1] = W, y[1] = L;
	for (int i = 2; i < N; ++i) {
	  int q = 0;
	  int X, Y;
	  for (;q<20;++q) {
	    X = rand()%(W+1), Y = rand()%(L+1);
	    //	    X = int(X)/2 + (X>W&&X+.5<=W)*.5, Y = int(Y)/2 + (Y>L&&Y+.5<=L)*.5;
	    bool bad = false;
	    for (int j = 0; j < i; ++j) {
	      double d2 = LengthSq(x[j]-X,y[j]-Y);
	      if (d2<(1LL*r[i].first+r[j].first)*(1LL*r[i].first+r[j].first)) {
		bad = true;
		break;	      
	      }
	    }
	    if (!bad) {
	      x[i] = X, y[i] = Y;
	      break;
	    }
	  }
	  if (q == 20)
	    goto fail;
	}
	for (int i = 0; i < N; ++i)
	  xx[r[i].second] = x[i], yy[r[i].second] = y[i];
	printf("Case #%d:", rr);
	for (int i = 0; i < N; ++i)
	  printf(" %d %d", xx[i], yy[i]);
	cout << endl;
	break;
      fail:
	;
      }
    }
  }
  return 0;
}
