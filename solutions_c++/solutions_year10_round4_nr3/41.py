#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

const int MAXN = 100;

bool grid[2][MAXN][MAXN];

int main() {
	int caseNum;
	scanf("%d", &caseNum);
	for (int caseIndex = 1; caseIndex <= caseNum; caseIndex++) {
		memset(grid[0], false, sizeof(bool) * MAXN * MAXN);
		int r;
		for (scanf("%d", &r); r-- > 0;) {
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			x1--;
			y1--;
			x2--;
			y2--;
			for (int i = x1; i <= x2; i++) {
				for (int j = y1; j <= y2; j++) {
					grid[0][i][j] = true;
				}
			}
		}
		int cur = 0;
		int ans = 0;
		while (true) {
			bool hasAlive = false;
			int next = !cur;
			for (int i = 0; i < MAXN; i++) {
				for (int j = 0; j < MAXN; j++) {
					if (grid[cur][i][j]) {
						if ((i > 0 && grid[cur][i - 1][j]) || (j > 0 && grid[cur][i][j - 1])) {
							hasAlive = grid[next][i][j] = true;
						} else {
							grid[next][i][j] = false;
						}
					} else {
						if ((i > 0 && grid[cur][i - 1][j]) && (j > 0 && grid[cur][i][j - 1])) {
							hasAlive = grid[next][i][j] = true;
						} else {
							grid[next][i][j] = false;
						}
					}
				}
			}
			ans++;
			if (!hasAlive) {
				break;
			}
			cur = next;
		}
		printf("Case #%d: %d\n", caseIndex, ans);
	}
	return 0;
}
