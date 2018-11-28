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

int mt[128][128];
int tm[128][128];
int xpx[128][128];
int xpy[128][128];

int main() {
	int tt;
	cin >> tt;
	forn(t, tt) {
		int n; cin >> n;
		
		memset(mt, -1, sizeof(mt));
		memset(tm, -1, sizeof(tm));
		forn(i, n) {
			forn(j, i+1) cin >> mt[i-j][j];
		}
		forn(j, n-1) {
			forn(i, n-1-j) cin >> mt[n-1-i][j+1+i];
		}
		
		
		int mx = 2*n-1;
		int my = 2*n-1;

		#define enrango(i, j) (0<= (i) && (i) < 128 && 0 <= (j) && (j) <128)

		forn(i, n) forn(j, n) tm[n-1-j][i] = mt[i][j];
		forn(i, n) { forn(j, n) cerr << mt[i][j]; cerr << "  "; forn(j, n) cerr << tm[i][j]; cerr << endl; }

		forsn(pl, -n+1, n) {
			
			int d = abs(pl);
			bool okx = true, oky = true;
			forn(i, n) forn(j, n) {
				int pi=j+pl, pj=(i-pl);
				okx = okx && (!enrango(pi,pj) || mt[pi][pj] == -1 || mt[i][j] == -1 || mt[pi][pj] == mt[i][j]);
				oky = oky && (!enrango(pi,pj) || tm[pi][pj] == -1 || tm[i][j] == -1 || tm[pi][pj] == tm[i][j]);
			}
			if (okx) { mx = min(mx, d); cerr << "X "; DBG(pl) }
			if (oky) { my = min(my, d); cerr << "Y "; DBG(pl) }

		}


		int res = mx + my;
		cerr << mx << ","<< my << endl;
		
		res = sqr(n+res) - sqr(n);
		
		cout << "Case #" << (t+1) << ": " << res << endl;
		cerr << endl << endl;
	}
	return 0;
}

