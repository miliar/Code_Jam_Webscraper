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
#define VI          VC<int>
#define VS          VC<string>
#define DB(a)		cout << #a << ": " << a << endl;

void print(VI v) {cerr << "[";if (v.S) cerr << v[0];FOR(i, 1, v.S) cerr << ", " << v[i];cerr << "]\n";}
void print(VS v) {cerr << "[";if (v.S) cerr << v[0];FOR(i, 1, v.S) cerr << ", " << v[i];cerr << "]\n";}
template<class T> string i2s(T x) {ostringstream o; o << x; return o.str(); }
VS splt(string s, char c = ' ') {VS rv; int p = 0, np; while (np = s.find(c, p), np >= 0) {if (np != p) rv.PB(s.substr(p, np - p)); p = np + 1;} if (p < s.S) rv.PB(s.substr(p)); return rv;}

#define BAD "IMPOSSIBLE"
#define MX 1110000
int dp[MX];
int main() {
	int tc;
	cin >> tc;
	FOR(atc, 1, tc + 1) {
		LL d;
		int n;
		VI v;
		cin >> d >> n;
		REP(i, n) {
			int a;
			cin >> a;
			v.PB(a);
		}
		sort(ALL(v));
		memset(dp, 0x3f, sizeof dp);
		dp[0] = 0;
		REP(i, MX) REP(j, n) if (i + v[j] < MX) 
			dp[i + v[j]] <?= dp[i] + 1;
			
		LL rv = 0;
		LL z = v[v.S - 1];
		LL no = (d - MX + 1000) / z;
		rv += no;
		d -= no * z;
		if (dp[d] > MX) rv = -1; else rv += dp[d];
		
		
		printf("Case #%d: ", atc);
		if (rv <= 0) cout << BAD;
		else cout << rv;
		cout << endl;
	}
}