#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

const int mxn = 110;

int n;
int x[mxn];
int who[mxn];
int next[mxn][2];
int dest[mxn][2];

int mem[mxn][mxn][mxn];

int f( int x1, int x2, int i ){
  int &ref = mem[x1][x2][i];
  if( ref != -1 ) return ref;

  //  printf( "%d %d %d\n", x1, x2, i );
  //  if( x1 > 5 ) return 0;
  if( i == n ) return 0;

  if( i == 2 ) {
    //    printf( "%d %d\n", x[i], who[i] );
  }
  if( x[i] == x1 && who[i] == 0 ){
    if( next[i][1] && dest[i][1] != x2 ) return ref = f( x1, x2+next[i][1], i+1 ) + 1;
    return ref = f( x1, x2, i+1 ) + 1;
  }
  if( x[i] == x2 && who[i] == 1 ){
    if( next[i][0] && dest[i][0] != x1 ) return ref = f( x1+next[i][0], x2, i+1 ) + 1;
    return ref = f( x1, x2, i+1 ) + 1;
  }

  int ret = 10000000;
  int delta1 = next[i][0], delta2 = next[i][1];
  if( dest[i][0] == x1 ) delta1 = 0;
  if( dest[i][1] == x2 ) delta2 = 0;

  ret = f( x1+delta1, x2+delta2, i );
  if( next[i][0] && dest[i][0] != x1 ) ret = min(ret, f( x1+next[i][0], x2, i ) );
  if( next[i][1] && dest[i][1] != x2 ) ret = min(ret, f( x1, x2+next[i][1], i ) );

  return ref = ret + 1;
}

void solve(){
  memset( next, 0, sizeof(next) );
  memset( dest, 0, sizeof(dest) );
  memset( mem, -1, sizeof(mem) );

  scanf( "%d", &n );
  for( int i = 0; i < n; i++ ){
    int X, koji;
    char temp[5];
    scanf( "%s %d", temp, &X );
    X--;

    if( temp[0] == 'O' ) koji = 0;
    else koji = 1;

    int prev = 0;
    dest[i][koji] = X;
    for( int j = i-1; j >= 0; j-- ){
      if( who[j] == koji ){
	prev = x[j];
	break;
      }
      dest[j][koji] = X;
    }

    for( int j = i+1; j < n; j++ )
      dest[j][koji] = X;

    for( int j = i; j >= 0; j-- ){
      if( j != i && who[j] == koji )
	break;
      if( prev < X ) next[j][koji] = 1;
      else if( prev > X ) next[j][koji] = -1;
    }
    

    who[i] = koji;
    x[i] = X;
  }

  printf( "%d\n", f(0,0,0) );
}

int main(){
  int t;
  scanf( "%d", &t );
  for( int i = 0; i < t; i++ ){
    printf( "Case #%d: ", i+1 );
    solve();
  }
  return 0;
}
