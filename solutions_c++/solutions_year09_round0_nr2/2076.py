#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

using namespace std;

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define	MIN(a, b)	((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))

//#define small

#ifdef small
	#define	FILE_IN		"B-small.in"
	#define FILE_OUT	"B-small.out"
#endif
#ifndef small
	#define	FILE_IN		"B-large.in"
	#define FILE_OUT	"B-large.out"
#endif

int dr [4] = {-1, 0, 0, 1} ;
int dc [4] = {0, -1, 1, 0} ;

int nr, nc, numComp ;
int t [105] [105], w [105] [105] ;
bool vis [105] [105] ;
char m [30] ;

bool can(int way, int cr, int cc, int &xr, int &xc) {
  xr = cr + dr [way] ; xc = cc + dc [way] ;
  return (xr >= 0 && xr < nr && xc >= 0 && xc < nc) ;
}
	ifstream in(FILE_IN) ;
	ofstream out(FILE_OUT) ;


int dfs(int cr, int cc) {
  if (vis [cr] [cc]) return w [cr] [cc] ;
  
  vis [cr] [cc] = true ;
  int nextr = -1, nextc = -1, minNext = -1 ;
  int xr, xc ;
  for (int way = 0 ; way < 4 ; way ++) {
    if (can(way, cr, cc, xr, xc)) {
      if (minNext == -1 || minNext > t [xr] [xc]) {
        nextr = xr ;
        nextc = xc ;
        minNext = t [xr] [xc] ;
      }
    }
  }
  if (minNext == -1 || minNext >= t [cr] [cc]) {
    w [cr] [cc] = numComp ++ ;    
  }
  else {
    w [cr] [cc] = dfs(nextr, nextc) ;
  }
    
  return w [cr] [cc] ;
}

int main(int argc, char **argv) {

  int numTest ;
  in >> numTest ;
  for (int test = 1 ; test <= numTest ; test ++) {
    in >> nr >> nc ;
    numComp = 0 ;    
    for (int r = 0 ; r < nr ; r ++)
      for (int c = 0 ; c < nc ; c ++) { 
        in >> t [r] [c] ; 
        vis [r] [c] = false ;
      
      }
        
//    memset(vis, false, sizeof(vis)) ;
    for (int r = 0 ; r < nr ; r ++)
      for (int c = 0 ; c < nc ; c ++)
        if (!vis [r] [c]) dfs(r, c) ;

    char ch = 'a' ;
    memset(m, 0, sizeof(m)) ;
    for (int r = 0 ; r < nr ; r ++)
      for (int c = 0 ; c < nc ; c ++)
        if (m [w [r] [c]] == 0) {
          m [w [r] [c]] = ch ++ ;
        }
    
    out << "Case #" << test << ": " << endl ;			
    for (int r = 0 ; r < nr ; r ++) {
      for (int c = 0 ; c < nc ; c ++) 
        if (c == 0) out << m [w [r] [c]] ;
        else out << " " << m [w [r] [c]] ;
      out << endl ;
    }
  }
	
	in.close() ;
	out.close() ;
}
