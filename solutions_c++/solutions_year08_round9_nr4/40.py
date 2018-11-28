#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <algorithm>

using namespace std;

const int Max = 32;
const int dir[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};

char map[Max][Max];
int n, m;
int dp1[Max][Max], pre1[Max][Max][2], dp2[Max][Max], pre2[Max][Max][2];
int path[Max][Max];

void input() {
	scanf("%d%d", &n, &m);
	for(int i = 1;i <= n;i ++) scanf("%s", map[i]+1);
	for(int i = 0;i <= n+1;i ++) map[i][0] = map[i][m+1] = '.';
	for(int j = 0;j <= m+1;j ++) map[0][j] = map[n+1][j] = '.';
}

void BFS(int sx, int sy, int dp[][Max], int pre[][Max][2]) {
	queue<pair<int, int> > Q;
	Q.push(make_pair(sx, sy));

	while(!Q.empty()) {
		sx = Q.front().first; sy = Q.front().second;
		Q.pop();
		for(int i = 0;i < 4;i ++) {
			int tx = sx + dir[i][0], ty = sy + dir[i][1];
			if(map[tx][ty] == '.') continue;

			if(dp[tx][ty] != -1) continue;
			dp[tx][ty] = dp[sx][sy] + 1;
			pre[tx][ty][0] = sx;
			pre[tx][ty][1] = sy;
			Q.push(make_pair(tx, ty));
		}
	}
}

void solve() {
	memset(dp1, -1, sizeof(dp1));
	dp1[1][1] = 0;
	BFS(1, 1, dp1, pre1);

	int sx = -1, sy;
	for(int i = 1;i <= n;i ++) for(int j = 1;j <= m;j ++) if(i+j > 2&&map[i][j] == 'T') {
		sx = i;
		sy = j;
	}



	int res = 0;


	if(sx == -1) {
		for(int i = 1;i <= n;i ++) for(int j = 1;j <= m;j ++) if(map[i][j] != '.') res += dp1[i][j];
	}
	else {
		memset(dp2, -1, sizeof(dp2));
		dp2[sx][sy] = 0;
		BFS(sx, sy, dp2, pre2);

		memset(path, 0, sizeof(path));
		while(!(sx+sy == 2)) {
			path[sx][sy] = 1;
			int tx = sx;
			sx = pre1[tx][sy][0];
			sy = pre1[tx][sy][1];
		}

		for(int i = 1;i <= n;i ++) for(int j = 1;j <= m;j ++) {
			if(map[i][j] == '.') continue;
			if(path[i][j]) {
				res += dp1[i][j];
			}
			else {
				if(dp1[i][j] < dp2[i][j]) res += dp1[i][j];
				else res += dp2[i][j];
			}
		}
	}

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
