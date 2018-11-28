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

VPII v[310];
int n;
/*
int go (int p, int c0, int c1) {
	int &rv = dp[p][c0][c1];
	if (rv != -1) return rv;
	if (
}*/

int test(int a, int b, int c) {
	int pa = 0, pb = 0, pc = 0;
	int tt = 0;
	int mx = 0;
	int ok = 0;
	while (true) {
		int bb = -1; PII p = MP(1<<20,0);
		if (pa < v[a].S && v[a][pa] < p) p = v[a][pa], bb = 0;
		if (pb < v[b].S && v[b][pb] < p) p = v[b][pb], bb = 1;
		if (pc < v[c].S && v[c][pc] < p) p = v[c][pc], bb = 2;
		p.Y = -p.Y;
		if (bb == -1) break;
		if (bb == 0) pa++; else if (bb == 1) pb++; else pc++;
		if (p.X > mx + 1) return 1000;
		if (p.X == ok + 1) mx >?= p.Y;
		if (p.X > ok) tt++, ok = mx;
		mx >?= p.Y;
	}
	if (mx < 10000) return 1000;
	if (ok < 10000) tt++;
	return tt;
}

int main() {
	int tc;
	cin >> tc;
	
	REP(atc, tc) {
		printf("Case #%d: ", atc + 1);
		cin >> n;
		map<string, int > mp;
		int cno = 0;
		REP(i, 310) v[i].clear();
		REP(i, n) {
			string s;
			int a, b;
			cin >> s >> a >> b;//sa[i] >> sb[i];
			if (mp.count(s) == 0) mp[s] = cno++;
			v[mp[s]].PB(MP(a, -b));
		}
		REP(i, cno) sort(ALL(v[i]));
		int b = 1000;
		REP(i, cno) b <?= test(i, cno, cno);
		REP(i, cno) REP(j, i) b <?= test(i, j, cno);
		REP(i, cno) REP(j, i) REP(k, j) b <?= test(i, j, k);

		if (b >= 1000) cout << "IMPOSSIBLE" << endl; else cout << b << endl;

	}
}
