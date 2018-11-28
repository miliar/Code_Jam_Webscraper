#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>
#include <cstring>

using namespace std;

#define ABS(x) ((x) > 0 ? (x) : -(x))

typedef pair<int, int> point;

bool cell[2][500][500];
int t;
int mx, my;

void init() {
	for(int i = 0; i < 500; ++i) {
		for(int j = 0; j < 500; ++j)
			cell[0][i][j] = cell[1][i][j] = false;
	}
	t = mx = my = 0;
}

int get_cell(int x, int y) {
	if (x < 0 || x >= 500 || y < 0 || y >= 500)
		return 0;

	return cell[t][x][y];
}

bool next_status(int x, int y) {
	if (get_cell(x - 1, y) == get_cell(x, y - 1))
		return get_cell(x - 1, y);

	return cell[t][x][y];
}

bool check() {
	bool next = false;
	int t2 = 1 - t;
	for(int x = 0; x <= mx; ++x) {
		for(int y = 0; y <= my; ++y) {
			cell[t2][x][y] = next_status(x, y);
			next |= cell[t2][x][y];
		}
	}

	return next;
}

int solve() {
	int count = 1;
	while(check()) {
		t = 1-t;
		++count;
	}
	return count;
}

int main() {
	freopen("f:/downloads/C-small-attempt2.in", "r", stdin);
	freopen("f:/downloads/output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for(int z = 0; z < T; ++z) {
		init();
		int n;
		scanf("%d", &n);
		for(int i = 0; i < n; ++i) {
			int x1, x2, y1, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for(int x = x1; x <= x2; ++x) {
				for(int y = y1; y <= y2; ++y) {
					cell[0][x][y] = true;
				}
			}
			mx = max(mx, x2);
			my = max(my, y2);
		}

		mx += 10;
		my += 10;
		printf("Case #%d: %d\n", z + 1, solve());
	}
}
