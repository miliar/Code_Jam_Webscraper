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

int m, v, x;
vint tr, ch, vl, cst;
#define INF 10000000

int main() {
	int T;
	cin >> T;
	forn(tt, T) {
		cin >> m >> v;
		x = (m-1)/2;
//		DBG(x);
		tr = ch = vl = vint(m);
		cst = vint(m, -1);
		forn(i, x) cin >> tr[i] >> ch[i];
		forsn(i, x, m) { cin >> vl[i]; ch[i] = 2; cst[i] = (vl[i]==v)?0:INF; }
		dforn(i, x) {
			int h1=2*i+1, h2=2*i+2;
			vl[i] = tr[i]?(vl[h1]&&vl[h2]):(vl[h1]||vl[h2]);
			if (v == vl[i]) { cst[i] = 0; continue; }
			if (v) {
				if (tr[i]) cst[i] = min(cst[h1]+cst[h2], ch[i]?min(1+cst[h1], 1+cst[h2]):INF);
				else cst[i] = min(cst[h1], cst[h2]);
			} else {
				if (!tr[i]) cst[i] = min(cst[h1]+cst[h2], ch[i]?min(1+cst[h1], 1+cst[h2]):INF);
				else cst[i] = min(cst[h1], cst[h2]);
			}
		}
		int res = cst[0];
		if (res >= INF) {
			cout << "Case #" <<  tt+1 << ": " << "IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" <<  tt+1 << ": " << res << endl;
		}
//		printf("Case #%d: %ld\n", tt+1, res);
	}

	return 0;
}
