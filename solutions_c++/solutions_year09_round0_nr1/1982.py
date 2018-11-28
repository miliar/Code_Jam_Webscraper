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

#define eps 1e-9
#define gr(a, b) ((a) > (b) + eps)
#define ge(a, b) ((a) > (b) - eps)
#define le(a, b) ((a) < (b) + eps)
#define ls(a, b) ((a) < (b) - eps)
#define eq(a, b) ((a) > (b) - eps && (a) < (b) + eps) 


//#define small

#ifdef small
	#define	FILE_IN		"A-small.in"
	#define FILE_OUT	"A-small.out"
#endif
#ifndef small
	#define	FILE_IN		"A-large.in"
	#define FILE_OUT	"A-large.out"
#endif

int L, D, N ;
string word [5050] ;
bool has [20] [50] ;

int main(int argc, char **argv) {
	ifstream in(FILE_IN) ;
	ofstream out(FILE_OUT) ;

  in >> L >> D >> N ;
  string l ;
  getline(in, l) ;
	for (int line = 0 ; line < D ; line ++) {
    getline(in, word [line]) ;
  }
  
	for (int test = 1 ; test <= N ; test ++) {
    memset(has, false, sizeof(has)) ;
    string stest ;
    getline(in, stest) ;
    int ip = 0 ;
    for (int i = 0 ; i < L ; i ++) {      
      if (stest [ip] == '(') {
        ip ++ ;
        while (stest [ip] != ')') {
          has [i] [stest [ip ++] - 'a'] = true ;
        }
        ip ++ ;
      }
      else {
        has [i] [stest [ip ++] - 'a'] = true ;
      }
    }
    int cnt = 0 ;
    for (int iw = 0 ; iw < D ; iw ++) {
      bool ok = true ;
      for (int i = 0 ; i < L && ok ; i ++) {
        ok = has [i] [word [iw] [i] - 'a'] ;
      }
      if (ok) cnt ++ ;
    }
    out << "Case #" << test << ": " << cnt << endl ;
  }

	in.close() ;
	out.close() ;
}
