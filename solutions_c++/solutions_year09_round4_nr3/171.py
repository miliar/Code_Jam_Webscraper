#include <iostream>
#include <vector>
#include <string>
#include <memory.h>
#include <algorithm>
#include <set>
#include <queue>
#include <sstream>
#include <list>
#include <map>
#include <cmath>

#include <memory.h>

using namespace std;

#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define FORE(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define FIR(k) FOR(i,0,k)
#define FJR(k) FOR(j,0,k)
#define FI FIR(n)
#define FJ FJR(n)
#define ALL(v) v.begin(), v.end()
#define LL long long

typedef vector<int> VI;
typedef pair<int, int> PI;


VI st[104];
int n;
int q[105][105];
int vis[105], back[105];

bool dfs_match(int v) {
	if (vis[v]) return false;
	vis[v] = true;
	FI if (q[v][i])
		if (back[i] == -1 || dfs_match(back[i])) {
			back[i] = v;
			return true;
		}
	return false;
}

int main() {
static const string FILENAME = "C-large";
freopen((FILENAME + ".in").c_str(), "rt", stdin);
freopen((FILENAME + ".out").c_str(), "w", stdout);	
	
	int ncase; cin >> ncase;
	FORE(caze, 1, ncase) {
		int k;
		cin >> n >> k;
		FI { 
			st[i].clear();
			st[i].resize(k);
			FJR(k) cin >> st[i][j];
		}
		memset(q, 0, sizeof q);
		FI FJ {
			int v = 1;
			FOR(t, 0,k) if (st[i][t] >= st[j][t]) v = 0;
			q[i][j] = v;
		}

		int m = 0;
		memset(back, -1, sizeof back);
		FI {
			memset(vis, 0, sizeof vis);
			if (dfs_match(i)) 
				++m;
		}
		int res = n-m;

		printf("Case #%d: %d\n", caze, res);
	}

}