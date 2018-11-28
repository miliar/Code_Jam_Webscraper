// Adrian Kügel
#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <map>
#include <assert.h>
#include <limits.h>
#include <complex>
#include <algorithm>
#include <ctype.h>
#include <string>
using namespace std;

typedef set<int> SI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef complex<double> tComp;
typedef pair<short, int> PCI;

int p[100][25];
VI adj[100];
char visit[100];
int comp;

void dfs(int cur) {
	if (visit[cur])
		return;
	visit[cur] = comp;
	for (VI::iterator it=adj[cur].begin(); it!=adj[cur].end(); ++it)
		dfs(*it);
}

int maxc, minc, n;
int col[100], ncols[100];
int cnt[100][100];
void backtrack(int cols) {
	if (cols >= minc || minc <= maxc)
		return;
	int bcols = -1, bcnt, ind;
	for (int i=0; i<n; ++i)
		if (visit[i] == comp && col[i] < 0 && (ncols[i] > bcols/* || ncols[i] == bcols && adj[i].size() > bcnt*/)) {
			bcnt = adj[i].size();
			bcols = ncols[i];
			ind = i;
		}
	if (bcols < 0) {
		minc = cols;
		return;
	}
	for (int i=0; i<=cols; ++i) {
		if (cnt[ind][i] == 0) {
			col[ind] = i;
			for (VI::iterator it=adj[ind].begin(); it!=adj[ind].end(); ++it)
				if (++cnt[*it][i] == 1)
					++ncols[*it];
			backtrack(cols + (i == cols));
			for (VI::iterator it=adj[ind].begin(); it!=adj[ind].end(); ++it)
				if (--cnt[*it][i] == 0)
					--ncols[*it];
		}
	}
	col[ind] = -1;
}

int main() {
	int tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		int k;
		scanf("%d %d", &n, &k);
		for (int i=0; i<n; ++i) {
			adj[i].clear();
			visit[i] = 0;
			col[i] = -1;
			ncols[i] = 0;
			memset(cnt[i], 0, n*sizeof(int));
		}
		for (int i=0; i<n; ++i)
			for (int j=0; j<k; ++j)
				scanf("%d", &p[i][j]);
		for (int i=0; i<n; ++i)
			for (int j=0; j<n; ++j) {
				if (i == j)
					continue;
				bool inters = false;
				for (int ii=1; ii<k; ++ii)
					if (p[i][ii-1] == p[j][ii-1] || p[i][ii] == p[j][ii]
							|| (p[i][ii-1] < p[j][ii-1]) != (p[i][ii] < p[j][ii])) {
						inters = true;
						break;
					}
				if (inters)
					adj[i].push_back(j);
			}
		maxc = 0;
		comp = 0;
		for (int i=0; i<n; ++i)
			if (!visit[i]) {
				++comp;
				dfs(i);
				minc = n;
				backtrack(0);
				maxc = max(maxc, minc);
			}
		printf("%d\n", maxc);
	}
	return 0;
}
