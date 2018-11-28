#pragma comment(linker, "/STACK:500000000")
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#define E(c) cerr<<#c
#define Eo(x) cerr<<#x<<" = "<<(x)<<endl

const int SIZE = 6<<10;
const int CNT = 10<<10;

typedef pair<int, int> pii;

int dir[6][2] = {{1,0},{-1,0},{0,1},{0,-1},{1,1},{-1,-1}};

int n, m;
short matr[SIZE][SIZE];
int arr[CNT][2];

vector<pii> verts[6], edges[6], all;
map<pii, int> vertind, edgeind;

inline bool good(int x, int y) {
	return x>=0 && y>=0 && x<=2*n && y<=2*n && y-x<=n && y-x>=-n;
}

inline bool IsSet(int x, int y, int t) {
	return matr[x][y] <= t;
}

int currtime;
bitset<SIZE> used[SIZE];
short qarr[SIZE*SIZE][2];
int qs;

bool HasLoop(int t0) {
	for (int i = 0; i<SIZE; i++) used[i].reset();
	currtime = t0;

	qs = 0;
	for (int i = 0; i<all.size(); i++) {
		int x = all[i].first;
		int y = all[i].second;
		if (!IsSet(x,y,t0)) {
			qarr[qs][0] = x;
			qarr[qs][1] = y;
			used[x][y] = true;
			qs++;
		}
	}

	int allcellscnt = 3*n*n + 3*n + 1;

	fprintf(stderr, "[");
	for (int i = 0; i<qs; i++) {
		int x = qarr[i][0];
		int y = qarr[i][1];
		for (int d = 0; d<6; d++) {
			int nx = x;
			int ny = y;
			while (1) {
				nx += dir[d][0];
				ny += dir[d][1];
				if (good(nx, ny) && !IsSet(nx, ny, currtime) && !used[nx][ny]) {
					qarr[qs][0] = nx;
					qarr[qs][1] = ny;
					used[nx][ny] = true;
					qs++;
				}
				else break;
			}
		}
	}

	fprintf(stderr, "|");
	
	for (int i = 0; i<=2*n; i++)
		for (int j = 0; j<=2*n; j++)
			if (good(i,j) && !IsSet(i,j,t0) && !used[i][j])
				return true;
	fprintf(stderr, "]");

	return false;
}

set<pii> vis, added;
void DFS2(int x, int y) {
	vis.insert(pii(x, y));
	added.insert(pii(x, y));
	for (int d = 0; d<6; d++) {
		int nx = x + dir[d][0];
		int ny = y + dir[d][1];
		if (good(nx, ny) && IsSet(nx, ny, currtime) && vis.find(pii(nx, ny)) == vis.end())
			DFS2(nx, ny);
	}
}

bool HasBridge(int t0, bool fork = false) {
	currtime = t0;
	vis.clear();

	for (int c = 0; c<6; c++) {
		const vector<pii> &curr = (fork ? edges[c] : verts[c]);
		for (int i = 0; i<curr.size(); i++) {
			int x = curr[i].first;
			int y = curr[i].second;
			if (IsSet(x,y,t0) && vis.find(pii(x,y)) == vis.end()) {
				added.clear();
				DFS2(x, y);
				set<int> has;
				for (set<pii>::iterator it = added.begin(); it != added.end(); it++) {
					map<pii, int> &tmap = (fork ? edgeind : vertind);
					if (tmap.find(*it) == tmap.end()) continue;
					has.insert(tmap[*it]);
				}
				if (has.size() >= (fork ? 3 : 2)) return true;
			}
		}
	}

	return false;
}

bool HasFork(int t0) { return HasBridge(t0, true); }

bool Solve(int t0) {
	if (HasFork(t0)) return true;
	fprintf(stderr, "1");
	if (HasBridge(t0)) return true;
	fprintf(stderr, "2");
	if (HasLoop(t0)) return true;
	fprintf(stderr, "3");
	return false;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d%d", &n, &m);
		n--;
		for (int i = 0; i<m; i++)
			for (int j = 0; j<2; j++) {
				scanf("%d", &arr[i][j]);
				arr[i][j]--;
			}

		for (int i = 0; i<6; i++) {
			verts[i].clear();
			edges[i].clear();
		}
		all.clear();

		verts[0].push_back(pii(0,0));
		verts[1].push_back(pii(n,0));
		verts[2].push_back(pii(0,n));
		verts[3].push_back(pii(2*n,n));
		verts[4].push_back(pii(n,2*n));
		verts[5].push_back(pii(2*n,2*n));
		for (int i = 1; i<=n-1; i++) {
			edges[0].push_back(pii(i,0));
			edges[1].push_back(pii(0,i));
			edges[2].push_back(pii(n+i,i));
			edges[3].push_back(pii(i,n+i));
			edges[4].push_back(pii(n+i,2*n));
			edges[5].push_back(pii(2*n,n+i));
		}
		for (int i = 0; i<6; i++) {
			all.insert(all.end(), verts[i].begin(), verts[i].end());
			all.insert(all.end(), edges[i].begin(), edges[i].end());
		}

		vertind.clear();
		edgeind.clear();
		for (int i = 0; i<6; i++) {
			for (int j = 0; j<verts[i].size(); j++) vertind[verts[i][j]] = i;
			for (int j = 0; j<edges[i].size(); j++) edgeind[edges[i][j]] = i;
		}


		int uppBound = m;
		memset(matr, 127, sizeof(matr));
		for (int i = 0; i<m; i++) {
			int x = arr[i][0];
			int y = arr[i][1];
			matr[x][y] = i;
			int d;
			for (d = 0; d<6; d++) {
				int nx = x + dir[d][0];
				int ny = y + dir[d][1];
				if (!good(nx, ny)) break;
				if (!IsSet(nx, ny, i)) break;
			}
			if (d == 6) {
				uppBound = i-1;
				break;
			}
		}

		int left = -1;
		int right = uppBound;
		while (right - left > 1) {
			int middle = (left + right) >> 1;
			if (Solve(middle))
				right = middle;
			else
				left = middle;
			fprintf(stderr, "!");
		}

		printf("Case #%d: ", tt);
		if (right == m) printf("none\n");
		else {
			bool ring = HasLoop(right);
			bool bridge = HasBridge(right);
			bool fork = HasFork(right);
			right++;
			if (!fork && ring && bridge) printf("bridge-ring in move %d\n", right);
			if (!fork && !ring && bridge) printf("bridge in move %d\n", right);
			if (!fork && ring && !bridge) printf("ring in move %d\n", right);

			if (fork && ring && bridge) printf("bridge-fork-ring in move %d\n", right);
			if (fork && !ring && bridge) printf("bridge-fork in move %d\n", right);
			if (fork && ring && !bridge) printf("fork-ring in move %d\n", right);
			if (fork && !ring && !bridge) printf("fork in move %d\n", right);
		}

		fflush(stdout);
	}
	return 0;
}
