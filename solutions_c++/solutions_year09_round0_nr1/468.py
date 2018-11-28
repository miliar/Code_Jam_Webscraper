#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <memory.h>

const int MAXD = 6000;
const int MAXL = 20;
const int MAXDICT = 300;
const int MAXLEN = MAXL * MAXDICT + 100;

int L = 0;
int D = 0;
int N = 0;
char dict[MAXD][MAXL] = {{0}};
bool pattern[MAXL][MAXDICT] = {{{0}}};

void read(void) {
	scanf("%d %d %d", &L, &D, &N);
	for (int i = 0; i < D; ++i)
		scanf("%s", dict[i]);
}

void makePattern(const char *const buff) {
	for (int i = 0; i < MAXL; ++i)
		memset(pattern[i], 0, sizeof(pattern[i]));

	int iter = 0;
	for (int i = 0; i < L; ++i) {
		if ('(' != buff[iter]) {
			pattern[i][buff[iter]] = true;
			++iter;
			continue;
		}
		++iter;
		while (')' != buff[iter]) {
			pattern[i][buff[iter]] = true;
			++iter;
		}
		++iter;
	}
}

int match(const int k) {
	for (int i = 0; i < L; ++i) {
		if (!pattern[i][dict[k][i]])
			return 0;
	}
	return 1;
}

int checkPattern() {
	int count = 0;
	for (int i = 0; i < D; ++i)
		count += match(i);
	return count;
}

void solve(void) {
	char buff[MAXLEN] = {0};
	for (int i = 0; i < N; ++i) {
		scanf("%s", buff);
		makePattern(buff);
		printf("Case #%d: %d\n", i + 1, checkPattern());
	}
}

int main(void) {
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
	read();
	solve();
	return 0;
}
