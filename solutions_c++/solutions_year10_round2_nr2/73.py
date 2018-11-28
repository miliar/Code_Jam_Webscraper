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

int n, k ;
double b, t, x [55], v [55] ;

int main(int argc, char **argv) {
	setName() ;	    
	ifstream in(FILE_IN.c_str()) ;
	ofstream out(FILE_OUT.c_str()) ;

	int numTest ;
	in >> numTest ;
	for (int test = 1 ; test <= numTest ; test ++) {
    in >> n >> k >> b >> t ;
    for (int i = 0 ; i < n ; i ++) in >> x [i] ;
    for (int i = 0 ; i < n ; i ++) in >> v [i] ;
    int c0 = 0, c1 = 0 ;
    int count = 0 ;
    for (int i = n - 1 ; i >= 0 && c1 < k ; i --) {
      if (le((b - x [i]) / v [i], t)) {
        c1 ++ ;
        count += c0 ;
        
      }
      else c0 ++ ;
    }
    if (c1 >= k) out << "Case #" << test << ": " << count << endl ;
    else out <<"Case #" << test << ": IMPOSSIBLE" << endl ;
  }
  in.close() ;
	out.close() ;
}
