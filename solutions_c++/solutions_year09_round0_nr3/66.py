#include <iostream>
#include <string.h>
#include <map>
using namespace std ;
char lin[15000] ;
char *match = "welcome to code jam" ;
int a[32][1000] ;
int main(int argc, char *argv[]) {
  int N ;
  fgets(lin, 15000, stdin) ;
  sscanf(lin, "%d", &N) ;
  for (int i=0; i<N; i++) {
    memset(a, 0, sizeof(a)) ;
    a[0][0] = 1 ;
    for (int k=0; k<1000; k++)
      a[0][k] = 1 ;
    fgets(lin, 15000, stdin) ;
    int v = 0 ;
    for (int j=0; lin[j] > 0; j++) {
      for (int k=0; match[k] >= ' '; k++) {
	a[k+1][j+1] = a[k+1][j] ;
	if (lin[j] == match[k])
	  a[k+1][j+1] = (a[k+1][j]+a[k][j]) % 10000 ;
      }
      v = a[strlen(match)][j+1] ;
    }
    cout << "Case #" << (i+1) << ": " ;
    if (v < 1000) cout << "0" ;
    if (v < 100) cout << "0" ;
    if (v < 10) cout << "0" ;
    cout << v << endl ;
  }
}
