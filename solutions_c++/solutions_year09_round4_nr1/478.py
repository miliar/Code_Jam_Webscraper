/* feliz cumpleaños sabi ! =P */
#include <vector>
#include <queue>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>

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

int mat[64][64];

int main() {
//	freopen("perm.in", "r", stdin);

	int tt;
	cin >> tt;

	forn(t, tt) {
		int n;
		cin >> n;
		forn(i, n) forn(j, n) { char c; cin >> c; mat[i][j] = c-'0'; }
		
		int v[64], rd[64], w[64];
		forn(i, n) {
			v[i] = 0; rd[i] = i;
			forn(j, n) if (mat[i][j]) v[i] = j;
		}
		
		tint res = 0;

		int acm[64];
		forn(i, n+1) acm[i] = 0;
		forn(i, n) acm[v[i]]++;
		forn(i, n) acm[i+1] += acm[i];
		
		dforn(i, n) w[i] = --acm[v[i]];
		#define show(D) { cerr << #D << " = "; forn(_, n) cerr << D[_] << " "; cerr << endl; }
		
/*
		show(v);
		show(w);
		res = 0; forn(i, n) forn(j, i) { res += w[i] < w[j]; }
		DBG(res);
*/
		
		int chg = 1;
		while(chg) { chg = 0;
			forn(i, n) forn(j, i) {
				if (w[i] < v[j] || w[j] < v[i]) continue;
				if (w[j] < w[i]) continue;
				swap(w[j], w[i]);
				chg = 1;
			}
		}

/*
		show(v); show(w);
		res = 0; forn(i, n) forn(j, i) { res += w[i] < w[j]; }
		DBG(res);
*/

/*
		forn(k, n)
		dforn(i, n-1) {
			if (v[i] > i) { 
				swap(v[i], v[i+1]); res++; 
				forn(kk, n) cerr << v[kk] << " "; cerr << endl;
			}
		}
*/
//		dforn(i, n) { if (acm[i] > i }
		
		res = 0; forn(i, n) forn(j, i) { res += w[i] < w[j]; }
		
		
		printf("Case #%d: %lld\n", t+1, res);
	}
	return 0;
}
