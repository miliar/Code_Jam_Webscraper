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
// Sorters <int>
template<typename T> struct sorter_gen {
  T& v;
  sorter_gen(T& vv) : v(vv) {}
  bool operator()(int a, int b) { return v[a] < v[b]; }
};
#define sortind(I, X) sort(all(I), (sorter_gen<typeof(X)>)(X))

#define MAXN 2048

int res[MAXN];
int hgst[MAXN];
int rev[MAXN];
int n;

void copate(int i) {
	int x1 = hgst[i];
	int x2 = hgst[x1];
	tint y1 = res[x1];
	tint y2 = res[x2];

	int ped = (y2-y1) / (x2-x1) + 1;

	int j = hgst[i];
	if (j-i <= 1) return;
	int k;
	for(k = i+1; k < j; k++) if (hgst[k] == j) break;
	
	res[k] = res[j] + ped * (k-j) - 1;
	copate(k);
	hgst[i] = k;
	copate(i);
}

int main() {
	int tt;
	cin >> tt;
	forn(_t, tt) {
		cin >> n;
		forn(i, n-1) { cin >> hgst[i]; hgst[i]--; }
		hgst[n-1] = n;
		// forn(i, n) rev[hgst[i]] = ;

		forn(i, n) cerr << hgst[i] << " "; cerr << endl;
		fill(res, res+n+1, -1);

		/* Check feasible */
		bool fail = false;
		forn(j, n-1) if (!fail) forn(i, j) {
			if (j < hgst[i] && hgst[i] < hgst[j]) { fail = true; break; }
		}
		if (fail) {
			printf("Case #%d: Impossible\n", _t+1);
			continue;
		}

		res[0] = 999999999;
		int ped = res[0] / (n+2);
		for(int i = 0; i < n; i = hgst[i]) {
			res[i] = res[0] - ped * i;
		}
		res[n] = res[0] - ped * n;
		for(int i = 0; i < n; i = hgst[i]) {
			copate(i);
		}

		// forn(i, n) cerr << l2[p[i]] - 2*i <<  " "; cerr<< endl;
		
		printf("Case #%d:", _t+1);
		forn(i, n) printf(" %d", res[i]);
		printf("\n");
	}
	return 0;
}

