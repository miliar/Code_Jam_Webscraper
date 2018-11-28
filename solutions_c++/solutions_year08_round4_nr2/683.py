#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <map>
#include <queue>
#include <set>
#include <functional>

using namespace std;

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

typedef pair<int, int> PI;
typedef vector<PI> VPI;

int X, Y, A;
int x1, y2, x3, y3;

int sum(int x1, int y1, int x2, int y2) {
	return x1*y2-x2*y1;
}

struct Task {
	
	void input() {
		cin >> X >> Y >> A;	
	}
	int solve() {
		for (x1 = 0; x1 <= X; ++x1)
			for(y2 = x1 ? 0 : 1; y2 <= Y; ++y2) {
				for (x3= 0; x3 <= X; ++x3)
					for (y3= 0; y3 <= Y; ++y3) {
						int a = sum(x1, 0, 0, y2) + sum(0, y2, x3, y3) + sum(x3, y3, x1, 0);
						a = abs(a);
						if (a == A) return true;
					}
			}


			return false;
	}
};



int main() {
freopen("B-small-attempt0.in", "rt", stdin);
//	freopen("B.in", "rt", stdin);
freopen("B-small-attempt0.out", "w", stdout);

	int tc; cin >>tc;
	REP(TC, tc) {
		Task t;
		t.input();
		int res = t.solve();
		if (!res) 
			printf("Case #%d: IMPOSSIBLE\n", TC+1, res);
		else
			printf("Case #%d: %d %d %d %d %d %d\n", TC+1, x1, 0, 0, y2, x3, y3);
	}

fclose(stdout);
}
