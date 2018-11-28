#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <queue>
#include <memory.h>

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PI;
typedef vector<PI> VPI;

#define FOR(i,a,n) for (int i = (a); i < (n); ++i)
#define FORE(i,a,n) for (int i = (a); i <= (n); ++i)
#define FORD(i,a,b) for (int i = (a); i >= (b); --i)
#define REP(i,n) FOR(i,0,n)
#define REPE(i,n) FORE(i,0,n)
#define LL long long
#define FIR(n) REP(i,n)
#define FJR(n) REP(j,n)
#define ALL(v) v.begin(), v.end()

#define FI FIR(n)
#define FJ FJR(n)
#define FR(i,a) FOR(i,a,n)
#define REPN(i) REP(i,n)

#define GI(n) scanf("%d", &n)
#define GI2(n,m) scanf("%d %d", &n, &m)

double X, S, R, t;
int n;

vector<pair<int, PI> >v;
VPI vl;

int main() {
freopen("A-large.in", "rt", stdin);
//freopen("A-large.out", "w", stdout);

	int ntc; GI(ntc);
	
	FORE(tc, 1, ntc) {
		cin >> X >> S >> R >> t >> n;
		int w, B, E;
		FI {

			cin >> B >> E >> w;
			v.push_back(make_pair(w, PI(B, E)));
			vl.push_back(PI(B, E));
		}

		vl.push_back(PI(X, X));
		sort(ALL(vl));
		int last = 0;
		FIR(vl.size()) {
			if (last != vl[i].first) {
				v.push_back(make_pair(0, PI(last, vl[i].first)));
			}
			last = vl[i].second;
		}

		sort(ALL(v));
		double res = 0;
		FIR(v.size()) {
			double len = v[i].second.second - v[i].second.first;
			double w = v[i].first;
			double nt = min(t, len / (R+w));

			res += nt + (len - nt*(R+w)) / (S+w);
			t -= nt;
		}


		v.clear();
		vl.clear();
		printf("Case #%d: %.9lf\n", tc, res);
	}
}
