#include <iostream>
using namespace std;

const int MAXN = 1000;
int bad[MAXN][MAXN], opt[MAXN][MAXN], cx, cy, n;
int dx[] = {1, 2}, dy[] = {2, 1};

void process() {
	memset(opt, 0, sizeof(opt));
	memset(bad, 0, sizeof(bad));
	scanf("%d %d %d", &cx, &cy, &n);
	for (int i = 0; i < n; i++) {
		int x, y;
		scanf("%d %d", &x, &y);
		x--; y--;
		bad[x][y] = 1;
	}

	opt[0][0] = 1;
	for (int x = 0; x < cx; x++)
		for (int y = 0; y < cy; y++)
			if (!bad[x][y])
			for (int i = 0; i < 2; i++) {
				int tx = x + dx[i];
				int ty = y + dy[i];
				if (tx < cx && ty < cy && !bad[tx][ty]) {
					opt[tx][ty] += opt[x][y];
					opt[tx][ty] %= 10007;
				}
			}
	printf("%d\n", opt[cx-1][cy-1]);
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		process();
	}
}
