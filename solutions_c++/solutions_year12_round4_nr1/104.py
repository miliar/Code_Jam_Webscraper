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
		int n;
		cin >> n;
		VPII v(n);
		REP(i, n) cin >> v[i].X >> v[i].Y;
		sort(ALL(v));
		
		int d; cin >> d;
		VI ok(n + 1);
		ok[0] = min(v[0].X, v[0].Y);
		
		REP(i, n) if (ok[i]) {
			ok[i] = min(ok[i], v[i].Y);
			FOR(j, i + 1, n) {
				if (v[j].X > v[i].X + ok[i]) break;
				ok[j] = max(ok[j], v[j].X - v[i].X);
			}
			ok[n] |= (v[i].X + ok[i]) >= d;
		}
		
		//print(ok);
		

		printf("Case #%d: %s\n", atc, ok[n] ? "YES" : "NO");
	}
}