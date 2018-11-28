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

typedef pair<int, int> pint ;

int n, k ;
int w [105] [35], ind [105], oud [105], d [105] ;
vector<int> e [105] ;
bool vis [105] [2] ;
int m [105] [2], p [105] [2] ;

void extend(int su) {
	queue<pint> q ;
	for (int u = 0 ; u < n ; u ++) {
		vis [u] [0] = false ;
		vis [u] [1] = false ;
		p [u] [0] = -1 ;
		p [u] [1] = -1 ;
	}
	vis [su] [0] = true ;
	q.push(pint(su, 0)) ;
	int sv = -1 ;
	while (!q.empty() && sv == -1) {
		pint cur = q.front() ; q.pop() ;
		int u = cur.first, x = cur.second ;
		if (x == 0) {
			for (int i = 0 ; i < e [u].size() && sv == -1 ; i ++) {
				int v = e [u] [i] ;
				if (vis [v] [1] == false) {
					p [v] [1] = u ;
					vis [v] [1] = true ;
					if (m [v] [1] == -1) {						
						sv  = v ;
					}
					else {						
						q.push(pint(v, 1)) ;					
					}
				}				
			}
		}
		else {
			int v = m [u] [1] ;
			p [v] [0] = u ;
			vis [v] [0] = true ;
			q.push(pint(v, 0)) ;
		}
	}
	if (sv != -1) {		
		int v = sv ;
		while (v != -1) {			
			int u = p [v] [1] ;
			int tv = m [u] [0] ;
			m [u] [0] = v ;
			m [v] [1] = u ;
			v = tv ;
		}
	}
}

int maxmatch() {
	int count = 0 ;
	for (int u = 0 ; u < n ; u ++) {
		m [u] [0] = -1 ;
		m [u] [1] = -1 ;
	}
	for (int u = 0 ; u < n ; u ++) {
		if (m [u] [0] == -1) {
			extend(u) ;
		}
		if (m [u] [0] != -1) count ++ ;
	}
	return count ;
}

int main(int argc, char **argv) {
	setName() ;	    
	ifstream in(FILE_IN.c_str()) ;
	ofstream out(FILE_OUT.c_str()) ;

	int numTest ;	
	in >> numTest ;
	for (int test = 1 ; test <= numTest ; test ++) {		
		in >> n >> k ;		
		
		for (int i = 0 ; i < n ; i ++) {
			e [i].clear() ;
			for (int j = 0 ; j < k ; j ++)
				in >> w [i] [j] ;
		}
		memset(ind, 0, sizeof(ind)) ;
		memset(oud, 0, sizeof(oud)) ;
		for (int u = 0 ; u < n ; u ++)
			for (int v = 0 ; v < n ; v ++) {
				bool ok = true ;
				for (int j = 0 ; j < k && ok ; j ++)
					if (w [u] [j] <= w [v] [j]) ok = false ;
				if (ok) {
					e [u].push_back(v) ;
					oud [u] ++ ;
					ind [v] ++ ;
				}
			}

		
		out << "Case #" << test << ": " << n - maxmatch() << endl ;
	}
	
	in.close() ;
	out.close() ;
}
