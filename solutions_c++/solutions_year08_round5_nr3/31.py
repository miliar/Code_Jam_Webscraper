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

int dp[1<<10][11];
int sx, sy;
string mp[10];
int main() {
	int tc;
	cin >> tc;
	FOR(atc,1,tc+1) {
		printf("Case #%d: ", atc);
		cin >> sy >> sx;
		REP(i, sy) cin >> mp[i];
		ZERO(dp);
		REP(i, sy) REP(s1, 1 << sx) REP(s2, 1 << sx) {
			int no = 0;
			REP(j, sx) if (mp[i][j] == 'x' && (s2 & (1 << j))) goto nxt;
			FOR(j, 1, sx) if ((s1 & (1 << j)) && (s2 & (1 << (j - 1)))) goto nxt;
			REP(j, sx - 1) if ((s1 & (1 << j)) && (s2 & (1 << (j + 1)))) goto nxt;
			REP(j, sx - 1) if ((s2 & (1 << j)) && (s2 & (1 << (j + 1)))) goto nxt;
			REP(j, sx) if (s2 & (1 << j)) no++;
			dp[s2][i+1] >?= dp[s1][i] + no;
			nxt: ;
		}
		int mx = 0;
		REP(s, 1 << sx) mx >?= dp[s][sy];
		cout << mx << endl;
	}
}
