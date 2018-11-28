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
		FILE_IN = "C-large.in" ;
		FILE_OUT = "C-large.out" ;
   	}
   	else {
		FILE_IN = "C-small.in" ;
		FILE_OUT = "C-small.out" ;
	}
}

#define MOD 100003LL

LL b [505] [505], d [505] [505] ;

LL bin(int n, int m) {
  if (n < 0 || m < 0 || m > n) return 0LL ;
  return b [n] [m] ;
}

LL calc(int n, int k) {
  if (k < 0) return 0LL ;
  if (k > n) return 0LL ;
  LL &ret = d [n] [k] ;
  if (ret != -1LL) return ret ;
  ret = 0LL ;
  for (int l = 1 ; l < k ; l ++) {
    ret = (ret + calc(k, l) * bin(n - k - 1, k - l - 1)) % MOD ;
  }
  return ret ;
}

int main(int argc, char **argv) {
  memset(b, 0, sizeof(b)) ;
  b [0] [0] = 1LL ;
  for (int i = 1 ; i < 505 ; i ++) {
    b [i] [0] = 1LL ;
    b [i] [i] = 1LL ;
    for (int j = 1 ; j < i ; j ++)
      b [i] [j] = (b [i - 1] [j - 1] + b [i - 1] [j]) % MOD ;
  }
  for (int i = 0 ; i < 505 ; i ++) for (int j= 0 ; j < 505 ; j ++) d [i] [j] = -1LL ;
  for (int _n = 1 ; _n < 505 ; _n ++) d [_n] [1] = 1LL ;
  for (int _n = 1 ; _n < 505 ; _n ++)
    for (int k = 2 ; k < _n ; k ++)
      calc(_n, k) ;

	setName() ;	    
	ifstream in(FILE_IN.c_str()) ;
	ofstream out(FILE_OUT.c_str()) ;


	int numTest ;
	in >> numTest ;
	for (int test = 1 ; test <= numTest ; test ++) {
    int n ;
    in >> n ;
    LL count = 0LL ;
    for (int k = 1 ; k < n; k ++) count = (count + calc(n, k)) % MOD ;
    out << "Case #" << test << ": " << count << endl ;
    
	}
	in.close() ;
	out.close() ;
}
