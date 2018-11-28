#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;
const int MAXL = 1000;
const int MAXK = 6;

char S[MAXL+1];
int n, k;

int P[MAXK];

int main()
{
  int t; scanf( "%d", &t );
  for( int t_case = 0; t_case < t; ++t_case ) {
    scanf( "%d%s", &k, S );
    n = strlen( S );

    for( int i = 0; i < k; ++i ) 
      P[i] = i;

    int sol = MAXL;
    for( ; ; ) {
      int cnt = 0;
      int z = -1;
      for( int i = 0; k * i < n; ++i ) {
	for( int j = 0; j < k; ++j ) {
	  if ( S[i*k+P[j]] != z )
	    ++cnt;
	  z = S[i*k+P[j]];
	}
      }
      
      sol = min( sol, cnt );
      if ( !next_permutation( P, P + k ) ) break;
    }
    printf( "Case #%d: %d\n", t_case + 1, sol );
  }
  return 0;
}
