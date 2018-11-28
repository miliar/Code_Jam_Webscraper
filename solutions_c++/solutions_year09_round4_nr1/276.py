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
#define gr(a, b) ((a) > (b) + eps)
#define ge(a, b) ((a) > (b) - eps)
#define le(a, b) ((a) < (b) + eps)
#define ls(a, b) ((a) < (b) - eps)
#define eq(a, b) ((a) > (b) - eps && (a) < (b) + eps) 


string FILE_IN, FILE_OUT ;

void setName() {
	string comm ;
  cin >> comm ;
  FILE_IN = "A-small.in" ;
	FILE_OUT = "A-small.out" ;
  if (comm [0] == 'l' || comm [0] == 'L') {
		FILE_IN = "A-large.in" ;
		FILE_OUT = "A-large.out" ;
	}
}

int n ;
string row [41] ;
vector<int> v ;

int main(int argc, char **argv) {
	setName() ;	    
	ifstream in(FILE_IN.c_str()) ;
	ofstream out(FILE_OUT.c_str()) ;
	
	string line ;
	istringstream is ;

	int numTest ;
	in >> numTest ;
	
	for (int test = 1 ; test <= numTest ; test ++) {
		in >> n ;		
		v.clear() ;
		int count = 0 ;		
		for (int r = 0 ; r < n ; r ++) {
			in >> row [r] ;			
			bool ok = true ;
			for (int c = row [r].size() - 1 ; c >= 0 && ok ; c --) {
				if (row [r] [c] == '1') {
						ok = false ;
						v.push_back(c) ;
				}
			}
			if (ok) v.push_back(0) ;			
		}
		for (int r = 0 ; r < n ; r ++) {
				
				bool found = false ;
				int ir ;
				for (int i = r ; i < n && !found ; i ++) {						
						if (v [i] <= r) {
								ir = i ;
								found = true ;
						}
				}
				if (found) {
						for (int i = ir ; i > r ; i --) {
							int t = v [i - 1] ;
							v [i - 1] = v [i] ;
							v [i] = t ;
							
							count ++ ;
						}
				}
		}
		out << "Case #" << test << ": " << count << endl ;
	}
	
	in.close() ;
	out.close() ;
}
