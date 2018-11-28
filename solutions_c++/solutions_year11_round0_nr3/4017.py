#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

const int mxn = 1010;
const int mxval = 1<<20;
const int inf = 1e9 + 1;

int n;
int niz[mxn];

int prev[mxval][2][2];
int now[mxval][2][2];

void solve(){
  scanf( "%d", &n );
  int s = 0;
  for( int i = 0; i < n; i++ ){
    scanf( "%d", &niz[i] );
    s ^= niz[i];
  }

  for( int bsum = 0; bsum < mxval; bsum++ ){
    prev[bsum][0][0] = prev[bsum][0][1] = prev[bsum][1][0] = prev[bsum][1][1] = -inf;
    if( (s^bsum) == bsum ) prev[bsum][1][1] = 0;
  }

  int i, bsum, uzeo1, uzeo2;
  for( i = n-1; i >= 0; i-- ){
    for( bsum = 0; bsum < (1<<20); bsum++ ){
      for( uzeo1 = 0; uzeo1 < 2; uzeo1++ ){
	for( uzeo2 = 0; uzeo2 < 2; uzeo2++ ){
	now[bsum][uzeo1][uzeo2] = max(
			   prev[bsum^niz[i]][1][uzeo2] + niz[i],
			   prev[bsum][uzeo1][1] 
			   );
	}
      }
    }
    memcpy( prev, now, sizeof(now) );
  }
  if( now[0][0][0] <= 0 ) printf( "NO\n" );
  else printf( "%d\n", now[0][0][0] );

}

int main(){
  int t;
  scanf( "%d", &t );
  for( int test = 1; test <= t; test++ ){
    printf( "Case #%d: ", test );
    solve();
  }
  return 0;
}
