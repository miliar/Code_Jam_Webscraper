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
		FILE_IN = "A-large.in" ;
		FILE_OUT = "A-large.out" ;
   	}
   	else {
		FILE_IN = "A-small.in" ;
		FILE_OUT = "A-small.out" ;
	}
}

struct Trie {
  map<string, Trie> next ;
} ;

int n, m ;

int ins(Trie &root, string path) {
  if (path.size() == 0) return 0 ;
  path = path.substr(1) ;
  istringstream in(path) ;
  Trie &cur = root ;
  int fin = path.find_first_of("/") ;
  if (fin == string::npos) fin = path.size() ;
  string dir = path.substr(0, fin) ;
  path = fin < path.size() ? path.substr(fin) : "" ;
  if (cur.next.count(dir) == 0) {
    Trie child ;
    cur.next [dir] = child ;
    return 1 + ins(cur.next [dir], path) ;
  }
  else {
    return ins(cur.next [dir], path) ;
  }
}

int main(int argc, char **argv) {
	setName() ;	    
	ifstream in(FILE_IN.c_str()) ;
	ofstream out(FILE_OUT.c_str()) ;

	string line ;
	istringstream is ;
  getline(in, line) ;

	int numTest ;
	numTest = s2i(line) ;
	for (int test = 1 ; test <= numTest ; test ++) {
    getline(in, line) ;
    istringstream is(line) ;
    is >> n >> m ;
    Trie root ;
    for (int r = 0 ; r < n ; r ++) {
      getline(in, line) ;
      ins(root, line) ;
    }
    int count = 0 ;
    for (int r = 0 ; r < m ; r ++) {
      getline(in, line) ;
      count += ins(root, line) ;
    }
    out << "Case #" << test << ": " << count << endl ;
    
	}
	in.close() ;
	out.close() ;
}
