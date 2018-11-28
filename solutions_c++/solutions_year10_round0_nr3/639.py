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

typedef unsigned long long LL;
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

#define sum(l, r) ((l) == 0 ? s [(r)] : (s [(r)] - s [(l) - 1]) )

LL R, k, N ;
LL g [2005], s [2005], vis [2005], next [2005], value [2005], total [2005] ;
int main(int argc, char **argv) {
	setName() ;	    
	ifstream in(FILE_IN.c_str()) ;
	ofstream out(FILE_OUT.c_str()) ;

	string line ;
	istringstream is ;

	int numTest ;
	in >> numTest ;
	for (int test = 1 ; test <= numTest ; test ++) {
    
    in >> R >> k >> N ;

    for (int i = 0 ; i < N ; i ++) {
      in >> g [i] ;
      g [N + i] = g [i] ;
    }
    s [0] = g [0] ;
    for (int i = 1 ; i < 2 * N ; i ++) s [i] = s [i - 1] + g [i] ;
    
    for (int i = 0 ; i < N ; i ++) {
      int l = i, r = N + i - 1, mid ;
      if (sum(i, r) <= k) l = r ;
      else {
        while (l < r - 1) {
          mid = (l + r) / 2 ;
          if (sum(i, mid) <= k) l = mid ;
          else r = mid ;
        }
      }
      next [i] = (l + 1) % N ;
      value [i] = sum(i, l) ;
    }
    for (int v = 0 ; v < 2 * N ; v ++) vis [v] = 0 ;
    int u = 0 ;
    vis [0] = 1 ; total [0] = 0 ;
    while (vis [next [u]] == 0) {
      vis [next [u]] = vis [u] + 1 ;
      total [next [u]] = total [u] + value [u] ;
      u = next [u] ;
    }
    LL preCycleTotal = total [next [u]], cycleTotal = total [u] - total [next [u]] + value [u] ;
    int preCycleSize = vis [next [u]] - 1, cycleSize = vis [u] - vis [next [u]] + 1 ;
    LL res = 0 ;
    if (R <= preCycleSize) {
      int cur = 0 ;
      for (int i = 0 ; i < R ; i ++) {
        res += value [cur] ;
        cur = next [cur] ;
      }
      cout << "A" << endl ;
    }
    else {
      R -= preCycleSize ;
      res += preCycleTotal + (R / cycleSize) * cycleTotal ;
      int cur = next [u] ;
      for (int i = 0 ; i < R % cycleSize ; i ++) {
        res += value [cur] ;
        cur = next [cur] ;
      }
      cout << "B" << endl ;
    }
    out << "Case #" << test << ": " << res << endl ;
	}
	int num ;
  cin >> num ;
	in.close() ;
	out.close() ;
}
