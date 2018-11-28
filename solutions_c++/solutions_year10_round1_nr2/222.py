#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

const int maxn = 200;
const int maxm = 256;
const int inf = (int)1e8;

int a[maxn];
int s[maxn][maxm];

int work() {
	int D, I, M, n;
	scanf("%d %d %d %d", &D, &I, &M, &n);
	for (int i = 1; i <= n; i++)
		scanf("%d", &a[i]);
	for (int j = 0; j < maxm; j++)
		s[0][j] = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 0; j < maxm; j++) {
			int best = inf;
			best <?= s[i-1][j] + D;
			int be = max(j-M, 0), en = min(j+M, maxm-1);
			int d = abs(a[i] - j);
			for (int k = be; k <= en; k++) {
				best <?= s[i-1][k] + d;
			}			
			s[i][j] = best;
		}
		if (M > 0) {
			for (int j = 0; j < maxm; j++) {
				for (int k = 0; k < maxm; k++) {				
					int d = (abs(k-j) + M-1) / M;
					s[i][k] <?= s[i][j] + d * I;
				}
			}
		}
	}
	int best = inf;
	for (int i = 0; i < maxm; i++) {
		best <?= s[n][i];
	}
	return best;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {		
		printf("Case #%d: %d\n", t, work());		
	}
}