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

tint mcd(tint a, tint b){ return (a==0)?b:mcd(b%a, a);}
struct dxy {tint d,x,y;};
dxy mcde(tint a, tint b) {
  dxy r, t;
  if (b == 0) {
    r.d = a; r.x = 1; r.y = 0;
  } else {
    t = mcde(b,a%b);
    r.d = t.d; r.x = t.y;
    r.y = t.x - a/b*t.y;
  }
  return r;
} 


static tint mods[100111];
static tint omods[100111];
static tint coef[100111];
int nmods;
//static int vl[10000*10000];

int num[128], n;
tint l;
#define INFTO 0x3f3f3f3f

tint solve() {
	tint mc = num[0];
	forn(i, n) mc = mcd(mc, num[i]);
	if (l % mc != 0) return -1;

	memset(mods, 0x3f, sizeof(mods));
	memset(coef, 0, sizeof(coef));
	nmods = 1; mods[0] = 0;
	tint m = num[n-1];
	int r = l % m;
	memcpy(omods, mods, sizeof(mods));

//	tint res = INFTO;

	int ch = 1;
	while (ch) { 
		ch = 0;
		forn(p, m) if (mods[p] != INFTO) {
			dforn(i, n-1) {
				for(int j = 1; j*num[i] % m; j++) { 
					int np = (p+num[i]*j) % m;
					int nv = mods[p] + j - (p+num[i]*j) / m;
					if (nv < omods[np]) { omods[np] = nv; ch++; }
					else { break; }
				}
			}
		}
		memcpy(mods, omods, sizeof(mods));
		DBG(ch);
	}
	if (mods[r] == INFTO) return -1;
	return mods[r] + (l - r) / m;
}

tint solve2() {
	tint a = num[0];
	tint b = num[1];
	if (l%b == 0) return l/b;
	tint d = mcd(a, b);
	if (l % d != 0) return -1;

	tint r = l % b;
	tint x = 0;
	for(x = 0; x < b; x++) if ( (a*x) % b == r) break;
	DBG(x);
	DBG((l-a*x) / b);
	return x + (l-a*x) / b;
}

int main() {
	int tt;
	cin >> tt;
	forn(t, tt) {
		cin >> l >> n;
		forn(i, n) cin >> num[i];
		sort(num, num+n);
		tint res = -1;
		if (n==1) {
			tint a = num[0];
			res = (l%a == 0)?l/a:-1;
		} else if (n==2) {
			res = solve2();
		} else {
			res = solve();
		}
		
		if (res == -1) {
			cout << "Case #" << (t+1) << ": " << "IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << (t+1) << ": " << res << endl;
		}
	}
	return 0;
}

