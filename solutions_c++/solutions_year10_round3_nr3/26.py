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

int n,m;
int cd[512][512];
int mp[512][512];
int us[512][512];

inline int get(int i, int j);
inline int get(int i, int j) {
	int cnd = min(cd[i][j], m-i);
	int lp = mp[i][j];
	for(int k=i; k-i < cnd; k++) {
		if (cd[k][j] < k-i+1 || mp[k][j] != lp) return k-i;
		cnd = min(cnd, cd[k][j]);
		lp ^= 1;
	}
	return cnd;
}

void status() {
	cerr << endl << "cd | get" << endl;
	forn(i, m) { 
		forn(j, n) fprintf(stderr, "%2d ", cd[i][j]);
		fprintf(stderr, "  |  ");
		forn(j, n) fprintf(stderr, "%2d ", get(i, j));
		fprintf(stderr, "  |  ");
		forn(j, n) fprintf(stderr, "%2d ", us[i][j]);
		fprintf(stderr, "\n");
	}
}

void pone(int i, int j, int k) {
	bool ok = 1;
	forn(ki, k) forn(kj, k-1) ok = ok && (mp[i+ki][j+kj] != mp[i+ki][j+kj+1]);
	forn(ki, k-1) forn(kj, k) ok = ok && (mp[i+ki][j+kj] != mp[i+ki+1][j+kj]);
	if (!ok) {
		cerr << "No es damero!" << endl;
		cerr << "(" << i << ", " << j << ") size " << k << endl;
		forn(ki, k) { forn(kj, k) cerr << ".x"[mp[i+ki][j+kj]]; cerr << endl; }
		
		status();
		exit(1);
	}
	forn(ki, k) forn(kj, k) {
		if (us[i+ki][j+kj]) {
			cerr << "Repite cuadrado!" << endl;
			cerr << "(" << i << ", " << j << ") size " << k << endl;
			
			status();
			exit(1);
		}
		us[i+ki][j+kj] = k;
	}
}

int main() {
	int tt;
	cin >> tt;
	forn(t, tt) {
		cin >> m >> n;
		
		forn(i, m) forn(j, n/4) { char x; cin >> x; int v = (x<='9')?x-'0':(x-'A'+10); forn(k, 4) mp[i][4*j+k] = (v >> (3-k)) & 1; }
		
//		forn(i, m) { forn(j, n) cerr << ".x"[mp[i][j]]; cerr << endl; }
		
		forn(i, m) {
			int mx = 0;
			dforn(j, n) {
				if (j+1<n && mp[i][j+1] != mp[i][j]) mx++; else mx = 1;
				cd[i][j] = mx;
			}
		}

//		memset(us, 0, sizeof(us));


		vector<pint> res;
		while(1) {
			
			int mx = 0;
			forn(i, m) forn(j, n) mx = max(mx, get(i, j));
			if (!mx) break;
			int cnt = 0;

//			DBG(mx) status();

//			if (mx == 1) {
//				forn(i, m) forn(j, n) if (cd[i][j] > 0) { cnt++; cd[i][j] = 0; }
//			} else {
				forn(i, m) forn(j, n) if (mx == get(i, j)) {
	//				pone(i, j, mx);
					cnt++;
					forsn(ki, i, i+mx) {
						forsn(kj, j, j+mx) cd[ki][kj] = 0;
						int q = 1;
						for(int kj = j-1; kj >= 0 && cd[ki][kj] > 1; kj--) cd[ki][kj] = q++;
					}
				}
//			}
			
			
			res.push_back(pint(mx, cnt));
		}

		cout << "Case #" << (t+1) << ": " << res.size() << endl;
		forall(it, res) cout << it->first << " " << it->second << endl;
	}
	return 0;
}

