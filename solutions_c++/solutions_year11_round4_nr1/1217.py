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

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define REP(i,a)    FOR(i,0,a)
#define ZERO(m)     memset(m,0,sizeof(m))
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()
#define LL          long long
#define LD          long double
#define MP          make_pair
#define X           first
#define Y           second
#define VC          vector
#define PII			pair <int, int>
#define VI          VC<int>
#define VPII		VC < PII >
#define VS          VC<string>
#define DB(a)		cout << #a << ": " << a << endl;

void print(VI v) {cerr << "[";if (v.S) cerr << v[0];FOR(i, 1, v.S) cerr << ", " << v[i];cerr << "]\n";}
void print(VS v) {cerr << "[";if (v.S) cerr << v[0];FOR(i, 1, v.S) cerr << ", " << v[i];cerr << "]\n";}
template<class T> string i2s(T x) {ostringstream o; o << x; return o.str(); }
VS splt(string s, char c = ' ') {VS rv; int p = 0, np; while (np = s.find(c, p), np >= 0) {if (np != p) rv.PB(s.substr(p, np - p)); p = np + 1;} if (p < s.S) rv.PB(s.substr(p)); return rv;}

int main() {
	int tc;
	cin >> tc;
	FOR(atc, 1, tc + 1) {
		LL x, s, r, t, n;
		cin >> x >> s >> r >> t >> n;
		LL xx = x;
		
		double xt = 0;
		VC < pair < int, int > > v;
		REP(i, n) {
			int a, b, c;
			cin >> a >> b >> c;
			v.PB(MP(c, b - a));
			x -= (b - a);
		}
		if (x) v.PB(MP(0, x));
		sort(ALL(v));
		
		double tt = t;
		double at = 0;
		REP(i, v.S) {
			
			
			double v0 = s + v[i].X;
			double v1 = v0 + (r - s);
			double t0 = v[i].Y / v1;
			
			//cerr << v[i].X << ' '<< v[i].Y << ' ' << v0 << ' ' << v1 << ' ' << t0 << endl;
			
			double t1 = min(t0, tt);
			tt -= t1;
			at += t1 + (v[i].Y - (t1 * v1)) / v0;
		}
		
		printf("Case #%d: %.9lf \n", atc, at);
	}
}