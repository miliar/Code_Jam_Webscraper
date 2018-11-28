#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

const int mxn = (1e8)+5;
char sol[mxn]; int sto = -1;

void calc( int n ){
  if( n == sto ) return;
  sto = n;

  int state = 0;
  sol[0] = 0;
  for( int i = 0; i < mxn-1; i++ ){
    int j;
    for( j = 0; j < n; j++ )
      if( (state&(1<<j)) == 0 ) break;
    
    if( j == n ) state ^= ((1<<(j))-1);
    else state ^= ((1<<(j+1))-1);

    if( state == (1<<n)-1 ) sol[i+1] = 1;
    else sol[i+1] = 0;
  }
}

int ispis[10000];
int main(){
  int T;
  scanf( "%d", &T );
  vector < pair< pair <int,int> , int > > niz;
  for( int id = 0; id < T; id++ ){
    int n, k;
    scanf( "%d %d", &n, &k );
    niz.push_back( make_pair(make_pair(n,k),id) );
  }
  sort( niz.begin(), niz.end() );

  
  for( int i = 0; i < T; i++ ){
    calc(niz[i].first.first);
    ispis[niz[i].second] = sol[niz[i].first.second];
  }

  for( int i = 0; i < T; i++ ){
    printf( "Case #%d: ", i+1 );
    if( ispis[i] ) printf( "ON\n" );
    else printf( "OFF\n" );
  }

  return 0;
}
