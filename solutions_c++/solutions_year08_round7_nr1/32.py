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

struct mix {
	vector<string> ing;
	int val;
	mix() : val(-1) {}
};

map<string, mix> mp;

int mej(string s) {
	if (!esta(s, mp)) return 0;
	int &r = mp[s].val;
	mix &mm = mp[s];
	if (r != -1) return r;
	r = 0;
	vint vals;
	forn(i, mm.ing.size()) {
		string ig = mm.ing[i];
		if (ig[0] <= 'Z') {
			vals.push_back(mej(ig));
		} else {
			
		}
	}
	sort(all(vals));
	reverse(all(vals));
	forn(i,vals.size()) {
		int x = vals[i]+i;
		if (x > r) r = x;
	}
	if (r<(int)vals.size()+1) r = vals.size()+1;

//	r++;
	return r;
}

int main() {
	int T;
	cin >> T;
	forn(tt, T) {
		int n; cin >> n;
		mp.clear();
		string init = "_";
		forn(i, n) {
			string s; cin >> s;
			int m; cin >> m;
			mix nw;
			forn(j, m) { string t; cin >> t; nw.ing.push_back(t); }
			mp[s] = nw;
			if (init == "_") init = s;
		}

		int res = mej(init);;

//		forall(it, mp) cerr << it->first << "  "  << it->second.val << endl;

		cout << "Case #" <<  tt+1 << ": " << res << endl;
//		printf("Case #%d: %ld\n", tt+1, res);
	}

	return 0;
}
