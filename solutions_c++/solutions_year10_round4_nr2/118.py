#include <vector>
#include <queue>
#include <map>
#include <list>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

/* tipos */
typedef pair<int,int> pint;
typedef long long tint;
typedef unsigned int mint;
typedef unsigned long long mtint;

typedef vector<int> vint;
typedef vector<vint> vvint;

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
tint sqr(tint a) { return a*a; }

int m[2048];
int cst[2090];
#define INFTO 0x3f3f3f3f3f3f3f3fLL
#define lvl(p) (31-__builtin_clz((p)))

int n, q;
tint din(int p) {
	if (p+1 > q) return m[p-q]>=0?0:INFTO;
	int pa = din(2*p+0);
	int pb = din(2*p+1);
	int l = lvl(p);
	int fl = (p << (n-l)) -q;
	int fr = ((p+1) << (n-l)) -q;
//	cerr << p << " " << fl << " " << fr << "  | " << pa << " " << pb << endl;
	forsn(i, fl, fr) if (m[i] < 0) return INFTO;
	forsn(i, fl, fr) m[i]--;
	int npa = din(2*p+0);
	int npb = din(2*p+1);
	forsn(i, fl, fr) m[i]++;
	return min(pa+pb+cst[p], npa+npb);
}

int lvl[2090];

int main() {
	int tt;
	cin >> tt;
	forn(t, tt) {
		cin >> n;
		q = 1 << n;
		DBG(q);
		DBG(n);

		dforn(i, q) cin >> m[i];
		dforn(i, q-1) cin >> cst[i+1];
		
//		forn(i, q) cerr << m[i] << " "; cerr << endl;
//		forn(i, q-1) cerr << cst[i+1] << " "; cerr << endl;
//		cerr << endl;
		
		tint res = din(1);
		
		cout << "Case #" << (t+1) << ": " << res << endl;
	}
	return 0;
}

