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

int st[1001];
int isp[1001];
int main() {
	int tc;
	cin >> tc;
	memset(isp, 1, sizeof isp);
	isp[0] = isp[1] = false;
	FOR(i, 2, 1001) FOR(j, 2, i) if (i % j == 0) isp[i] = false;
	FOR(atc,1,tc+1) {
		printf("Case #%d: ", atc);
		int a, b, p;
		cin >> a >> b >> p;
		memset(st, -1, sizeof st);
		FOR(i, a, b + 1) st[i] = i;
		FOR(i, a, b + 1) FOR(k, p, i) if (isp[k] && i % k == 0) FOR(j, a, i) if (j % k == 0) {
			if (st[i] == st[j]) continue;
			int mx = st[i] >? st[j];
			int mn = st[i] <? st[j];
			REP(z, 1001) if (st[z] == mx) st[z] = mn;
		}
		set<int> s;
		FOR(z, a, b + 1) s.insert(st[z]);
		cout << s.S << endl;
	}
}
