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

using namespace std;

/* tipos */
typedef pair<int,int> pint;
typedef long long tint;
typedef unsigned int mint;
typedef unsigned long long mtint;

typedef vector<int> vint;
typedef vector<vint> vvint;

typedef long double tdbl;

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

struct vine {
	int d, l;
};

#define MAXN 10100
vine v[MAXN];

int best[MAXN];
int state[MAXN];


int main() {
	int tt;
	cin >> tt;
	forn(_t, tt) {
		int n, d;
		cin >> n;
		forn(i, n) cin >> v[i].d >> v[i].l;
		cin >> d;
		bool res = false;
		queue<int> q;
		fill(best, best+n, 0);
		fill(state, state+n, 0);

		v[n].d = d;
		v[n].l = 0;
		best[n] = -1;
		n++;
		#define pone(i, d) if (best[i] < (d)) { if (!state[i]) q.push(i); best[i] = (d); }
		pone(0, v[0].d);
		while (!q.empty()) {
			int i = q.front(); q.pop();
			state[i] = 0;
			int md = best[i];
			for(int j = i+1; j < n && (v[j].d - v[i].d <= md); j++) {
				pone(j, min(v[j].l, v[j].d - v[i].d));
			}
		}

		// cerr << "best = "; forn(i, n) cerr << best[i] << " "; cerr << endl;

		res = best[n-1] >= 0;

		printf("Case #%d: %s\n", _t+1, res?"YES":"NO");
	}
	return 0;
}

