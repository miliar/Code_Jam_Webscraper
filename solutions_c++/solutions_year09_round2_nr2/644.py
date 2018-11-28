#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <ctype.h>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

char a[200];

int main() {
  int N, i, j;
  string k;

  scanf("%d\n", &N );

  for ( i = 0; i < N; i++ ) {
    scanf("%s\n", a );
    k = string( a );
    if ( !next_permutation( k.begin(), k.end() ) ) {
      k += '0';
      sort( k.begin(), k.end() );
      for ( j = 0; j < k.length(); j++ ) {
	if ( k[j] != '0' ) {
	  k[0] = k[j];
	  k[j] = '0';
	  break;
	}
      }
    }
    printf("Case #%d: %s\n", i + 1, k.c_str() );
  }

  return 0;
}
