#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

const int mxn = 520;
const int mxm = mxn*4;
typedef pair<int,int> par;

int polje[mxn][mxm];
int n, m;
char temp[mxn];
int DP[mxn][mxm];
int next[mxn][mxm];

inline int tobin( const char x ){
  if( x <= '9' && x >= '0' ) return x-'0';
  return x-'A'+10;  
}

inline int min( const int a, const int b, const int c ){
  return min(min(a,b),c);
}

void precompute(){
  memset( DP, 0, sizeof(DP) );
  for( int i = 0; i < n; i++ ){
    for( int j = 0; j < m; j=next[i][j] ){
      if( polje[i][j] == 2 ) continue;
      if( polje[i][j] == polje[i-1][j-1] && polje[i][j-1] == polje[i-1][j] && polje[i][j] != polje[i-1][j] )
	DP[i][j] = min(DP[i-1][j-1],DP[i-1][j],DP[i][j-1])+1;
      else DP[i][j] = 1;
    }
  }
}

void output(){
  for( int i = 0; i < n; i++, printf( "\n" ) )
    for( int j = 0; j < m; j++ )
      printf( "%d", polje[i][j] );
  printf("\n");
}

int najveci(){
  precompute();

  int mx = 0;
  for( int i = 0; i < n; i++ )
    for( int j = 0; j < m; j=next[i][j] )
      if( DP[i][j] > mx ) mx = DP[i][j];


  for( int i = 0; i < n; i++ ){
    for( int j = 0; j < m; j=next[i][j] ){
      if( DP[i][j] == mx ){
	for( int r1 = i-mx+1; r1 <= i; r1++ ){
	  next[r1][j-mx] = j+1;
	  for( int s1 = j-mx+1; s1 <= j; s1++ )
	    polje[r1][s1] = 2;
	}
	//	output();
	return mx;
      }
    }
  }

  return mx;
}

void solve(){
  scanf( "%d %d", &n, &m );
  for( int i = 0; i < n; i++ ){
    scanf( "%s", temp );
    for( int j = 0; j < m/4; j++ ){
      int mask = tobin(temp[j]);
      for( int koja = 3; koja >= 0; koja-- ){
	if( mask&(1<<koja) ) polje[i+1][j*4+3-koja+1] = 0;
	else polje[i+1][j*4+3-koja+1] = 1;
      }
    }
    polje[i+1][0] = polje[i+1][m+1] = 2;
  }
  n += 2;
  m += 2;

  for( int i = 0; i < n; i++ )
    for( int j = 0; j < m; j++ )
      next[i][j] = j+1;

  for( int i = 0; i < m; i++ )
    polje[0][i] = polje[n-1][i] = 2;


  int sol = 0;
  vector <int> vel;
  int mx = 0;
  for( mx = najveci(); mx > 1; mx = najveci() )
    vel.push_back(mx);
  if( mx == 1 ){
    vel.push_back(mx);
    for( int i = 0; i < n; i++ )
      for( int j = 0; j < m; j++ )
	if( polje[i][j] != 2 ) vel.push_back(1);
    vel.push_back(0);
  } else vel.push_back(0);
  for( int i = 0; i < (int)vel.size()-1; i++ )
    if( vel[i] != vel[i+1] ) sol++;

  printf( "%d\n", sol );
  int kol = 0;
  for( int i = 0; i < (int)vel.size()-1; i++ ){
    kol++;
    if( vel[i] != vel[i+1] ){
      printf( "%d %d\n", vel[i], kol );
      kol = 0;
    }
  }

}

int main(){
  int t;
  scanf( "%d", &t );
  for( int T = 1; T <= t; T++ ){
    printf( "Case #%d: ", T );
    solve();
    fprintf( stderr, "T %d\n", T );
  }

  return 0;
}
