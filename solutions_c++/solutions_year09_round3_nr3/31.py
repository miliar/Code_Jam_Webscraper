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

typedef unsigned 
long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define	MIN(a, b)	((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))

#define eps 1e-9
#define sqr(x) ((x) * (x))
#define gr(a, b) ((a) > (b) + eps)
#define ge(a, b) ((a) > (b) - eps)
#define le(a, b) ((a) < (b) + eps)
#define ls(a, b) ((a) < (b) - eps)
#define eq(a, b) ((a) > (b) - eps && (a) < (b) + eps) 


string FILE_IN, FILE_OUT ;

void setName() {
	string comm ;
  cin >> comm ;
  FILE_IN = "C-small.in" ;
	FILE_OUT = "C-small.out" ;
  if (comm [0] == 'l' || comm [0] == 'L') {
		FILE_IN = "C-large.in" ;
		FILE_OUT = "C-large.out" ;
	}
}

int p, q ;
VI c ;
int d [1100] [1100] ;

int calc(int p1, int p2) {
	if (p1 < 0) return -1 ;
	if (p2 < p1) return -1 ;
	if (p1 == p2) return 0 ;
	if (p1 + 1 == p2) return 0 ;
	int &ret = d [p1] [p2] ;
	if (ret != -1) return ret ;
	for (int i = p1 + 1 ; i < p2 ; i ++) {
		int tmp = c [p2] - c [p1] - 2 + calc(p1, i) + calc(i, p2) ;
		if (ret == -1 || (ret > tmp)) {
			ret = tmp ;
		}
	}
	return ret ;
}

int main(int argc, char **argv) {
	setName() ;	    
	ifstream in(FILE_IN.c_str()) ;
	ofstream out(FILE_OUT.c_str()) ;

	int numTest ;	
	in >> numTest ;
	for (int test = 1 ; test <= numTest ; test ++) {
		for (int i = 0 ; i < 1100 ; i ++) for (int j = 0 ; j < 1100 ; j ++) d [i] [j] = -1 ;
		in >> p >> q ;
		c.clear() ;
		for (int i = 0 ; i < q ; i ++) {
			int cell ;
			in >> cell ;
			c.push_back(cell) ;			
		}
		c.push_back(0) ;
		c.push_back(p + 1) ;
		sort(c.begin(), c.end()) ;
						
		out << "Case #" << test << ": " << calc(0, q + 1) << endl ;
	}
	
	in.close() ;
	out.close() ;
}
