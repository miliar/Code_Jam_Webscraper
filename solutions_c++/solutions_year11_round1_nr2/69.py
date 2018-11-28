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
#include <cstring>
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
typedef vector<string> vstr;

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

string wrd[10500];
string qrys[105];
string res[105];
int wid[10500][32];
int ns;
int sset[10500];
int lset[10500];
int xset[10500];

int scratch[2048];
int vl[10500];

int split(int s, int l) {
	int _xset;
	int _sset = sset[s]; sset[s] = -1; lset[s] = 0;
	int _ns = ns;
	for(int x=_sset; x!=-1; x=_xset) {
		_xset = xset[x];
		int id = scratch[wid[x][l]];
		if (!id) {
			if (wid[x][l] == 0) {
				id = s;
			} else {
				lset[ns] = 0;
				sset[ns] = -1;
				id = scratch[wid[x][l]] = ns++;
			}
		}
		xset[x] = sset[id];
		sset[id] = x;
		lset[id]++;
	}
	forsn(cs, _ns, ns) scratch[wid[sset[cs]][l]] = 0;
	if (lset[s] == 0) {
		ns--;
		sset[s] = sset[ns];
		lset[s] = lset[ns];
		return 0;
	}
	return lset[s];
}

void show() {
	forn(s,ns) {
		cerr << "s" << s << " (" << lset[s] << ") : ";
		for(int x=sset[s]; x!=-1; x=xset[x]) cerr << " " << x; cerr << endl;
	}
	int sm = 0; forn(i, 2048) sm += scratch[sm];
	if (sm) cerr << "ALERT! sm=" << sm << endl;
	cerr << "----" << endl;
}

int m, n;
void solve() {
	memset(wid, 0, sizeof(wid));
	forn(i, n) {
		wid[i][0] = wrd[i].size();
		forn(j, wid[i][0]) wid[i][ wrd[i][j] & 0x1f ] |= 1 << j;
	}
	
	forn(q, m) {
		ns = 1;
		sset[0] = 0; lset[0] = n;
		forn(i, n) xset[i] = i+1; xset[n-1] = -1;
		//show();
		split(0, 0);
		//show();
		memset(vl, 0, sizeof(int)*n);
		forn(l, 26) {
			int ll = qrys[q][l] & 0x1f;
			//DBG(ll);
			for(int s =ns-1; s>=0; s--) {
				int sz = lset[s];
				int spl = split(s, ll);
				if (spl && spl != sz) {
					for(int x=sset[s]; x!=-1; x=xset[x]) vl[x]++;
				}
			}
			//show();
			if(ns == n) break;
		}
		int best = -1;
		forn(i, n) if (best == -1 || vl[best] < vl[i]) best = i;
		forn(i, n) cerr << vl[i] << " "; cerr << endl;
		res[q] = wrd[best];
	}
}

int main() {
	memset(scratch, 0, sizeof(scratch));
	
	int tt;
	cin >> tt;
	forn(t, tt) {
		cin >> n >> m;
		forn(i, n) cin >> wrd[i];
		forn(i, m) cin >> qrys[i];
		solve();
		cout << "Case #" << t+1 << ":";
		forn(q, m) cout << " " << res[q];
		cout << endl;
	}
	return 0;
}

