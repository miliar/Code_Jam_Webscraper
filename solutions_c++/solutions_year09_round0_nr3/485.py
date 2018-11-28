#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <memory.h>
#include <string.h>

const int MAXN = 600;
const char * const pattern = "welcome to code jam";
const int MAXL = 19;
const int BASE = 10000;

int N = 0;
char str[MAXN] = {0};
int cnt[MAXN][MAXL] = {{0}};

void read(void) {
	scanf("%d", &N);
}

void init(void) {
	for (int i = 0; i < MAXN; ++i)
		memset(cnt[i], 0, sizeof(cnt[i]));
}

int solveI(void) {
	int N = strlen(str);
	for (int i = 0; i < N; ++i)
		if (pattern[0] == str[i])
			cnt[i][0] = 1;
	for (int i = 0; i < N; ++i)
		for (int j = 1; j < MAXL; ++j)
			if (pattern[j] == str[i])
				for (int k = 0; k < i; ++k)
						cnt[i][j] = (cnt[i][j] + cnt[k][j - 1]) % BASE;

	int sum = 0;
	for (int i = 0; i < N; ++i)
		if (pattern[MAXL - 1] == str[i])
			sum = (sum + cnt[i][MAXL - 1]) % BASE;
	return sum; 
}

void printAns(const int k, const int ans) {
	printf("Case #%d: ", k);
	int cur = 10;
	while (cur < BASE) {
		if (ans < cur)
			printf("0");
		cur *= 10;
	}
	printf("%d\n", ans);
}

void solve(void) {
	gets(str);
	for (int i = 0; i < N; ++i) {
		init();
		gets(str);
		printAns(i + 1, solveI());
	}
}

int main(void) {
	freopen("c.in", "rt", stdin);
	freopen("c.out", "wt", stdout);
	read();
	solve();
	return 0;
}
