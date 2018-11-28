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
typedef vector<int> VI;

VI g[2000];
int malted[2000];
int cnt[2000];
int st[2000];

struct Task {
	
	int n, m;

	void input() {
		cin >> n >> m;
		memset(st, 0, sizeof st);
		memset(cnt, 0, sizeof cnt);
		memset(malted, -1, sizeof malted);

		int x, y, t;
		FIR(m) {
			cin >> t;
			FJR(t) {
				cin >> x >> y;
				--x;
				if (y) malted[i] = x;
				else {
					g[i].push_back(x);
					++cnt[i];
				}
			}

			sort(ALL(g[i]));
		}
	}
	bool solve() {
		bool change;
		bool res = true;
		do {
			change = false;
			FIR(m) {
				if(!cnt[i] && (malted[i] == -1 || !st[malted[i]])) {
					if(malted[i] == -1) {
						res = false;
						break;
					}

					st[malted[i]] = 1;
					change = true;
					FJR(m) {
						VI::iterator it = lower_bound(ALL(g[j]), malted[i]);
						if (it != g[j].end() && *it == malted[i]) {
							g[j].erase(it);
							--cnt[j];
						}
					}
				}
			}
		
			if (!res) break;
		} while (change);

		FIR(m) g[i].clear();
		return res;
	}
};

int main() {
freopen("B-large.in", "rt", stdin);
freopen("B-large.out", "w", stdout);

	int tc; cin >>tc;
	REP(TC, tc) {
		Task t;
		t.input();
		int res = t.solve();

		if (res) {
			printf("Case #%d:", TC+1);
			FIR(t.n) printf(" %d", st[i]);
			printf("\n");
		} else
			printf("Case #%d: IMPOSSIBLE\n", TC+1);
	}

fclose(stdout);
}
