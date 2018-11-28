#include <cstdio>
#include <cstring>

const int cmod = 10000;
const int maxl = 1000;
const int L = 19;
const char *dest = "welcome to code jam";

char str[maxl];
int opt[maxl][L + 1];

int main() {
	int t, i, j, k, len;
	scanf("%d", &t);
	gets(str);
	for (i = 0; i < t; i++) {
		len = strlen(gets(str));
		for (j = 0; j <= len; j++)
			for (k = 0; k <= L; k++)
				opt[j][k] = 0;
		opt[0][0] = 1;
		for (j = 0; j < len; j++)
			for (k = 0; k <= L; k++)
				if (opt[j][k]) {
					(opt[j + 1][k] += opt[j][k]) %= cmod;
					if (k < L && str[j] == dest[k])
						(opt[j + 1][k + 1] += opt[j][k]) %= cmod;
				}
		printf("Case #%d: %04d\n", i + 1, opt[len][L]);
	}
	//printf("%d\n", opt[20][18]);
	return 0;
}
