#include <vector>
#include <map>
#include <set>
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

tdbl probs[32][4];
int q;

tdbl calc(tint chs) {
	tdbl res = 1.0;
	forn(i, q) res *= probs[i][(chs >> (2*i)) & 3];
	return res;
}

tint enc(int* pq) {
	tint res = 0;
	forn(i, q) res |= (*(pq++)) << (2*i);
	return res;
}

typedef pair<tdbl, tint> pdi;

int main() {
	int T;
	cin >> T;
	forn(tt, T) {
		int m;
		cin >> m >> q;

		forn(i, q) {
			forn(j, 4) cin >> probs[i][j];
			sort(probs[i], probs[i+1]);
			swap(probs[i][0], probs[i][3]);
			swap(probs[i][1], probs[i][2]);
		}
		tdbl res = 1.0;
		if ((1 << (2*q)) <= m) {
			res = 1.0;
			DBG(q); DBG(m);
		} else {

		set<pdi> best;
		set<tint> used;
		best.insert(pdi(calc(0), 0));
		used.insert(0);

		vdbl ress;
		forn(k, m) {
//			forall(it, best) cerr << it->second << " "; cerr << endl;
			pdi mj = *(best.rbegin()); best.erase(mj);
			tint v = mj.second;
	
			int vl[32];
			forn(i, q) vl[i] = (v >> (2*i)) & 3;

//			cerr << v << " ==> "; forn(i, q) cerr << vl[i] << " "; cerr << " | " << mj.first << endl;
			ress.push_back(mj.first);
			forn(i, q) if (vl[i] < 3) {\
				vl[i]++;
				tint t = enc(vl);
				if (!esta(t, used)) {
					pdi nw(calc(t), t);
					best.insert(nw);
					used.insert(t);
//					DBG(t);
				}
				vl[i]--;
			}
		}
		sort(all(ress));
		res = 0.0;
		dforn(i, m) res += ress[i];
		}
		

		printf("Case #%d: %.8lf\n", tt+1, (double)res);
	}

	return 0;
}
