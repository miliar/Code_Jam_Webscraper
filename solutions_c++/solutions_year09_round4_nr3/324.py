#include <cstdio>
#include <algorithm>

using namespace std;

const int maxn = 100;
const int maxk = 25;

int tab[maxn][maxk];
int seq[maxn][maxn];
bool above[maxn][maxn];
int n, K, ans;

void DFS(int dig, int len) {
	if (len >= ans) return;
	if (dig == n) {
		ans = len;
		return;
	}
	int i, j;
	int *curr = seq[dig];
	for (i = 0; i < len; i++)
		if (above[dig][curr[i]]) {
			for (j = 0; j < len; j++)
				seq[dig + 1][j] = curr[j];
				seq[dig + 1][i] = dig;
			DFS(dig + 1, len);
		}
	for (i = 0; i < len; i++)
		seq[dig + 1][i] = curr[i];
	seq[dig + 1][len] = dig;
	DFS(dig + 1, len + 1);
}

void Solve() {
	scanf("%d %d", &n, &K);
	int i, j, k;
	for (i = 0; i < n; i++)
		for (j = 0; j < K; j++)
			scanf("%d", &tab[i][j]);
	ans = n;
	for (i = 0; i < n; i++)
		for (j = i + 1; j < n; j++) {
			for (k = 0; k < K && tab[i][k] == tab[j][k]; k++);
			if (k < K && tab[i][k] > tab[j][k]) {
				for (k = 0; k < K; k++)
					swap(tab[i][k], tab[j][k]);
			}
		}
	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++) {
			for (k = 0; k < K; k++)
				if (tab[i][k] <= tab[j][k]) break;
			above[i][j] = k == K;
		}
	DFS(0, 0);
	printf("%d\n", ans);
}

int main() {
	int t, i;
	scanf("%d", &t);
	for (i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}