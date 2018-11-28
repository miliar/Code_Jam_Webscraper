#include <stdio.h>
#include <string>
using namespace std;
int mil[15][2][4], n, l, whe[15], bes[15], ans, mal, ful;
inline bool all(int las[]) {
	for (int i = 0; i < l - 1; ++i)
		if (las[i] != (1 << 30) - 1)
			return false;
	if (las[l - 1] != ful)
		return false;
	return true;
}
void work(int dep, int las[]) {
	if  (dep < n) {
		int sat[4], j;
		for (int i = 0; i < 2; ++i) {
			for (j = 0; j < l; ++j)
				sat[j] = las[j] | mil[dep][i][j];
			mal += i; whe[dep] = i;
			work(dep + 1, sat);
			mal -= i;
		}
	}
	else if (mal < ans && all(las)) {
		ans = mal;
		memcpy(bes, whe, n << 2);
	}
}
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cas, tex, i, j, k, m, ini[4];
	for (scanf("%d", &cas), tex = 1; tex <= cas; ++tex) {
		scanf("%d%d", &n, &m);
		memset(mil, 0, sizeof(mil));
		for (i = 0; i < m; ++i) 
			for (scanf("%d", &j); j > 0; --j) {
				scanf("%d%d", &k, &l);
				--k;
				mil[k][l][i / 30] |= 1 << i % 30;
			}
		l = (m - 1) / 30 + 1; mal = 0; ans = n + 1;
		if (m % 30 == 0)
			ful = (1 << 30) - 1;
		else
			ful = (1 << m % 30) - 1;
		for (i = 0; i < l; ++i)
			ini[i] = 0;
		work(0, ini);
		printf("Case #%d:", tex);
		if (ans > n) 
			printf(" IMPOSSIBLE");
		else for (i = 0; i < n; ++i)
				printf(" %d", bes[i]);
		printf("\n");
	}
	return 0;
}