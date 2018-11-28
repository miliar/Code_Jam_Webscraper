#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int p;
int need[1025];
int cost[1025][1025];
int f[1025][1025][11];

int main (int argc, char * const argv[])
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int tt = 1; tt <= test; tt++) {
		memset(f, 0xff, sizeof(f));
		scanf("%d", &p);
		for (int i = 0; i < 1 << p; i++) {
			scanf("%d", &need[i]);
		}
		for (int i = 0; i < p; i++) {
			for (int j = 0; j < 1 << (p - i - 1); j++) {
				scanf("%d", &cost[i][j]);
				for (int k = 0; k <= p - i - 1; k++) {
					if (i == 0) {
						if (k < need[j * 2] && k < need[j * 2 + 1]) {
							f[i][j][k] = 0;
						} else {
							if (k == min(need[j * 2], need[j * 2 + 1]))
								f[i][j][k] = cost[i][j];
						}
					} else {
						if (f[i - 1][j * 2][k] >= 0 && f[i - 1][j * 2 + 1][k] >= 0) f[i][j][k] = f[i - 1][j * 2][k] + f[i - 1][j * 2 + 1][k] + cost[i][j];
						if (f[i - 1][j * 2][k + 1] >= 0 && f[i - 1][j * 2 + 1][k + 1] >= 0) {
							if (f[i][j][k] < 0) {
								f[i][j][k] = f[i - 1][j * 2][k + 1] + f[i - 1][j * 2 + 1][k + 1];
							} else {
								if (f[i - 1][j * 2][k + 1] + f[i - 1][j * 2 + 1][k + 1] < f[i][j][k]) {
									f[i][j][k] = f[i - 1][j * 2][k + 1] + f[i - 1][j * 2 + 1][k + 1];
								}
							}

						}
					}

				}
			}
		}
		int ans = 2147483647;
		for (int i = 0; i <= p; i++) {
			if (f[p - 1][0][i] >= 0 && f[p - 1][0][i] < ans) ans = f[p - 1][0][i];
		}
		printf("Case #%d: %d\n", tt, ans);
	}
}
