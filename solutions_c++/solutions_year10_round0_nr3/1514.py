#include <cstdio>
#include <string>
using namespace std;

const int MAXN = 2048;

int casenum, n, K, R, g[MAXN], pos[MAXN];
long long profit[MAXN];

int main () {
	
	int i, j, p;
	long long sum, ans, mod;
	
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	scanf("%d", &casenum);
	for (int ca = 1; ca <= casenum; ca++) {
		scanf("%d %d %d", &R, &K, &n);
		sum = 0;
		for (i = 0; i < n; i++) {
			scanf("%d", &g[i]);
			sum += g[i];
		}
//		printf("SUM: %I64d\n", sum);
		
		for ( ;i < n + n; i++) {
			g[i] = g[i-n];
		}
		
		if (K >= sum) {
			ans = R * sum;
			goto out;
		}
		
		for (i = 0; i < n; i++) {
			profit[i] = 0;
			
			mod = K;
			
			for (j = i; j < i + n; j++) {
				if (mod >= g[j]) {
					profit[i] += g[j];
					mod -= g[j];
				} else break;
			}
			pos[i] = (j - 1 + n) % n;
		}
		
//		for (i = 0; i < n; i++)
//			printf("%d -> profit: %I64d, pos: %d\n", i, profit[i], pos[i]);
		ans = 0;
		p = 0;
		while (R--) {
			ans += profit[p];
			p = (pos[p] + 1) % n;
		}
out:
		printf("Case #%d: %I64d\n", ca, ans);
	}
	return 0;
}
