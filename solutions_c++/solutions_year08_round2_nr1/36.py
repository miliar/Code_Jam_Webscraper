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

LL v[3][3];
int main() {
	int tc;
	cin >> tc;
	FOR(atc,1,tc+1) {
		ZERO(v);
		printf("Case #%d: ", atc);
		LL a, b, c, d, x, y, m;
		LL n;
		cin >> n >> a >> b >> c>> d >> x >> y >> m;
		REP(i, n) {
			v[x % 3][y % 3]++;
			x = (a * x + b) % m;
			y = (c * y + d) % m;
		}
		LL tt = 0;
		REP(i, 9) REP(j, i + 1) REP(k, j + 1) {
			int x1 = i % 3, x2 = j % 3, x3 = k % 3;
			int y1 = i / 3, y2 = j / 3, y3 = k / 3;
			if ((x1 + x2 + x3) % 3 || (y1 + y2 + y3) % 3) continue;
			if (i == j && j == k) tt += v[x1][y1] * (v[x1][y1] - 1) * (v[x1][y1] - 2) / 6;
			else if (i == j) tt += v[x1][y1] * (v[x1][y1] - 1) / 2 * v[x3][y3];
			else if (i == k) tt += v[x1][y1] * (v[x1][y1] - 1) / 2 * v[x2][y2];
			else if (k == j) tt += v[x2][y2] * (v[x2][y2] - 1) / 2 * v[x1][y1];
			else tt += v[x1][y1] * v[x2][y2] * v[x3][y3];
			//cout << i << ' ' << j << ' ' << k << ' ' << tt << endl;
		}
		cout << tt << endl;
	}
}
