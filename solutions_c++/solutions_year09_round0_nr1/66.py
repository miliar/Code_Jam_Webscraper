#include <iostream>
#include <string.h>
using namespace std ;
int bm[15][26][1024] ;
char lin[15000] ;
int main(int argc, char *argv[]) {
  int L, D, N ;
  fgets(lin, 15000, stdin) ;
  sscanf(lin, "%d %d %d", &L, &D, &N) ;
  for (int i=0; i<D; i++) {
    fgets(lin, 15000, stdin) ;
    for (int j=0; j<L; j++)
      bm[j][lin[j]-'a'][i>>5] |= 1<<(i&31) ;
  }
  for (int i=0; i<N; i++) {
    int b[1024] ;
    int c[1024] ;
    memset(b, -1, sizeof(b)) ;
    fgets(lin, 15000, stdin) ;
    int p = 0 ;
    for (int j=0; j<L; j++) {
      memset(c, 0, sizeof(c)) ;
      if (lin[p] == '(') {
	p++ ;
	while (lin[p] != ')') {
	  for (int k=0; k<1024; k++)
	    c[k] |= bm[j][lin[p]-'a'][k] ;
	  p++ ;
	}
	p++ ;
      } else {
	memcpy(c, bm[j][lin[p]-'a'], sizeof(c)) ;
	p++ ;
      }
      for (int k=0; k<1024; k++)
	b[k] &= c[k] ;
    }
    int r = 0 ;
    for (int j=0; j<1024; j++) {
      int t = b[j] ;
      while (t) {
	r++ ;
	t &= t-1 ;
      }
    }
    cout << "Case #" << (i+1) << ": " << r << endl ;
  }
}
