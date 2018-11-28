#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>

using namespace std;

/* tipos */
typedef long long tint;
typedef unsigned int uint;
typedef unsigned long long utint;
typedef long double tdbl;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<string> vstr;
typedef vector<tint> vtint;
typedef vector<tdbl> vdbl;
typedef pair<int, int> pint;
typedef pair<string, string> pstr;

typedef long double tipo;

/* "funciones" */
#define forn(i,n) for(int ___n=n, i=0;i<___n;++i)
#define dforn(i,n) for(int i=(n)-1;i>=0;--i)
#define forsn(i,s,n) for(int ___n=n, i=s;i<___n;++i)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define forall(it,X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define dforall(it,X) for(typeof((X).rbegin()) it = (X).rbegin(); it != (X).rend(); ++it)
#define all(X) (X).begin(), (X).end()
#define esta(e, c) (c.find(e) != c.end())
#define DBG(a) cerr << #a << " = " << a << endl;

template<class T> string itos(const T&x) { ostringstream o; o<<x; return o.str(); }
template<class T> inline int size(const T&c) { return c.size(); }
inline int bneed(unsigned long long x) { return x?64-__builtin_clzll(x):0; }
inline int lg2(unsigned long long x) { return x?63-__builtin_clzll(x):-1; }
#define strtostr(S, s) {istringstream s; s.str(S);}

#define foldr(X, OP, NEU, res) { res = (NEU); forall(it, X) res OP (*it);}
#define sumall(X, res) foldr(X, +=, 0, res)
#define mulall(X, res) foldr(X, *=, 1, res)

/* fin del template */

#define INF 10000000

char mp[4][4];
int mem[1<<16][4][4];
int mpr, mpc;

#define rango(i, j) (((i)>=0) && ((i) < mpr) && ((j)>=0) && ((j) < mpc))
#define coor(i, j) ((i)*4+(j))
#define bit(x, b) (((x) >> (b)) & 1)

int din(int tbl, int ri, int rj) {
	int &r = mem[tbl][ri][rj];
	if (r!= -1) return r;
	r = 0;
	forsn(di, -1, 2) forsn(dj, -1, 2) if (rango(ri+di, rj+dj) && !bit(tbl, coor(ri+di, rj+dj))) {
//		cerr << ri << "  "  << rj << " ==> "  << ri+di << "  "  << rj+dj << endl;
		if (din(tbl | (1 << coor(ri+di, rj+dj)), ri+di, rj+dj) == 0) { r=1; break; }
	}
	return r;
}

int main() {
	int T;
	cin >> T;
	forn(tt, T) {
		fill(mem[0][0], mem[1<<16][0], -1);
		int r, c, ri=-1, rj=-1;
		cin >> r >> c; mpr=r; mpc=c;
		forn(i, 4) forn(j, 4) mp[i][j] = '#';
		forn(i, r) forn(j, c) {
			cin >> mp[i][j];
			if (mp[i][j] == 'K') { ri = i; rj = j; mp[i][j] = '#'; }
		}

		int init = 0;
		forn(i, 4) forn(j, 4) init |= (mp[i][j] == '#') << (4*i+j);
		
//		forn(i, r) { forn(j, c) cerr << mp[i][j]; cerr << endl; }
		int res = din(init, ri, rj);
		cout << "Case #" <<  tt+1 << ": " << (char)('B'-res) << endl;
//		printf("Case #%d: %ld\n", tt+1, res);
//	return 0;
	}

	return 0;
}
