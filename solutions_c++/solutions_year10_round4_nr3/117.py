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

int mp[256][256];
int omp[256][256];

int main() {
	int tt;
	cin >> tt;
	forn(t, tt) {
		int r; cin >> r;
		memset(mp, 0, sizeof(mp));
		int mi=0, mj=0;
		forn(i, r) {
			int a, b, c, d;
			cin >> a >> b >> c >> d;
			if (a > c) swap(a,c); mi = max(mi, c+1);
			if (b > d) swap(b,d); mj = max(mj, d+1);
			forsn(pi, a, c+1) forsn(pj, b, d+1) mp[pi][pj] = 1;
		}
		
		int res = 0;
		int count = mi || mj;
		while(count) {
			count = 0;
			mi++; mj++;
			res++;
			dforsn(i, 1, mi) dforsn(j, 1, mj) {
				int a = mp[i][j];
				int n = mp[i-1][j];
				int w = mp[i][j-1];
				mp[i][j] = (n && w) || (a && (n || w));
				count +=  mp[i][j];
			}
		}
		
		
		cout << "Case #" << (t+1) << ": " << res << endl;
	}
	return 0;
}

