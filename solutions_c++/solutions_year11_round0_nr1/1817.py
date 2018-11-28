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

int rp[2];
int rt[2];
int main() {
	int tc;
	cin >> tc;
	FOR(atc, 1, tc + 1) {
		int n;
		cin >> n;
		VPII v;
		REP(i, n) {
			string s; int p;
			cin >> s >> p;
			v.PB(MP(s[0] == 'O', p));
		}
		rt[0] = rt[1] = 0;
		rp[0] = rp[1] = 1;
		REP(i, n) {
			//cout << v[i].X << ' ' << v[i].Y << endl;
			int r = v[i].X;
			rt[r] += abs(rp[r] - v[i].Y) + 1;
			rt[r] = max(rt[r], rt[1 - r] + 1);
			rp[r] = v[i].Y;
		}
		printf("Case #%d: %d\n", atc, max(rt[0], rt[1]));
	}
}