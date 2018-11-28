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
		int n, s, p;
		cin >> n >> s >> p;
		int t0 = 0, t1 = 0, t2 = 0;
		REP(i, n) {
			int x;
			cin >> x;
			int t = 0;
			REP(a, 11) FOR(b, max(0, a - 2), min(11, a + 3)) FOR(c, max(0, max(a, b) - 2), min(11, min(a, b) + 3)) if (a + b + c == x) {
				int sp = abs(a - b) == 2 || abs(a - c) == 2 || abs(b - c) == 2;
				int bg = max(max(a, b), c) >= p;
				t = max(t, (!bg ? 0 : sp ? 1 : 2));
			}
			if (t == 0) t0++; else if (t == 1) t1++; else t2++;
		}
		
		int rv = t2 + min(t1, s);
		printf("Case #%d: %d\n", atc, rv);
	}
}