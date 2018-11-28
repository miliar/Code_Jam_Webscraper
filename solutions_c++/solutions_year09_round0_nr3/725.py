#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_L 510
#define MOD 10000

char word[] = "welcome to code jam";
char str[MAX_L];
int length;
int m;
int f[MAX_L][MAX_L];

int main(int argc, char* argv[]) {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int N;
	scanf("%d", &N);
	getchar();

	for (int k = 1; k <= N; ++k) {
		fgets(str, MAX_L, stdin);
		length = strlen(str);
		str[--length] = '\0';

		m = strlen(word);
		memset(f, 0, sizeof(f));
		for (int i = 0; i < length; ++i) {
			for (int j = 0; j < m; ++j) {
				if (i < j)
					f[i][j] = 0;
				else {
					if (str[i] == word[j]) {
						f[i][j] = 0;
						// i-1, j-1
						if (j == 0)
							f[i][j] += 1;
						else if (i != 0)
							f[i][j] += f[i-1][j-1];
						// i-1, j
						if (i != 0)
							f[i][j] += f[i-1][j];
					} else {
						if (i != 0)
							f[i][j] = f[i-1][j];
					}
				}
				f[i][j] = f[i][j] % MOD;
			}
		}

		int res = f[length - 1][m - 1];
		printf("Case #%d: %d%d%d%d\n", k, res / 1000, res % 1000 / 100, res % 100 / 10, res % 10);
		
	}

	return 0;
}
