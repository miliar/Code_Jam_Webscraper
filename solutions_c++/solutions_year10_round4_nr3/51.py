// c-small

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int m[256][256];
const int n = 256;

int solve() {
	int r;
	scanf("%d", &r);
	memset(m, 0, sizeof(m));
	while (r --) {
		int x1, x2, y1, y2;
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		if (x1 > x2) swap(x1, x2);
		if (y1 > y2) swap(y1, y2);
		for (int x = x1; x <= x2; ++x) {
			for (int y = y1; y <= y2; ++y)
				m[x][y] = 1;
		}
	}
	for (int turn = 1; ; ++turn) {
		bool flag = false;
		for (int i = n - 1; i >= 1; --i) {
			for (int j = n - 1; j >= 1; --j) {
				if (m[i-1][j] == turn && m[i][j-1] == turn) {
					m[i][j] = turn + 1;
					flag = true;
				} else if ((m[i-1][j] == turn || m[i][j-1] == turn) && (m[i][j] == turn)) {
					m[i][j] = turn + 1;
					flag = true;
				}
			}
		}
		/*for (int i = 1; i <= 10; ++i) {
			for (int j = 1; j <= 10; ++j)
				if (m[i][j] == turn+1) printf("1"); else printf("0");
			putchar('\n');
		}
		putchar('\n');*/

		if (!flag) return turn;
	}
}

int main() {
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int T, tc = 0;
	scanf("%d", &T);
	while (T--) {
		printf("Case #%d: %d\n", ++tc, solve());
	}
}
