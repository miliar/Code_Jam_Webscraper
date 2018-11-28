#include <cstdio>
#include <algorithm>
#define MAX_N 2100
#define MAX_P 11
#define INF 1000000000
using namespace std;

int p, tests, m[MAX_N], c[MAX_N], dp[MAX_N][MAX_P];

int licz(int poz, int juz) {
	if (poz >= (1 << p)) {
		if (juz >= p - m[poz - (1 << p)]) return 0;
		else return INF;
	} else {
		if (dp[poz][juz] != -1)
			return dp[poz][juz];
		int ans = min(c[poz] + licz(2 * poz, juz + 1) + licz(2 * poz + 1, juz + 1),
					  licz(2 * poz, juz) + licz(2 * poz + 1, juz));
		if (ans >= INF) ans = INF;
		return (dp[poz][juz] = ans);
	}
}

int main() {
	scanf("%d", &tests);
	for (int tc = 1; tc <= tests; tc++) {
		scanf("%d", &p);
		for (int i = 0; i < (1 << p); i++)
			scanf("%d", &m[i]);
		for (int i = 0; i < p; i++) {
			for (int j = (1 << (p - i - 1)); j < (1 << (p - i)); j++)
				scanf("%d", &c[j]);
		}
		//for (int i = 1; i < (1 << p); i++) printf("%d ", c[i]); printf("\n");
		memset(dp, -1, sizeof(dp));
		printf("Case #%d: %d\n", tc, licz(1, 0));
	}
	return 0;
}