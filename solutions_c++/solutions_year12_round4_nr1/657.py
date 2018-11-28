#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxn = 10001;

char f[maxn][maxn];
int d[maxn];
int l[maxn];
int N;
int D;

bool calcf(int n, int m) {
	if (f[n][m] != -1) return f[n][m];
	char& ans = f[n][m];

	int s = min(l[m], d[m] - d[n]);
	if (d[m] + s >= D) return ans = 1;

	ans = 0;
	for (int i = m+1; i <= N && d[i] <= d[m]+s; i++) {
		ans |= calcf(m, i);
		if (ans) return ans;
	}

	return 0;
}

void init() {
	scanf("%d", &N);
	d[0] = 0;
	for (int i = 1; i <= N; i++)
		scanf("%d%d", &d[i], &l[i]);
	scanf("%d", &D);
}

int main() {
	int T; scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		init();

		printf("Case #%d: ", i+1);

		memset(f, -1, sizeof f);
		if (calcf(0, 1)) printf("YES\n");
		else printf("NO\n");
	}

	return 0;
}
