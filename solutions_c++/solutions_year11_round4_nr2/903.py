#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn = 510;
int r, c, d, w[maxn][maxn];

int main() {
	int tc;
	cin >> tc;
	for (int tt = 1; tt <= tc; tt++) {
		cin >> r >> c >> d;
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++) {
				char c;
				cin >> c;
				w[i][j] = d + c - '0';
			}
		
		int ans;
		bool solved = false;
		for (ans = r > c ? c : r; ans >= 3; ans--) {
			for (int i = 0; i < r + 1 - ans; i++) {
				for (int j = 0; j < c + 1 - ans; j++) {
					int x = i, y = j, lx = i + ans - 1, ly = j + ans - 1;
					
					int tx = 0, ty = 0, ww = 0;					
					for (int k = x; k <= lx; k++) {
						for (int l = y; l <= ly; l++) {
							if (k == x && l == y)
								continue;
							if (k == x && l == ly)
								continue;
							if (k == lx && l == y)
								continue;
							if (k == lx && l == ly)
								continue;
								
							ww += (w[k][l]);
							tx += (k - x) * (w[k][l]);
							ty += (l - y) * (w[k][l]);
						}
					}
					if (((ans - 1) * ww) % 2 == 0 && tx == (ans - 1) * ww / 2)
						if (tx == ty)
						{
							solved = true;
							break;
						}
				}
				if (solved)
					break;
			}
			if (solved)
				break;
		}
		if (ans < 3)
			printf("Case #%d: IMPOSSIBLE\n", tt);
		else
			printf("Case #%d: %d\n", tt, ans);
	}
}
