#include <stdio.h>
#include <string.h>

char w[] = "welcome to code jam", s[1000];
int cnt[20][505], len,i,j;

int main() {
	int test, ntest;
	scanf("%d", &ntest); getchar();
	for (test = 1; test <= ntest; test++) {
		printf("Case #%d: ", test);
		fgets(s, 1000, stdin);
		len = strlen(s);
		for (i = 0; i <= len; i++) for (j = 0; j <= 19; j++) cnt[j][i] = 0;
		for (i = 0; i <= len; i++) cnt[0][i] = 1;

		for (i = 1; i <= 19; i++) {
			for (j = 1; j <= len; j++) {
				cnt[i][j] = cnt[i][j-1];
				if (s[j-1] == w[i-1]) {
					cnt[i][j] = (cnt[i-1][j-1] + cnt[i][j]) % 10000;
				}
			}
		}
		printf("%04d\n", cnt[19][len]);
	}
	return 0;
}
