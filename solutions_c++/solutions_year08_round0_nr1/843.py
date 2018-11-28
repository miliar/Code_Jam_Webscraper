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

VS sn;
VI qn;
int a, b;
int dp[1002][1002];
int go(int x, int y) {
	int &rv = dp[x][y];
	if (rv != -1) return rv;
	if (y == b) return rv = 0;
	if (qn[y] == x) {
		rv = 1 << 28;
		REP(i, a) if (i != x) rv <?= 1 + go(i, y + 1);
	} else {
		rv = go(x, y + 1);
	}
	return rv;
}

string readLine() {
	string s;
	getline(cin, s);
	while (s.S && (s[s.S-1] == '\r' || s[s.S-1] == '\n')) s = s.substr(0, s.S - 1);
	return s;
}

int main() {
	int tc;
	cin >> tc;
	readLine();
	FOR(atc, 1, tc + 1) {
		cin >> a;
		sn.clear();
		qn.clear();
		readLine();
		REP(i, a) {
			sn.PB(readLine());
		}
		cin >> b;
		readLine();
		REP(i, b) {
			string x = readLine();
			REP(j, a) if (x == sn[j]) qn.PB(j);
		}
		int mn = 1 << 28;
		memset(dp, -1, sizeof dp);
		REP(i, a) mn <?= go(i, 0);
		printf("Case #%d: ", atc);
		cout << mn;
		printf("\n");
	}
}
