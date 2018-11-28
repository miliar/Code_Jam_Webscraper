#include <vector>
#include <map>
#include <set>
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

#define INF 10000000

#define MAXMEM 1000
tint _comb[MAXMEM][MAXMEM];
tint comb(tint n, tint m) {
  if (m<0||m>n)return 0;if(m==0||m==n)return 1;
  if (n >= MAXMEM) return comb(n-1,m-1)+comb(n-1,m);
  tint& r = _comb[n][m];
  if (r == -1) r = comb(n-1,m-1)+comb(n-1,m);
  return r;
}

struct pto {
	int i, j;
	pto() : i(0), j(0) {}
	pto(int ii, int jj) : i(ii), j(jj) {}
	bool operator<(const pto& o) const { if (i != o.i) return i < o.i; return j < o.j; }
};

int mp[128][128];

int main() {
	int T;
	cin >> T;
	forn(tt, T) {
		memset(mp, 0x3f, sizeof(mp));
		int mi, mj, R;
		cin >> mi >> mj >> R;
		forn(i, R) {
			int i, j;
			cin >> i >> j; i--; j--;
			mp[i][j] = 0;
		}
		mp[0][0] = 1;
		forn(i, mi) forn(j, mj) if (mp[i][j] == 0x3f3f3f3f) {
			mp[i][j] = 0;
			if (i>0 && j>1) mp[i][j] += mp[i-1][j-2];
			if (i>1 && j>0) mp[i][j] += mp[i-2][j-1];
			mp[i][j] = mp[i][j] % 10007;
		}
//		forn(i, mi) { forn(j, mj) cerr << mp[i][j] << " "; cerr << endl; }
		int res = mp[mi-1][mj-1];
		cout << "Case #" <<  tt+1 << ": " << res << endl;
//		printf("Case #%d: %ld\n", tt+1, res);
	}

	return 0;
}
