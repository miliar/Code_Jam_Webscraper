#include <stdio.h>
#include <string.h>

const int MAXN = 1010;

int k = 0;
char s[MAXN];
int perm[MAXN] = {0};
bool was[MAXN] = {0};
int best = 0;

int count() {
	char sp[MAXN] = {0};
	int l = strlen(s) / k;
	for (int i = 0; i < l; ++i) {
		for (int j = 0; j < k; ++j) {
			sp[i * k + j] = s[i * k + perm[j]];
		}
	}
	int inv = 1;
	for (int i = 1; i < k * l; ++i) {
		if (sp[i] != sp[i - 1]) {inv++;}
	}
	return inv;
}

void check() {
	int c = count();
	if (best > c) {best = c;}
}

void find(int p) {
	if (k == p) {
		check();
		return;
	}
	for (int i = 0; i < k; ++i) {
		if (!was[i]) {
			was[i] = true;
			perm[p] = i;
			find(p + 1);
			was[i] = false;
		}
	}
}

void solve(void) {
	scanf("%d\n", &k);
	gets(s);
	for (int i = 0; i < MAXN; ++i) {was[i] = false;}
	best = 1000000;
	find(0);
	printf("%d\n", best);
}

int main(void) {
	freopen("d.in", "rt", stdin);
	freopen("d.out", "wt", stdout);

	int T = 0;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}
