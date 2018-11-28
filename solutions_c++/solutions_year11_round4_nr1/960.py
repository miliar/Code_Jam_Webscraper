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


struct swlk {
	int d;
	int w;
};

bool operator<(const swlk& x, const swlk& y) {
	return x.w < y.w;
}

int main() {
	int tt;
	cin >> tt;
	forn(_t, tt) {
		int x,s,r,t,n;
		cin >> x >> s >> r >> t >> n;
		vector<swlk> wlk;

		int cx = 0;
		forn(i, n) {
			int b, e, w;
			cin >> b >> e >> w;
			if (b > cx) { wlk.push_back((swlk){b-cx, s}); cx = b; }
			if (e > b)  { wlk.push_back((swlk){e-b, s+w}); cx = e; }
		}
		r-=s;
		if (x > cx) { wlk.push_back((swlk){x-cx, s}); cx = x; }

//		DBG(wlk.size())
//		forn(i,wlk.size()) cerr << wlk[i].d << "|" << wlk[i].w << endl;

		sort(all(wlk));
		tdbl res = 0.0;
		tdbl ct = t;
		forn(i, wlk.size()) {
			swlk cw = wlk[i];
			if (ct * (tdbl)(cw.w + r) > (tdbl)cw.d) {
				tdbl nt = (tdbl)cw.d / (tdbl)(cw.w + r);
				ct -= nt;
				res += nt;
			} else {
				tdbl nt = 0.0;
				tdbl d = cw.d;
				if (ct > 0.0) {
					nt = ct;
					tdbl d0 = ct * (tdbl)(cw.w+r);
					d -= d0;
					ct = 0.0;
				}
				res += nt;
				res += d / (tdbl)(cw.w);
			}
		}
		printf("Case #%d: %.8lf\n", _t+1, (double)res);
	}
	return 0;
}

