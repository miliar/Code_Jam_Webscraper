#include <stdio.h>
#include <string.h>
#include <algorithm>

const int MOD = 100003;
typedef long long int64;
const int SIZE = 512;

inline void add(int &a, const int &b) {
	a += b;
	if (a >= MOD) a -= MOD;
}

inline int mult(int a, int b) {
	return (int64(a)*b)%MOD;
}

int n;
int comb[SIZE][SIZE];

int res[SIZE][SIZE];
int ans[SIZE];


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	for (int i = 0; i<SIZE; i++) {
		comb[i][0]= comb[i][i] = 1;
		for (int j = 1; j<=i-1; j++) {
			comb[i][j] = comb[i-1][j-1];
			add(comb[i][j], comb[i-1][j]);
		}
	}

	int n = SIZE-1;
	memset(res, 0, sizeof(res));
	res[1][0] = 1;
	for (int i = 1; i<=n; i++)
		for (int k = 0; k<i; k++) if (res[i][k])
			for (int j = i+i-k; j<=n; j++)
				add(res[j][i], mult(res[i][k], comb[j-i-1][i-k-1]));
	for (int i = 1; i<=n; i++) {
		ans[i] = 0;
		for (int j = 0; j<=i; j++) add(ans[i], res[i][j]);
	}

	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d", &n);
		printf("Case #%d: %d\n", tt, ans[n]);
	}
	return 0;
}
