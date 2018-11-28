#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;


int m[110][110];

int main() {
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {

		for (int i = 0; i < 110; ++i) {
			for (int j = 0; j < 110; ++j) {
				m[i][j] = 0;
			}
		}

		bool bact = false;

		int r;
		scanf("%d", &r);

		for (int i = 0; i < r; ++i) {
			int x1, y1, x2, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for (int x = x1; x <= x2; ++x) {
				for (int y = y1; y <= y2; ++y) {
					m[x][y] = 1;
					bact = true;
				}
			}
		}


		int turns = 0;
		while (bact) {
			++turns;
			bact = false;
			for (int x = 100; x >= 1; --x) {
				for (int y = 100; y >= 1; --y) {
					if (!m[x-1][y] && !m[x][y-1]) m[x][y] = 0;
					if (m[x-1][y] && m[x][y-1]) m[x][y] = 1;
					if (m[x][y]) bact = true;
				}
			}
		}

		printf("Case #%d: %d\n", tt, turns);
	}
}
