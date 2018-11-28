#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>

int dp[5][32][10][10][10][10][10], n, m;
int grid[5][5], res;

void input() {
	scanf("%d%d", &n, &m);
	for(int i = 0;i < n;i ++) for(int j = 0;j < m;j ++) scanf("%d", &grid[i][j]);
}

int count(int p,int s) {
	int ret = 0;
	if(s&(1<<p)) ++ ret;
	if(p > 0&&(s&(1<<(p-1)))) ++ ret;
	if(p < n-1&&(s&(1<<(p+1)))) ++ ret;

	return ret;
}

int pnum[5];

void DFS(int j,int s,int id) {
	if(id == n) {
		int num[5];
		for(int i = 0;i < 5;i ++) num[i] = pnum[i];
		int tpre = dp[j][s][num[0]][num[1]][num[2]][num[3]][num[4]];
		if(tpre == -1) return ;
		for(int s1 = 0;s1 < (1<<n);s1 ++) {
			int tnum[5], i;
			memset(tnum, 0, sizeof(tnum));

			for(i = 0;i < n;i ++) tnum[i] = count(i, s1);

			for(i = 0;i < n;i ++) if(num[i] + tnum[i] != grid[i][j]) break;
			if(i < n) continue;

			for(i = 0;i < n;i ++) {
				tnum[i] += count(i, s);
				if(tnum[i] > grid[i][j+1]) break;
			}
			if(i < n) continue;

			int &tnow = dp[j+1][s1][tnum[0]][tnum[1]][tnum[2]][tnum[3]][tnum[4]];

			int tmp = tpre + ((s1&(1<<(n/2))) > 0? 1:0);
			if(tmp > tnow) tnow = tmp;

			if(j+1 == m-1&&tnow > res) res = tnow;
		}
		return ;
	}
	for(int i = 0;i < 10;i ++) {
		pnum[id] = i;
		DFS(j, s, id+1);
	}
}

void solve() {
	memset(dp, -1, sizeof(dp));
	for(int s = 0;s < (1<<n);s ++) {
		int num[5], i;
		memset(num, 0, sizeof(num));
		for(i = 0;i < n;i ++) {
			num[i] = count(i, s);
			if(num[i] > grid[i][0]) break;
		}
		if(i < n) continue;

		dp[0][s][num[0]][num[1]][num[2]][num[3]][num[4]] = ((s&(1<<(n/2))) > 0? 1:0);
	}

	res = 0;

	for(int j = 0;j < m-1;j ++) {
		for(int s = 0;s < (1<<n);s ++) {
			memset(pnum, 0, sizeof(pnum));
			DFS(j, s, 0);
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
