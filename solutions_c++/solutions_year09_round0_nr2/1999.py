#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <sstream>
#include <cassert>


inline void openFiles() {
#ifndef ONLINE_JUDGE
	freopen("test.in", "rt", stdin);
	freopen("test.out", "wt", stdout);
#endif
}

void solve();

int main() {
	openFiles();
	int t; scanf("%d\n", &t);
	for (int i = 0; i < t; ++i)
		solve();
	return 0;
}

std::vector<std::vector<char> > map, res;
int n, m, currLbl;

int rec(int x, int y) {
	if (res[x][y] == 0) {
		const int dx[] = {-1,0,0,1};
		const int dy[] = {0,-1,1,0};
		int minval = 1000000;
		for (int i = 0; i < 4; ++i) {
			int xx = x + dx[i];
			int yy = y + dy[i];
			if (xx < 0 || xx >= n || yy < 0 || yy >= m)
				continue;
			if (map[xx][yy] < map[x][y]) {
				minval = std::min(minval, (int)map[xx][yy]);
			}
		}
		for (int i = 0; i < 4; ++i) {
			int xx = x + dx[i];
			int yy = y + dy[i];
			if (xx < 0 || xx >= n || yy < 0 || yy >= m)
				continue;
			if (map[xx][yy] == minval) {
				return res[x][y] = rec(xx, yy);
			}
		}
		res[x][y] = ++currLbl;
	}
	return res[x][y];
}

void solve() {
	currLbl = 0;
	scanf("%d %d", &n, &m);
	map.assign(n, std::vector<char>(m));
	res.assign(n, std::vector<char>(m));
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j) {
			int t; scanf("%d", &t);
			map[i][j] = t;
		}
	static int ntest = 0;
	printf("Case #%d:\n", ++ntest);
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (j) printf(" ");
			printf("%c", rec(i,j) + 'a' - 1);
		}
		printf("\n");
	}
}
