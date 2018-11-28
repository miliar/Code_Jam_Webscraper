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

#define eps 1e-9
#define gr(a, b) ((a) > (b) + eps)
#define ge(a, b) ((a) > (b) - eps)
#define le(a, b) ((a) < (b) + eps)
#define ls(a, b) ((a) < (b) - eps)
#define eq(a, b) ((a) > (b) - eps && (a) < (b) + eps) 


#define small

#ifdef small
	#define	FILE_IN		"D-small.in"
	#define FILE_OUT	"D-small.out"
#endif
#ifndef small
	#define	FILE_IN		"D-large.in"
	#define FILE_OUT	"D-large.out"
#endif


int num_tests, test ;
int R, W, H ;
bool fr [105] [105] ;
int d [105] [105] ;

int dr [2] = {2, 1} ;
int dc [2] = {1, 2} ;

bool ok(int way, int r, int c, int &xr, int &xc) {
	xr = r + dr [way] ;
	xc = c + dc [way] ;
	return (xr >= 0 && xr < H && xc >= 0 && xc < W) ;
}

int main(int argc, char **argv) {
	ifstream in(FILE_IN) ;
	ofstream out(FILE_OUT) ;

	in >> num_tests ;
	for (int test = 1 ; test <= num_tests ; test ++) {
		cout << "Test: " << test << endl ;
		in >> H >> W >> R ;
		for (int ir = 0 ; ir < H ; ir ++) {
			for (int ic = 0 ; ic < W ; ic ++) {
				fr [ir] [ic] = true ;
				d [ir] [ic] = 0 ;
			}
		}
		for (int ir = 0 ; ir < R ; ir ++) {
			int r, c;
			in >> r >> c ;
			fr [r - 1] [c - 1] = false;
		}
		d [0] [0] = 1 ;
		int nr, nc ;
		for (int ir = 0 ;ir < H ; ir ++) {
			for (int ic = 0 ; ic < W ; ic ++)	{
				if (fr [ir] [ic] && d [ir] [ic] > 0) {
					for (int way = 0 ; way < 2 ; way ++) {
						if (ok(way, ir, ic, nr, nc)) {
							if (fr [nr] [nc]) {
								d [nr] [nc] = (d [nr] [nc] + d [ir] [ic]) % 10007 ;
							}
						}
					}
				}
			}
		}
		/*
		f
		or (int ir = 0 ; ir < H ; ir ++) {
			for (int ic = 0 ; ic < W ; ic ++) {
				cout << d [ir] [ic] << ", " ;
			}
			cout << endl ;
		}
		*/
		out << "Case #" << test << ": " << d [H - 1] [W - 1] << endl ;
	}
	int tmp ;
	cin >> tmp ;
		
	in.close() ;
	out.close() ;
}
