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

#define MX (24*60+1000)

VI v[MX];
int main() {
	int tc;
	cin >> tc;
	FOR(atc,1,tc+1) {
		REP(i, MX) v[i].clear();
		int t, na, nb;
		cin >> t >> na >> nb;
		int xa = 0, xb = 0;
		REP(i, na + nb) {
			int a,b,c,d;
			scanf("%d:%d %d:%d", &a, &b, &c, &d);
			v[a*60+b].PB(1 + (i >= na));
			v[c*60+d+t].PB(-1 - (i < na));
		}

		REP(i, MX) if (v[i].S) sort(ALL(v[i]));

		int ta = 0, tb = 0;
		REP(i, MX) REP(j, v[i].S) {
			int x = v[i][j];
			if (x == -2) tb++;
			if (x == -1) ta++;
			if (x == 1) {
				if (ta) ta--;
				else xa++;
			} 
			if (x == 2) {
				if (tb) tb--;
				else xb++;
			}
		}

		printf("Case #%d: %d %d", atc, xa, xb);
		printf("\n");
	}
}
