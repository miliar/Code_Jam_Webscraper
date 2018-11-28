#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

const int MAXN = 10010;
char str[MAXN], str2[MAXN];
bool used[MAXN];
int a[MAXN];
int m, n;
int best;

int compute_sol() {
	//for (int i = 0; i < m; i++)
	//	printf("%d ", a[i]);
	//printf("\n");
	for (int k = 0; k < n/m; k++)
		for (int i = 0; i < m; i++) {
			// printf("k*m+i=%d\n", k*m+i);
			str2[k*m+i] = str[k*m+a[i]];
		}
	//printf("%s\n", str2);
	int cnt = 1;
	for (int i = 1; i < n; i++)
		if (str2[i] != str2[i-1])
			cnt++;
	//printf("cnt=%d\n", cnt);
	return cnt;
}

void dfs(int dep) {
	if (dep >= m) {
		int tmp = compute_sol();
		if (tmp < best)
			best = tmp;
		return;
	}

	for (int i = 0; i < m; i++)
		if (!used[i]) {
			used[i] = true;
			a[dep] = i;
			dfs(dep+1);
			used[i] = false;
		}
}

void process() {
	scanf("%d", &m);
	scanf("%s", str);
	n = strlen(str);

	memset(used, 0, sizeof(used));
	best = n;
	dfs(0);
	printf("%d\n", best);
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		process();
	}
}

