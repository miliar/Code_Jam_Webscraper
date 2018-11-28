#include <cstdio>
#include <memory>

const int maxn = 5000;
const int maxlen = 15;

int L, D, N, ans;
bool pattern[maxlen][26];
char words[maxn][maxlen + 1];

inline void init() {
	scanf("%d%d%d", &L, &D, &N);
	for (int i = 0; i < D; ++i) scanf(" %s", words[i]);
}

inline void getPattern() {
	char ch;
	memset(pattern, false, sizeof pattern);
	for (int i = 0; i < L; ++i) {
		scanf(" %c", &ch);
		if (ch == '(') {
			scanf(" %c", &ch);
			while (ch != ')') {
				pattern[i][ch - 'a'] = true;
				scanf(" %c", &ch);
			}
		}
		else pattern[i][ch - 'a'] = true;
	}
}

inline bool check(int now) {
	for (int i = 0; i < L; ++i) if (!pattern[i][words[now][i] - 'a']) return false;
	return true;
}

inline void process() {
	for (int i = 1; i <= N; ++i) {
		getPattern();
		ans = 0;
		for (int j = 0; j < D; ++j) if (check(j)) ++ans;
		printf("Case #%d: %d\n", i, ans);
	}
}

int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	init();
	process();

	return 0;
}
