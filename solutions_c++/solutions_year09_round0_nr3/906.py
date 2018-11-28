#include <stdio.h>
#include <string.h>
#include <assert.h>

#define KEY		"welcome to code jam"
#define KEYSIZE		19
#define LINESIZE	500
#define MOD		10000

int solve(char *line, int n)
{
	int i, k;
	int cnt[KEYSIZE + 1];
	const char *key = KEY;

	memset(cnt, 0, sizeof(cnt));
	cnt[0] = 1;
	for (i = 0; i < n; i++)
		for (k = KEYSIZE - 1; k >= 0; k--)
			if (line[i] == key[k])
				cnt[k + 1] = (cnt[k + 1] + cnt[k]) % MOD;

	return cnt[KEYSIZE];
}

int main(int argc, char **argv)
{
	int T, X;
	char buf[LINESIZE + 10];
	int n;

	if (argc > 1 && !freopen(argv[1], "rt", stdin)) {
		perror(argv[1]);
		return 1;
	}
	if (argc > 2 && !freopen(argv[2], "wt", stdout)) {
		perror(argv[2]);
		return 1;
	}

	assert(scanf("%d\n", &T) == 1);
	fprintf(stderr, "T=%d\n", T);

	for (X = 1; X <= T; X++) {
		assert(fgets(buf, sizeof(buf), stdin));
		n = strlen(buf);
		while (buf[n - 1] == '\n' || buf[n - 1] == '\r')
			buf[--n] = '\0';
		printf("Case #%d: %04d\n", X, solve(buf, n));
	}

	return 0;
}
