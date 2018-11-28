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

#if defined (__GNUC__) && (__GNUC__ <= 2)
#include <hash_map>
#include <hash_set>
#else
#include <ext/hash_map>
#include <ext/hash_set>
using namespace __gnu_cxx;
#endif
using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

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
	#define	FILE_IN		"A-small.in"
	#define FILE_OUT	"A-small.out"
#endif
#ifndef small
	#define	FILE_IN		"A-large.in"
	#define FILE_OUT	"A-large.out"
#endif

#define MAXM  10005
	ifstream in(FILE_IN) ;
	ofstream out(FILE_OUT) ;
	
int num_tests, test, M, value ;
int v [MAXM], d [MAXM] [2] ;
int g [MAXM], chg [MAXM] ;

int calc(int u, int value) {
  if (u >= M) return -1 ;
  int &ret = d [u] [value] ;
  if (ret != -1) return ret ;
  int ul = 2 * u + 1, ur = 2 * u + 2 ;
  if (ul >= M || ur >= M) return -1 ;

  int cl [2] = {calc(ul, 0), calc(ul, 1)} ;
  int cr [2] = {calc(ur, 0), calc(ur, 1)} ;

  for (int vl = 0 ; vl < 2 ; vl ++) {
    if (cl [vl] != -1) {
      for (int vr = 0 ; vr < 2 ; vr ++) {
        if (cr [vr] != -1) {          
          if (g [u] == 1) {
            if ((vl && vr) == value) {
              if (ret == -1 || ret > cl [vl] + cr [vr]) 
                ret = cl [vl] + cr [vr] ;
            } 
            if ((vl || vr) == value && chg [u] == 1) {
              if (ret == -1 || ret > cl [vl] + cr [vr] + 1) 
                ret = cl [vl] + cr [vr] + 1 ;
            }                          
          }
          else {
            if ((vl || vr) == value) {
              if (ret == -1 || ret > cl [vl] + cr [vr]) 
                ret = cl [vl] + cr [vr] ;
            } 
            if ((vl && vr) == value && chg [u] == 1) {
              if (ret == -1 || ret > cl [vl] + cr [vr] + 1) 
                ret = cl [vl] + cr [vr] + 1 ;
            }  
          }
        }
      }
    }
  }
  return ret ;
}

int main(int argc, char **argv) {
	in >> num_tests ;
	for (int test = 1 ; test <= num_tests ; test ++) {
		in >> M >> value ;
		for (int i = 0 ; i < M ; i ++) {
      chg [i] = 1 ;
      g [i] = 1 ;
      v [i] = -1 ;
      d [i] [0] = -1 ;
      d [i] [1] = -1 ;
    }
        
		for (int i = 0 ; i < (M - 1) / 2 ; i ++) {
      in >> g [i] >> chg [i] ;
    }
    for (int i = (M - 1) / 2 ; i < M ; i ++) {
      in >> v [i] ;
      d [i] [v [i]] = 0 ;
    }
    
    int res = calc(0, value) ;
    if (res == -1) {
      out << "Case #" << test << ": " << "IMPOSSIBLE" << endl ;
    }
    else {
		  out << "Case #" << test << ": " << calc(0, value) << endl ;
    }
	}
	
	in.close() ;
	out.close() ;
}
