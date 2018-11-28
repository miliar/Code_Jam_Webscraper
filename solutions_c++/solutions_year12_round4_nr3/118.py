#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std ;
int hseen[2000] ;
long long r[2000] ;
int main(int argc, char *argv[]) {
  int kase = 0 ;
  int kases = 0 ;
  scanf("%d", &kases) ;
  for (int kase=1; kase<=kases; kase++) {
    int N ;
    scanf("%d", &N) ;
    for (int i=0; i+1<N; i++) {
      int v ;
      scanf("%d", &v) ;
      hseen[i] = v-1 ;
    }
    for (int i=0; i<N; i++)
      r[i] = 0 ;
    int impossible = 0 ;
    while (!impossible) {
      int changed = 0 ;
      for (int i=0; i+1<N; i++) {
	long long pk = r[hseen[i]] ;
	for (int j=i+1; j<N; j++)
	  if (j != hseen[i]) {
	    long long t = r[i]+((r[j]-r[i])*(hseen[i]-i)+j-i)/(j-i) ;
	    if (t > pk)
	      pk = t ;
	  }
	if (pk > 1000000000)
	  impossible = 1 ;
	if (pk > r[hseen[i]]) {
	  r[hseen[i]] = pk ;
	  changed++ ;
	}
      }
      if (changed == 0 || impossible)
	break ;
    }
    cout << "Case #" << kase << ":" ;
    if (impossible)
      cout << " Impossible" ;
    else
      for (int i=0; i<N; i++)
	cout << " " << r[i] ;
    cout << endl ;
  }
}
