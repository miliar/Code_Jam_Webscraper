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

const int MAXN = 51;
const int INF = 0x7fffffff;

int n;
int value[MAXN * 2 + 10][MAXN * 2 + 10];
bool tags[MAXN * 2 + 10][MAXN * 2 + 10];

inline bool check(int ci, int cj) {
	for (int i = 1; i < n + n; i++) {
		for (int j = 1; j < n + n; j++) {
			if (tags[i][j]) {
				int nj = cj - j + cj;
				if (1 <= nj && nj < n + n && tags[i][nj] && value[i][nj] != value[i][j]) {
					return false;
				}
				int ni = ci - i + ci;
				if (1 <= ni && ni < n + n && tags[ni][j] && value[ni][j] != value[i][j]) {
					return false;
				}
				if (1 <= ni && ni < n + n && 1 <= nj && nj < n + n && tags[ni][nj] && value[ni][nj] != value[i][j]) {
					return false;
				}
			}
		}
	}
	return true;
}

int main() {
	int caseNum;
	scanf("%d", &caseNum);
	for (int caseIndex = 1; caseIndex <= caseNum; caseIndex++) {
		memset(tags, false, sizeof(tags));
		scanf("%d", &n);
		for (int i = 1; i <= n; i++) {
			int p = n - i + 1;
			for (int j = 1; j <= i; j++) {
				scanf("%d", &value[i][p]);
				tags[i][p] = true;
				p += 2;
			}
		}
		for (int i = n + 1; i < n + n; i++) {
			int p = i - n + 1;
			for (int j = 1; j <= n + n - i; j++) {
				scanf("%d", &value[i][p]);
				tags[i][p] = true;
				p += 2;
			}
		}
		int minSize = 10 * n;
		for (int ci = -2 * n; ci < 4 * n; ci++) {
			for (int cj = -2 * n; cj < 4 * n; cj++) {
				if (check(ci, cj)) {
					minSize = min(minSize, abs(ci - n) + abs(cj - n) + n);
				}
			}
		}
		printf("Case #%d: %d\n", caseIndex, minSize * minSize - n * n);
	}
	return 0;
}
