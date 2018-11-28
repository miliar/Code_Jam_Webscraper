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
#define FORE(i,a)   for(__typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define ZERO(m)     memset(m,0,sizeof(m))
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()
#define LL          long long
#define LD          long double
#define MP          make_pair
#define PII         pair<int, int>
#define X           first
#define Y           second
#define VC          vector
#define VI          VC<int>
#define VVI         VC< VI >
#define VS          VC<string>
#define VPII        VC< PII >
#define DB(a)       cerr << #a << ": " << a << endl;

void print(VI v) {cout << "[";if (v.S) cout << v[0];FOR(i, 1, v.S) cout << ", " << v[i];cout << "]\n";}
void print(VS v) {cout << "[";if (v.S) cout << v[0];FOR(i, 1, v.S) cout << ", " << v[i];cout << "]\n";}
void print(VVI v) {cout << "[ ---";if (v.S) cout << " ", print(v[0]);FOR(i, 1, v.S) cout << " ", print(v[i]);	cout << "--- ]\n";}
void print(PII p) {cout << "{" << p.X << ", " << p.Y << "}";}
void print(VPII v) {cout << "[";if (v.S) print(v[0]);FOR(i, 1, v.S)  cout << ", ", print(v[i]);cout << "]\n";}

template<class T> string i2s(T x) {ostringstream o; o << x; return o.str(); }
VS splt(string s, char c = ' ') {VS rv; int p = 0, np; while (np = s.find(c, p), np >= 0) {if (np != p) rv.PB(s.substr(p, np - p)); p = np + 1;} if (p < s.S) rv.PB(s.substr(p)); return rv;}

int main() {
	int tc;
	cin >> tc;
	FOR(atc,1,tc+1) {
		printf("Case #%d: ", atc);
		int n, m, a;
		cin >> n >> m >> a;
		if (a > n * m) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		int x0 = 0;
		REP(x1, n + 1) REP(x2, n + 1) REP(y0, m + 1) REP(y1, m + 1) REP(y2, m + 1) {
			//x2 * y1 - x1 * y2 == (a + x2 * y1) / x2
			/*
			int v = a + x2 * (y1 - y0);
			if (x2 == 0) {
				if (v) continue;
				y2 = 0;
			} else {
				if (v % x2) continue;
				y2 = v / x2 + y0;
			}
			if (y2 < 0 || y2 > m) continue;*/
			if (x2 * (y1 - y0) - x1 * (y2 - y0) != a) continue;
			printf("%d %d %d %d %d %d\n", x0, y0, x1, y1, x2, y2);
			goto nxt;
		}
nxt: ;
	}
}
