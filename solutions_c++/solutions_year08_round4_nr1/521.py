#include <algorithm>
#include <cstdio>
using namespace std;

const int MaxN = 10000 + 100;

int totCase, caseNum;
int n, m, res;
int c[MaxN], g[MaxN], value[MaxN];
int f[MaxN][2], v[MaxN][2];

void init();
void work();

int main() {
	init();
	scanf("%d", &totCase);
	for (caseNum = 1; caseNum <= totCase; ++caseNum) {
		scanf("%d %d", &n, &res);
		m = (n - 1) / 2;
		for (int i = 0; i < m; ++i)
			scanf("%d %d", &g[i], &c[i]);
		for (int i = m; i < n; ++i)
			scanf("%d", &value[i]);
		printf("Case #%d: ", caseNum);
		work();
	}
	return 0;
}

void init() {
	for (int i = 0; i < MaxN; ++i)
		v[i][0] = v[i][1] = -1;
}

void work() {
	for (int i = m; i < n; ++i) {
		if (value[i] == 0) {
			v[i][0] = caseNum;
			f[i][0] = 0;
		} else {
			v[i][1] = caseNum;
			f[i][1] = 0;
		}
	}
	for (int i = m - 1; i >= 0; --i) {
		int left = i * 2 + 1, right = i * 2 + 2;
		// Original
		for (int j = 0; j < 2; ++j)
			for (int k = 0; k < 2; ++k)
				if (v[left][j] == caseNum && v[right][k] == caseNum) {
					int res = (j & k);
					if (g[i] == 0)
						res = (j | k);
					if (v[i][res] != caseNum) {
						v[i][res] = caseNum;
						f[i][res] = f[left][j] + f[right][k];
					} else if (f[i][res] > f[left][j] + f[right][k]) {
						f[i][res] = f[left][j] + f[right][k];
					}
				}
		// Change
		if (c[i] == 1) {
			for (int j = 0; j < 2; ++j)
				for (int k = 0; k < 2; ++k)
					if (v[left][j] == caseNum && v[right][k] == caseNum) {
						int res = (j | k);
						if (g[i] == 0)
							res = (j & k);
						if (v[i][res] != caseNum) {
							v[i][res] = caseNum;
							f[i][res] = f[left][j] + f[right][k] + 1;
						} else if (f[i][res] > f[left][j] + f[right][k] + 1) {
							f[i][res] = f[left][j] + f[right][k] + 1;
						}
					}
		}
	}
	if (v[0][res] != caseNum)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", f[0][res]);
}
