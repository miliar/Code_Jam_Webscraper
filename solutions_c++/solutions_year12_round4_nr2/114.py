#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std ;
int r[1000] ;
int o[1000], oi[1000] ;
int x[1000], y[1000] ;
long long s(long long v) {
  return v*v ;
}
long long d2(long long x, long long y) {
  return x*x+y*y ;
}
int check(int ii, int xt, int yt) {
  for (int i=0; i<ii; i++) {
    if (d2(xt-x[o[i]],yt-y[o[i]]) < s(r[o[i]]+r[o[ii]]))
      return 0 ;
  }
  return 1 ;
}
int main(int argc, char *argv[]) {
  int kase = 0 ;
  int kases = 0 ;
  srand48(1000) ;
  scanf("%d", &kases) ;
  for (int kase=1; kase<=kases; kase++) {
    int N, W, L ;
    scanf("%d %d %d", &N, &W, &L) ;
    for (int i=0; i<N; i++) {
      scanf("%d", r+i) ;
      o[i] = i ;
    }
    for (int i=0; i<N; i++)
      for (int j=i+1; j<N; j++)
	if (r[o[i]] < r[o[j]])
	  swap(o[i], o[j]) ;
    for (int i=0; i<N; i++)
      oi[o[i]] = i ;
    int failed = -1 ;
    while (1) {
      for (int i=0; i<N; i++) {
	// try random placements; pick one closest to origin.
	// restart if we don't succeed after some number of tries
	int c1 = o[i] ;
	int bestx = -1, besty = -1, bestd ;
	for (int j=0; j<1000; j++) {
	  int x1 = (int)((W+1)*drand48()) ;
	  int y1 = (int)((L+1)*drand48()) ;
	  if (bestx >= 0 && d2(x1, y1) >= bestd)
	    continue ;
	  //	  cout << "Trying " << x1 << " " << y1 << endl ;
	  if (check(i, x1, y1)) {
	    //	    cout << "Good placement" << endl ;
	    bestx = x1 ;
	    besty = y1 ;
	    bestd = d2(x1, y1) ;
	    break ;
	  }
	}
	if (bestx < 0) {
	  failed = i ;
	  break ;
	}
	int dec = 1024 ;
	while (dec > 0) {
	  if (bestx - dec >= 0 && check(i, bestx-dec, besty))
	    bestx -= dec ;
	  if (besty - dec >= 0 && check(i, bestx, besty-dec))
	    besty -= dec ;
	  dec >>= 1 ;
	}
	//	cout << "Placing " << i << " r " << r[o[i]] << " at " << bestx << " " << besty << endl ;
	x[o[i]] = bestx ;
	y[o[i]] = besty ;
      }
      if (failed == -1)
	break ;
    }
    cout << "Case #" << kase << ":" ;
    for (int i=0; i<N; i++)
      cout << " " << x[i] << " " << y[i] ;
    cout << endl ;
  }
}
