#include<stdio.h>
#include<string.h>

const int maxd = 5000;
const int maxl = 16;
const int maxn = 500;

int L, D, N;
char dict[maxd][maxl];
char str[maxl * 30];
char has[maxl][27];

void init(char *s) {
	memset(has, 0, sizeof(has));
	int pos = 0;
	for (; *s; ++s) {
		if (*s == '(') {
			++s;
			while (*s != ')') {
				has[pos][*s - 'a'] = 1;
				++s;
			}
			++pos;
		} else {
			has[pos][*s - 'a'] = 1;
			++pos;
		}
	}
}

int ok(char *w) {
	for (int i = 0; i < L; i++, ++w) {
		if (!has[i][*w - 'a']) {
			return 0;
		}
	}
	return 1;
}

int main() {
	scanf("%d%d%d", &L, &D, &N);
	for (int i = 0; i < D; i++) {
		scanf("%s", dict[i]);
	}
	for (int i = 1; i <= N; i++) {
		scanf("%s", str);
		init(str);
		int cnt = 0;
		for (int j = 0; j < D; j++) {
			if (ok(dict[j])) {
				cnt++;
			}
		}
		printf("Case #%d: %d\n", i, cnt);
	}
	return 0;
}

