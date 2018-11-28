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
	#define	FILE_IN		"D-small.in"
	#define FILE_OUT	"D-small.out"
#endif
#ifndef small
	#define	FILE_IN		"D-large.in"
	#define FILE_OUT	"D-large.out"
#endif

#define MAXM  10005
	ifstream in(FILE_IN) ;
	ofstream out(FILE_OUT) ;
	
int num_tests, test ;
int k ;
string s, tmp ;

int count(string s) {
  int cnt = 1 ;
  char last = s [0] ;
  for (int i = 1 ; i < s.size() ; i ++) {
    if (s [i] != last) {
      cnt ++ ;
      last = s [i] ;
    }
  }
  return cnt ;
}

int main(int argc, char **argv) {
  getline(in, tmp) ;
  istringstream is(tmp) ;
	is >> num_tests ;

	for (int test = 1 ; test <= num_tests ; test ++) {
    getline(in, tmp) ;
    istringstream is(tmp) ;
    is >> k ;
    getline(in, s) ;
    int p [k] ;
    for (int i = 0 ; i < k ; i ++) p [i] = i ;
      
    int best = -1, cnt ;
    do {
      int i = 0 ;
      cnt = 0 ;
      string gs = "" ;
      while (i < s.size()) {
        string ts = "" ;
        for (int j = i ; j < i + k ; j ++)
          ts += s [i + p [j - i]] ;
        gs += ts ;         
        i += k ;
      }
      cnt = count(gs) ;
      if (best == -1 || best > cnt) best = cnt;
    } while (next_permutation(p, p + k)) ;
    
    out << "Case #" << test << ": " << best << endl ;    
	}

	in.close() ;
	out.close() ;
}
