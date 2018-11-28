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

#define IMP " Impossible"

int main() {
	int tc;
	cin >> tc;
	FOR(atc, 1, tc + 1) {
		int n; cin >> n;
		VI v(n); REP(i, n - 1) cin >> v[i];
		REP(i, n -1 )v[i]--;
		
		printf("Case #%d:", atc);
		
		int mx, mn;
		VI h(n);
		int tries = 0;
		again: ;
		tries++;
		if (tries >= 100000) {
			cout << IMP;
			goto nexttest;
		}
		h[n-1] = h[n-2] = 0;
		
		
		mn = 0, mx = 0;
		for (int i = n - 3; i >= 0; i--) {
			int bd = rand() % 20 - 10;
			bool ok = false;
			int bh = 0;
			FOR(j, mn - 10, mx + 11) {
				LL h0 = h[v[i]] - j;
				LL d0 = v[i] - i;
				FOR(k, i + 1, n) {
					LL h1 = h[k] - j;
					LL d1 = k - i;
					if (h1 * d0 > h0 * d1 || h1 * d0 == h0 * d1 && k < v[i]) goto next;
				}
				if (!ok) {
					bh = j;
					ok = true;
				} else {
					
					if (abs(j - h[i+1] + bd) < abs(bh - h[i+1] + bd))
						bh = j;
				}
				next: ;
			}
			if (!ok) {
				goto again;
			}
			h[i] = bh;
			mn = min(mn, bh);
			mx = max(mx, bh);
		}
		
		REP(i, n) printf(" %d", h[i] - mn);
		
		nexttest: ;
		cout << endl;
	}
}