#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VII;
typedef vector<string> VS;

#define ABS(x) ((x)<0? -(x):(x))
#define ALL(x) x.begin(),x.end()
#define SIZE(x)  int((x).size())
#define PB push_back
#define REP( a, b ) for ( int a = 0; a < b; a++ )
#define TR(x,it)  for(typeof((x).begin()) it=(x).begin(); it!=(x).end(); it++)

VI Split( string s, string c )
{
  VI ret;
  for( int i=0, n; i <= s.length(); i=n+1 ){
    n = s.find_first_of( c, i );
    if( n == string::npos ) n = s.length();
    string tmp = s.substr( i, n-i );
    if ( tmp.size() ) 
      ret.push_back(atoi(tmp.c_str())-1);
  }
  return ret;
}

int count( VI a, int c )
{
  int ret = 0;
  for ( int i = c-1; i >= 0; i-- ) {
    if ( a[i] == 0 ) break;
    ret ++;
  }
  for ( int i = c+1; i < SIZE(a); i++ ) {
    if ( a[i] == 0 ) break;
    ret ++;
  }
  return ret;
}

int getnum( VI m, int N )
{
  int low = 1<<30;
  sort(ALL(m));
  do { 
    int res = 0;
    VI a(N,1);
    REP( i, SIZE(m) ) {
      int c = m[i];
      a[c] = 0;
      res += count( a, c );
    }
    if ( res < low ) 
      low = res;
  } while( next_permutation(ALL(m)) );

  return low;
}

int main( int argc, char *argv[] )
{
  FILE *fp;
  int N;

  fp = fopen( argv[1], "rb" );
  fscanf( fp, "%d\n", &N );
  {
    for ( int i = 1; i <= N; i ++ ) {
      char buff[1000];
      int x,y;
      fscanf( fp, "%d  %d\n", &y,&x );
      fgets( buff,1000,fp );
      string line = string(buff);
      VI l = Split( line, " " );
      printf("Case #%d: %d\n",i,getnum(l,y));
    }

  }
  fclose(fp);
  return 0;
}


// Powered by FileEdit
// Powered by TZTester 1.01 [25-Feb-2003]
// Powered by CodeProcessor
