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

int mat[128][128];
int vk[128][32];

#define touch(a, b, c, d) ((a == c) || (b == d) || ((a) < (c) != (b) < (d)))

int bs;
char ok[1 << 16];
int chrt[1 << 16];
#define bit(x, i) (!!((x) & (1 << (i))))


int main() {
//	freopen("perm.in", "r", stdin);

	int tt;
	cin >> tt;

	forn(t, tt) {
		int n, p;
		cin >> n >> p;
		
		forn(i, n) forn(j, p) cin >> vk[i][j];
		forn(i, n) forn(j, n) mat[i][j] = 0;
		forn(i, n) forn(j, n) if (i != j) forn(k, p-1) {
			mat[i][j] |= touch(vk[i][k], vk[i][k+1], vk[j][k], vk[j][k+1]);
		}
		
//		forn(i, n) { forn(j, n) cerr << mat[i][j]; cerr << endl; }
		forn(x, 1 << n) {
			int kk = 0;
			forn(i, n) if (bit(x, i)) forn(j, i) if (bit(x, j)) kk |= mat[i][j];
			ok[x] = !kk;
		}
		chrt[0] = 0;
		forsn(x, 1, 1 << n) {
			chrt[x] = n;
			for(int ss = x; ss; ss = (ss-1)&x) {
				if (ok[ss]) chrt[x] = min(chrt[x], chrt[x-ss]+1);
			}
		}
		int res = chrt[(1 << n)-1];
		printf("Case #%d: %d\n", t+1, res);
	}
	return 0;
}
