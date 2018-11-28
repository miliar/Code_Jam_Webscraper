#include <cstdio>
#include <algorithm>

using namespace std;

typedef pair<int,int> par;

const int mxn = 1000;
par niz[mxn];
int n;

bool sjeku( int i, int j ){
  if( niz[j].second > niz[i].second ){
    return niz[j].first < niz[i].first;
  }

  return niz[j].first > niz[i].first;
}

int solve(){
  scanf( "%d", &n );
  for( int i = 0; i < n; i++ )
    scanf( "%d %d", &niz[i].first, &niz[i].second );
  int sol = 0;
  for( int i = 0; i < n; i++ )
    for( int j = i+1; j < n; j++ )
      if( sjeku(i,j) ) sol++;
  return sol;
}

int main(){
  int t;
  scanf( "%d", &t );
  for( int T = 1; T <= t; T++ )
    printf( "Case #%d: %d\n", T, solve() );
  return 0;
}
