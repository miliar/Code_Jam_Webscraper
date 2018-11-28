#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std ;
int d[10000], el[10000], re[10000], oldre[10000] ;
int cntb[10000], cntf[10000] ;
int main(int argc, char *argv[]) {
  int kase = 0 ;
  int kases = 0 ;
  scanf("%d", &kases) ;
  for (int kase=1; kase<=kases; kase++) {
    int N ;
    scanf("%d", &N) ;
    for (int i=0; i<N; i++) {
      int d_, el_ ;
      scanf("%d %d", &d_, &el_) ;
      d[i] = d_ ;
      el[i] = el_ ;
      re[i] = 0 ;
      oldre[i] = 0 ;
      cntb[i] = cntf[i] = 1 ;
    }
    int D ;
    scanf("%d", &D) ;
    re[0] = d[0] ;
    int good = 0 ;
    while (1) {
      int changed = 0 ;
      for (int i=0; i<N; i++) {
	if (re[i] > oldre[i]) {
	  //	  cout << "Changed " << i << endl ;
	  if (re[i] + d[i] >= D) {
	    good = 1 ;
	    break ;
	  }
	  while (1) {
	    int c = i - cntb[i] ;
	    if (c >= 0 && d[i] - d[c] <= re[i]) {
	      cntb[i]++ ;
	      int newlen = d[i] - d[c] ;
	      //	      cout << "Now " << i << " can reach " << c << " at " << newlen << endl ;
	      if (newlen > el[c])
		newlen = el[c] ;
	      if (newlen > re[c]) {
		re[c] = newlen ;
		changed++ ;
	      }
	    } else {
	      break ;
	    }
	  }
	  while (1) {
	    int c = i + cntf[i] ;
	    if (c < N && d[c] - d[i] <= re[i]) {
	      cntf[i]++ ;
	      int newlen = d[c] - d[i] ;
	      //	      cout << "Now " << i << " can reach " << c << " at " << newlen << endl ;
	      if (newlen > el[c])
		newlen = el[c] ;
	      if (newlen > re[c]) {
		re[c] = newlen ;
		changed++ ;
	      }
	    } else {
	      break ;
	    }
	  }
	  oldre[i] = re[i] ;
	}
      }
      if (!changed || good)
	break ;
    }
    cout << "Case #" << kase << ": " << (good ? "YES" : "NO") << endl ;
  }
}
