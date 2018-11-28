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


int mp[512][512];

int rs[512][512];
int rse[512][512];
int ars[512][512];
int arse[512][512];

int cs[512][512];
int cse[512][512];
int acs[512][512];
int acse[512][512];

int main() {
	int tt;
	cin >> tt;
	forn(_t, tt) {
		int res = 0;
		int r,c,d;
		cin >> r >> c >> d;
		forn(i,r) forn(j,c) { char _; cin >> _; mp[i][j] = _-'0'; }

		// cerr << r << c << d << endl;
		//forn(i, r) { forn(j, c) cerr << mp[i][j] << " "; cerr << endl; }
		#define DBGm(rse) cerr << #rse << endl; forn(i, r+1) { forn(j, c+1) cerr << rse[i][j] << " "; cerr << endl; }
		
		forn(i, r+1) {
			int xs = 0; forn(j, c+1) { rs[i][j] = xs; xs += mp[i][j]; }
			int xse = 0; forn(j, c+1) { rse[i][j] = xse; xse += mp[i][j] * j; }
		}
		forn(j, c+1) {
			int xs = 0; forn(i, r+1) { cs[i][j] = xs; xs += mp[i][j]; }
			int xse = 0; forn(i, r+1) { cse[i][j] = xse; xse += mp[i][j] * i; }
		}
		forn(j, c+1) {
			int acc = 0; forn(i, r+1) { ars[i][j] = acc; acc += rs[i][j]; }
			int acce = 0; forn(i, r+1) { arse[i][j] = acce; acce += rse[i][j]; }
		}
		forn(i, r+1) {
			int acc = 0; forn(j, c+1) { acs[i][j] = acc; acc += cs[i][j]; }
			int acce = 0; forn(j, c+1) { acse[i][j] = acce; acce += cse[i][j]; }
		}

		// DBGm(rse) DBGm(rs) DBGm(arse) DBGm(ars)

		forn(i, r) if (r-i > res) forn(j, c) {
			int mk = min(r-i, c-j)+1;
			for(int k = max(3,res+1); k < mk; k++) {
				// msr = 2*(rse[i][j+k]-rse[i][j]) - (rs[j+k]-rs[j]) * (j+j+k-1);
				int dk = k-1;
				int msr =
					(2*( (arse[i+k][j+k]-arse[i  ][j+k]) - (arse[i+k][j]-arse[i  ][j]) )
					- ( (ars[i+k][j+k]-ars[i  ][j+k]) - (ars[i+k][j]-ars[i  ][j]) ) * (j+j+k-1))
					- dk * (-mp[i][j] - mp[i+dk][j] + mp[i][j+dk] + mp[i+dk][j+dk]);
				// cerr << "msr " << i << " " << j << " " << k << " " << msr << endl;
				// cerr << "r sum "; forn(l, k) cerr << (2*(rse[i+l][j+k]-rse[i+l][j]) - (rs[i+l][j+k]-rs[i+l][j]) * (j+j+k-1)) << " ";
				// cerr << " | " << dk * (-mp[i][j] - mp[i+dk][j] + mp[i][j+dk] + mp[i+dk][j+dk]) << endl;
				if (msr) continue;

				int msc =
					(2*(acse[i+k][j+k]-acse[i  ][j+k]) - (acs[i+k][j+k]-acs[i  ][j+k]) * (i+i+k-1)) -
					(2*(acse[i+k][j  ]-acse[i  ][j  ]) - (acs[i+k][j  ]-acs[i  ][j  ]) * (i+i+k-1))
					- dk * (-mp[i][j] + mp[i+dk][j] - mp[i][j+dk] + mp[i+dk][j+dk]);
				// cerr << "msc " << i << " " << j << " " << k << " " << msc << endl;
				if (msc) continue;
				res = k;
			}
		}

		if (res < 3) {
			printf("Case #%d: IMPOSSIBLE\n", _t+1);
		} else {
			printf("Case #%d: %d\n", _t+1, res);
		}
	}
	return 0;
}

