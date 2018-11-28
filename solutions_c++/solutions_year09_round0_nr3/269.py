#include <stdio.h>
#include <string.h>

const char* s = "welcome to code jam";

int opt[505][20];

int main() {

	//freopen("C.in", "r", stdin);
	//freopen("C.out", "w", stdout);

	int n;
	char str[505];

	scanf("%d", &n);
	gets(str);
	for (int prob = 0; prob < n; prob ++) {
		gets(str);
		int len = strlen(str);

		memset(opt, 0, sizeof(opt));
		opt[0][0] = 1;
		for (int i = 1; i <= len; i ++) {
			opt[i][0] = 1;
			for (int j = 1; j <= 19; j ++) {
				opt[i][j] = opt[i - 1][j];
				if (str[i - 1] == s[j - 1]) opt[i][j] = (opt[i][j] + opt[i - 1][j - 1]) % 10000;
			}
		}

		int ans = opt[len][19];
		printf("Case #%d: %d%d%d%d\n", prob + 1, ans / 1000, ans % 1000 / 100, ans % 100 / 10, ans % 10);
	}

	return 0;
}