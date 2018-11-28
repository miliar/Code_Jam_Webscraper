#include <cstdio>
#include <cstring>
#include <cassert>
#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }

typedef long long int64;

#define inf 0x3f3f3f3f

#define maxs (1 << 7)
#define P 10007

int cnt[maxs][maxs];

int dx[2] = {1, 2};
int dy[2] = {2, 1};

int main() {
	int t, tc;
	scanf("%d", &tc);
	for(t = 1; t <= tc; t++) {
		int w, h, r, i, j, k, x, y;
		scanf("%d%d%d", &h, &w, &r);
		memset(cnt, 0, sizeof(cnt));
		for(i = 0; i < r; i++) {
			scanf("%d%d", &y, &x); x--; y--;
			cnt[y][x] = -1;
		}
		cnt[h-1][w-1] = 1;
		for(i = h-1; i >= 0; i--)
			for(j = w-1; j >= 0; j--)
				if(cnt[i][j] == -1) cnt[i][j] = 0;
				else {
					for(k = 0; k < 2; k++) {
						int ni = i + dy[k], nj = j + dx[k];
						if(ni >= h || nj >= w) continue;
						cnt[i][j] += cnt[ni][nj];
					}
					cnt[i][j] %= P;
				}
		printf("Case #%d: %d\n", t, cnt[0][0]);
	}
	return 0;
}
