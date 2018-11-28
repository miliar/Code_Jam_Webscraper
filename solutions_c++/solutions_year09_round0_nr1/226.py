#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

bool vst[16][26];
int L, D, N;
char words[5009][17];
char s[10009];

void calc(char *s) {
	int n = strlen(s);
	int i, j, k;
	static stack[10009];

	memset(vst, 0, sizeof(vst));
	for (i = j = 0; i < n; ++i) {
		if (s[i] >= 'a' && s[i] <= 'z') {
			vst[j++][s[i] - 'a'] = true;
		} else if (s[i] == '(') {
			for (k = i + 1; s[k] != ')'; ++k) {
				vst[j][s[k] - 'a'] = true;
			}
			++j;
			i = k;
		}
	}
}


int main() {
	int i, j, k;
	int ans;
	freopen("F:\\A-large.in", "r", stdin);
	freopen("F:\\A-large.out", "w", stdout);

	scanf("%d%d%d", &L, &D, &N);
	for (i = 0; i < D; ++i)
		scanf("%s", words[i]);
	for (i = 0; i < N; ++i) {
		scanf("%s", s);
		calc(s);
		ans = 0;
		for (j = 0; j < D; ++j) {
			for (k = 0; k < L; ++k)
				if (!vst[k][words[j][k] - 'a'])
					break;
			if (k >= L) ++ans;
		}
		printf("Case #%d: %d\n", i + 1, ans);
	}
	return 0;
}
