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

int dp[2][30000];
int g[30000];
int c[30000];
int n, v, n1;

int go(int a, int b) {
	int &rv = dp[b][a];
	if (rv != -1) return rv;
	if (a >= n1) return rv = g[a] == b ? 0 : (1 << 20);
	rv = 1 << 20;
	if (g[a] == 0 || c[a]) {
		if (b == 0) {
			rv <?= (g[a] != 0) + go(a*2+1,0) + go(a*2+2,0);
		} else {
			rv <?= (g[a] != 0) + go(a*2+1,1) + go(a*2+2,0);
			rv <?= (g[a] != 0) + go(a*2+1,1) + go(a*2+2,1);
			rv <?= (g[a] != 0) + go(a*2+1,0) + go(a*2+2,1);
		}
	}
	if (g[a] == 1 || c[a]) {
		if (b == 1) {
			rv <?= (g[a] != 1) + go(a*2+1,1) + go(a*2+2,1);
		} else {
			rv <?= (g[a] != 1) + go(a*2+1,1) + go(a*2+2,0);
			rv <?= (g[a] != 1) + go(a*2+1,0) + go(a*2+2,0);
			rv <?= (g[a] != 1) + go(a*2+1,0) + go(a*2+2,1);
		}
	}

	return rv;
}

int main() {
	int tc;
	cin >> tc;
	FOR(atc,1,tc+1) {
		printf("Case #%d: ", atc);
		cin >> n >> v;
		n1 = (n - 1) / 2;
		REP(i, n1) cin >> g[i] >> c[i];
		REP(i, n - n1) cin >> g[i + n1];
		memset(dp, -1, sizeof dp);
		int a = go(0, v);
		if (a >= (1<<20)) {
			cout << "IMPOSSIBLE";
		} else 
			cout << a;
		cout << endl;
	}
}
