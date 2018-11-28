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

int no[1<<21];
int main() {
	int tc;
	cin >> tc;
	FOR(atc,1,tc+1) {
		printf("Case #%d: ", atc);
		int n, dn;
		VI d;
		cin >> n >> dn;
		REP(i, dn) {
			int x;
			cin >> x;
			d.PB(x);
		}

		ZERO(no);
		REP(i, n) {
			int p = (1<<20)+i;
			while (p) {
				no[p]++;
				p /= 2;
			}
		}

		VI deck(n, 0);
		int ap = 0;
		REP(i, n) {
			deck[ap] = i + 1;
			if (i == n - 1) break;
			int t = i + 1;
			int p = (1<<20) + ap;
			while (p) {
				no[p]--;
				p /= 2;
			}
			p = (1<<20) + ap;
			while (p > 1) {
				if (p & 1) t += no[p - 1];
				p /= 2;
			}
			t %= (n - i - 1);
			ap = 0;
			p = 1;
			while (p < (1<<20)) {
				p *= 2;
				if (no[p] <= t) {
					t -= no[p++];
				}
			}
			ap = p - (1 << 20);
		}
		REP(i, dn) cout << deck[d[i] - 1] << ' ';
		cout << endl;
	}
}
