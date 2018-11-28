#include <iostream>
#include <string.h>
#include <cstdlib>
using namespace std ;
char mline[1000] ;
long long a[1000] ;
int main(int argc, char *argv[]) {
  fgets(mline, 1000, stdin) ;
  int T = atol(mline) ;
  for (int c=1; c<=T; c++) {
    fgets(mline, 1000, stdin) ;
    int N = atol(mline) ;
    for (int i=0; i<N; i++) {
      fgets(mline, 1000, stdin) ;
      long long v = 0 ;
      for (int j=0; j<N; j++) {
	if (mline[j] == '1')
	  v |= (1LL << (N-j-1)) ;
      }
      a[i] = v ;
    }
    int r = 0 ;
    for (int i=0; i<N; i++) {
      long long m = (1LL << (N - i - 1)) - 1 ;
      int j = i ;
      while (a[j] & m)
	j++ ;
      while (j > i) {
	swap(a[j], a[j-1]) ;
	r++ ;
	j-- ;
      }
    }
    cout << "Case #" << c << ": " << r << endl ;
  }
}
