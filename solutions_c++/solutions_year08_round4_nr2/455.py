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

#define small

#ifdef small
	#define	FILE_IN		"B-small.in"
	#define FILE_OUT	"B-small.out"
#endif
#ifndef small
	#define	FILE_IN		"B-large.in"
	#define FILE_OUT	"B-large.out"
#endif

#define MAXM  10005
	ifstream in(FILE_IN) ;
	ofstream out(FILE_OUT) ;
	
int num_tests, test ;
LL N, M, A ;
LL xx0, yy0, xx1, yy1, xx2, yy2 ;

int main(int argc, char **argv) {
	in >> num_tests ;

	for (int test = 1 ; test <= num_tests ; test ++) {
    cout << test << " / " << num_tests << endl ;
    in >> N >> M >> A ;
		bool found = false ;		
    for (LL ix2 = 0 ; ix2 <= N && !found ; ix2 ++) {
      for (LL iy3 = 0 ; iy3 <= M && !found ; iy3 ++) {
        for (LL ix3 = 0 ; ix3 <= N && !found ; ix3 ++) {
          for (LL iy2 = 0 ; iy2 <= M && !found ; iy2 ++) {
            if (ix2 * iy3 - ix3 * iy2 == A) {
              found = true ;
              xx0 = 0 ; yy0 = 0 ;
              xx1 = ix2 ; yy1 = iy2 ;
              xx2 = ix3 ; yy2 = iy3 ;
            }      
          }
        }
      }
    }

    for (LL ix2 = 0 ; ix2 <= N && !found ; ix2 ++) {
      for (LL iy3 = 0 ; iy3 <= M && !found ; iy3 ++) {
        for (LL ix3 = 0 ; ix3 <= N && !found ; ix3 ++) {
          for (LL iy1 = 0 ; iy1 <= M && !found ; iy1 ++) {
            if (ix2 * iy3 - ix2 * iy1 + ix3 * iy1 == A) {
              found = true ;
              xx0 = 0 ; yy0 = iy1 ;
              xx1 = ix2 ; yy1 = 0 ;
              xx2 = ix3 ; yy2 = iy3 ;
            }      
          }
        }
      }
    }    
    if (!found) {
      out << "Case #" << test << ": " << "IMPOSSIBLE" << endl ;
    }
    else {
		  out << "Case #" << test << ": " << xx0 << " " << yy0 << " "<< xx1 << " "<< yy1 << " "<< xx2 << " " << yy2 << endl ;
    }
	}
	
	in.close() ;
	out.close() ;
}
