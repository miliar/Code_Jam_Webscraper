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
#define forsn(i,s,n) for(int ___n=n, i=s;i<___n;++i)
#define forall(it,X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define DBG(X) cerr << #X << " = " << X << endl

template<class T> string itos(const T&x) { ostringstream o; o<<x; return o.str(); }

int bone(int x) {
	int res = 0;
	while (x) { res+=x&1; x/=2; }
	return res;
}

int main() {
	int N;
	cin >> N;
	forn(tt, N) {
		int n, m; cin >> n >> m;
		vvint mat(m, vint(2*n, 0));
		vint vl(m, 0);
		forn(i, m) {
			int t;
			cin >> t;
			forn(j, t) {
				int x, y; cin >> x >> y; x--;
				mat[i][x+n*y] = 1;
				vl[i] |= 1 << (x+n*y);
			}
		}

//		forn(i, m) { forn(j, 2*n) cerr << mat[i][j] << " "; cerr << " | " << vl[i] << endl; }

		int z = 1 << (n);
		int mej = -1;
		forn(xx, z) { int x = xx | (((z-1)^xx) << n);
//			if (bone(x) > n) continue;
			bool ok = true;
			forn(i, m) ok = ok && (x&vl[i]);
			if (!ok) continue;
			if ((mej==-1) || (bone(mej>>n) > bone(x>>n))) mej = x;
		}

		if (mej == -1) {
			printf("Case #%d: IMPOSSIBLE\n", tt+1);
		} else {
			mej = mej >> n;
			vint res(n);
			forn(i, n) { res[i] = mej & 1; mej /= 2; }
			printf("Case #%d:", tt+1);
			forn(i, n) printf(" %d", res[i]);
			printf("\n");
		}
	}
	return 0;
}
