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
#define ABS(a) ((a) > 0 ? (a) : -(a))

#define eps 1e-9
#define gr(a, b) ((a) > (b) + eps)
#define ge(a, b) ((a) > (b) - eps)
#define le(a, b) ((a) < (b) + eps)
#define ls(a, b) ((a) < (b) - eps)
#define eq(a, b) ((a) > (b) - eps && (a) < (b) + eps) 


string FILE_IN, FILE_OUT ;

void setName() {
	string comm ;
    cin >> comm ;
    if (comm [0] == 'l' || comm [0] == 'L') {
		FILE_IN = "B-large.in" ;
		FILE_OUT = "B-large.out" ;
   	}
   	else {
		FILE_IN = "B-small.in" ;
		FILE_OUT = "B-small.out" ;
	}
}

#define right(u) (2 * (u) + 1)
#define left(u) (right(u) + 1)

map<VI, int> d [2500] ;
int cost [2500] ;
int n, k ;

int calc(int u, VI c) {
  if (d [u].count(c) != 0) return d [u] [c] ;
  //cout << "u: " << u << ", " << cost [u] << endl ;
  //for (int i = 0 ; i < c.size() ; i ++) cout << c [i] << " " ;
  //cout << endl ;
  
  if (c.size() == 0) return 0 ;
  if (c.size() == 1) {
    d [u] [c] = 0 ;
  }
  else {
    VI l, r, lw, rw ;
    bool ok = true ;

    for (int i = 0 ; i < c.size() / 2 ; i ++) {
      l.push_back(c [i] - 1) ;
      lw.push_back(c [i]) ;

      if (c [i] == 0) ok = false ;
    }
    for (int i = c.size() / 2 ; i < c.size() ; i ++) {
      r.push_back(c [i] - 1) ;
      rw.push_back(c [i]) ;

      if (c [i] == 0) ok = false ;
    }
    d [u] [c] = calc(left(u), lw) + calc(right(u), rw) + cost [u] ;
    //cout << "ok: " << ok << endl ;
    if (ok) {
        
      int tmp = calc(left(u), l) + calc(right(u), r) ;
      //cout << "    tmp: " << tmp << endl ;
      if (tmp < d [u] [c]) d [u] [c] = tmp ;
    }
    
  }
  //cout << "d [" << u << "->"  << d [u] [c] << endl ;
  return d [u] [c] ;
}

int p ;

int main(int argc, char **argv) {
	setName() ;	    
	ifstream in(FILE_IN.c_str()) ;
	ofstream out(FILE_OUT.c_str()) ;

	int numTest ;
	in >> numTest ;
	for (int test = 1 ; test <= numTest ; test ++) {
    cout << "Test: " << test << endl ;
    in >> p ;
    //cout << "p: " << p << endl ;
    VI cond ;
    int tmp ;
    for (int i = 0 ; i < 2500 ; i ++) d [i].clear() ;
    for (int i = 0; i < (1 << p) ; i ++) {
      in >> tmp ;
      cond.push_back(tmp) ;
    }
    //reverse(cond.begin(), cond.end()) ;

    for (int i = (1 << p) - 2 ; i >= 0 ; i --) {
      in >> cost [i] ;
      //cout << "i: " << cost [i] << endl ;
    }
    //cout << "cond: " << cond.size() << endl ;
    out << "Case #" << test << ": " << calc(0, cond) << endl ;
    
  }
  //int t ; cin >> t ;
  in.close() ;
	out.close() ;
}
