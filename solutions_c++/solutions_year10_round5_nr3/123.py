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

int x[2500000];
int vs[2500000];
int main() {
	int tc;
	cin >> tc;
	FOR(atc, 1, tc + 1) {
		ZERO(x);
		int n;
		VI v;
		cin >> n;
		ZERO(vs);
		REP(i, n) {
			int a, b;
			cin >> a >> b;
			x[a + 1100000] += b;
			v.PB(a + 1100000);
			vs[a + 1100000] = 1;
		}
		int no = 0;
		while (v.S) {
			int a = v[v.S - 1];
			v.pop_back();
			vs[a] = 0;
			if (x[a] < 2) continue;
			no += x[a] / 2;
			x[a-1] += x[a] / 2;
			x[a+1] += x[a] / 2;
			x[a] %= 2;
			v.PB(a-1), vs[a-1] = 1;
			v.PB(a+1), vs[a+1] = 1;
		}
		printf("Case #%d: %d\n", atc, no);
	}
}