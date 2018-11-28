#include<stdio.h>
#include<algorithm>
const int maxlen = 1007;
const int maxn = 7;
const int inf = 30000;
int n;
char str[maxlen];
char s[maxlen];
int perm[maxn];
char tmp[maxlen];
void re_order(char *p) {
	for (int i = 0; i < n; i++) {
		tmp[i] = p[perm[i]];
	}
	for (int i = 0; i < n; i++) {
		p[i] = tmp[i];
	}
}
int solve() {
	strcpy(s, str);
	for (int i = 0; s[i]; i += n) {
		re_order(s + i);
	}
	int ret = 1;
	for (int i = 1; s[i]; i++) {
		ret += (s[i] != s[i - 1]);
	}
	return ret;
}
int main() {
	int T;
	scanf("%d", &T);
	for (int casen = 1; casen <= T; casen++) {
		scanf("%d%s", &n, str);
		for (int i = 0; i < n; i++) {
			perm[i] = i;
		}
		int ans = inf;
		do {
			ans = std::min(ans, solve());
		} while (std::next_permutation(perm, perm + n));
		printf("Case #%d: %d\n", casen, ans);
	}
	return 0;
}

