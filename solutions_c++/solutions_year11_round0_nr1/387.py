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

void go(const VI& v, int& pos) {
	if (v.back() == -1 || v.back() == pos) return;
	if (v.back() < pos) --pos; else ++pos;
}

int main() {
freopen("A-large.in", "rt", stdin);
freopen("A-large.out", "w", stdout);

	int ntc; GI(ntc);
	char buf[5];

	FORE(tc, 1, ntc) {
		VI t_o, t_b;
		VI or;

		int n; GI(n);
		FI {
			int pos;
			scanf("%s %d", buf, &pos);
			if (buf[0] == 'O') t_o.push_back(pos); else t_b.push_back(pos);
			or.push_back(buf[0] == 'O');
		}
		t_o.push_back(-1); reverse(ALL(t_o));
		t_b.push_back(-1); reverse(ALL(t_b));
		reverse(ALL(or));

		int res = 0;

		int pos_o = 1, pos_b = 1;
		while (!or.empty()) {
			++res;

			bool moved = false;
			if (or.back() && pos_o == t_o.back())
				moved = true, t_o.pop_back();
			else
				go(t_o, pos_o);


			if (!or.back() && pos_b == t_b.back())
				moved = true, t_b.pop_back();
			else
				go(t_b, pos_b);

			if (moved)or.pop_back();
		}

		printf("Case #%d: %d\n", tc, res);
	}

}
