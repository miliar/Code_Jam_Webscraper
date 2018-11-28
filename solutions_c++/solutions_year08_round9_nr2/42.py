#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>

const int Max = 100;

int map[Max][Max], n, m;
int dx1, dy1, dx2, dy2, x, y;

void input() {
	scanf("%d%d", &n, &m);
	scanf("%d%d", &dx1, &dy1);
	scanf("%d%d", &dx2, &dy2);
	scanf("%d%d", &x, &y);
}

void fill(int x, int y) {
	if(x < 0||x >= n||y < 0|| y >= m) return ;
	if(map[x][y] == 1) return ;
	map[x][y] = 1;

	fill(x + dx1, y + dy1);
	fill(x + dx2, y + dy2);
}

void solve() {
	memset(map, 0, sizeof(map));

	fill(x, y);

	int res = 0;
	for(int i = 0;i < n;i ++) for(int j = 0;j < m;j ++) if(map[i][j] == 1) ++ res;
	printf("%d\n", res);
}

int main() {
	freopen("./input", "r", stdin);
	freopen("./output.txt", "w", stdout);

	int Cas;
	scanf("%d", &Cas);
	for(int i = 1;i <= Cas;i ++) {
		input();
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
