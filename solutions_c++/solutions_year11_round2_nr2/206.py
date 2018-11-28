#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <queue>

using namespace std;

#define LL          long long
#define FOR(i,a,b)  for(LL i=(a);i<(b);++i)
#define REP(i,a)    FOR(i,0,a)
#define ZERO(m)     memset(m,0,sizeof(m))
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()
#define LD          long double
#define MP          make_pair
#define X           first
#define Y           second
#define VC          vector
#define PII			pair <LL, LL>
#define VI          VC<int>
#define VPII		VC < PII >
#define VS          VC<string>
#define DB(a)		cout << #a << ": " << a << endl;

void print(VI v) {cerr << "[";if (v.S) cerr << v[0];FOR(i, 1, v.S) cerr << ", " << v[i];cerr << "]\n";}
void print(VS v) {cerr << "[";if (v.S) cerr << v[0];FOR(i, 1, v.S) cerr << ", " << v[i];cerr << "]\n";}
template<class T> string i2s(T x) {ostringstream o; o << x; return o.str(); }
VS splt(string s, char c = ' ') {VS rv; int p = 0, np; while (np = s.find(c, p), np >= 0) {if (np != p) rv.PB(s.substr(p, np - p)); p = np + 1;} if (p < s.S) rv.PB(s.substr(p)); return rv;}

int n;
LL d;
VPII v;

int check(LL x) {
	if (x < 0) return 0;
	LL a = -(1ll << 50);
	REP(i, n) {
		LL p = max(v[i].X - x, a + d);
		LL r = p + (v[i].Y - 1) * d;
		if (r > v[i].X + x) return 0;
		a = r;
	}
	return 1;
}

int main() {
	int tc;
	cin >> tc;
	FOR(atc, 1, tc + 1) {
		cin >> n >> d;
		v.clear();
		REP(i, n) {
			LL a, b; cin >> a >> b;
			a *= 2;
			v.PB(MP(a,b));
		}
		d *= 2;
		sort(ALL(v));
		
		LL l = 0, r = 1ll << 50;
		while (r - l > 5) {
			LL s = (l+r)/2;
			if (check(s)) r = s; else l = s;
		}
		
		LL rv = -1;
		FOR(i, l - 5, r + 5) if (check(i)) {
			rv = i;
			break;
		}
		
		LD drv = (LD)rv / 2;
		printf("Case #%d: ", atc);
		printf("%.7Lf\n", drv);
	}
}