#include <cstdlib>
#include <cstdio>
#include <memory.h>

int pas[501][501];
long long mem[501][501];

int main()
{
	int T;
	scanf("%d", &T);

	for (int i = 0; i <= 500; i++) {
		for (int j = 0; j <= 500; j++) {
			if (j == 0) pas[i][j] = 1;
			else pas[i][j] = (pas[i-1][j-1] + pas[i-1][j]) % 100003;
		}
	}

	for (int t = 1; t <= T; t++) {
		int n;
		scanf("%d", &n);
		memset(mem, 0x00, sizeof(mem));
		
		for (int i = 2; i <= n; i++) {
			mem[i][1] = 1;
			for (int j = 2; j < i; j++) {
				for (int k = 1; k < j; k++) {
					if (i - j < j - k) continue;
					mem[i][j] = (mem[i][j] + mem[j][k] * pas[i-j-1][j-k-1]) % 100003;
				}
			}
		}
		int res = 0;
		for (int i = 1; i < n; i++) res = (res + mem[n][i]) % 100003;
		printf("Case #%d: %d\n", t, res);
	}		
	return 0;
}
