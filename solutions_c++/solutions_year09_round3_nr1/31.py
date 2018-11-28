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


int next(int num, int base) {
	int val = 0, dig ;
	while (num > 0) {
		dig = num % base ;
		val += dig * dig ;
		num /= base ;
	}
	return val ;
}

map<char, int> m ;
vector<char> lang ;

int main(int argc, char **argv) {
	setName() ;	    
	ifstream in(FILE_IN.c_str()) ;
	ofstream out(FILE_OUT.c_str()) ;
	
	string line ;
	istringstream is ;

	int numTest ;
	getline(in, line) ;
	is.str(line) ;
	is >> numTest ;
	for (int test = 1 ; test <= numTest ; test ++) {
		getline(in, line) ;
		m.clear() ;
		lang.clear() ;
		m [line [0]] = 1 ;
		lang.push_back(line [0]) ;
		int nv = 0 ;
		for (int i = 1 ; i < line.size() ; i ++) {
			if (m.count(line [i]) == 0) {
				m [line [i]] = nv ;
				if (nv == 0) nv = 2 ;
				else nv ++ ;
				lang.push_back(line [i]) ;
			}
		}
		LL b = lang.size() ;
		if (b == 1) b ++ ;
		LL val = 0 ;
		for (int i = 0 ; i < line.size() ; i ++) 
			val = b * val + m [line [i]] ;
				
		out << "Case #" << test << ": " << val << endl ;
	}
	
	in.close() ;
	out.close() ;
}
