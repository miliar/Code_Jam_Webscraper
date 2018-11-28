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

int a[1024];
int u[1024];

int main() {
freopen("D-large.in", "rt", stdin);
//freopen("D-large.out", "w", stdout);

	int ntc; GI(ntc);
	
	FORE(tc, 1, ntc) {
		int n; GI(n);
		FI GI(a[i]); FI --a[i];

		VI cl;
		memset(u, 0, sizeof u);

		FI if (!u[i]) {
			int len = 0;
			int next = i;
			while (!u[next]) {
				++len;
				u[next] = 1;
				next = a[next];
			}

			cl.push_back(len);
		}

		int res = 0;

		FIR(cl.size()) if (cl[i] > 1) res += cl[i];

		printf("Case #%d: %d.000000\n", tc, res);
	}

}
