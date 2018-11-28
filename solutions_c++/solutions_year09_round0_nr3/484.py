#include <cstdio>
#include <cstring>

#define MOD 10000

int welcomeToCodeJamLength = 19;
char *welcomeToCodeJam = "welcome to code jam";

int textLength;
char text[505];

int c[25][505];

int main() {
//	freopen("C.in", "r", stdin);

	int prob, nprob; scanf("%d", &nprob);

	gets(text);

	for (prob = 0; prob < nprob;) {
		gets(text);
		textLength = strlen(text);

		memset(c, 0, sizeof(c));
		c[0][0] = 1;
		for (int i = 0; i <= welcomeToCodeJamLength; ++i)
			for (int j = 1; j <= textLength; ++j) {
				c[i][j] = (c[i][j] + c[i][j - 1]) % MOD;
				if (i && welcomeToCodeJam[i - 1] == text[j - 1]) c[i][j] = (c[i][j] + c[i - 1][j - 1]) % MOD;
			}

		printf("Case #%d: %04d\n", ++prob, c[welcomeToCodeJamLength][textLength]);
	}

	return 0;
}

