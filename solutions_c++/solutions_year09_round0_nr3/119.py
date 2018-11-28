#include <cstdio>
#include <memory>
#include <cstring>

const int plen = 19;
const char pattern[20] = "welcome to code jam";
const int maxlen = 500;
const int Number = 10000;

int casei, cases, len, now, last;
int DP[2][plen];
char text[maxlen + 1];

inline void init() {
	gets(text);
}

inline void process() {
	memset(DP[0], 0, sizeof DP[0]);
	len = strlen(text);
	now = 0;
	for (int i = 0; i < len; ++i) {
		last = now; now ^= 1;
		
		if (text[i] == pattern[0]) DP[now][0] = (DP[last][0] + 1) % Number;
		else DP[now][0] = DP[last][0];
		for (int j = 1; j < plen; ++j)
			if (text[i] == pattern[j]) DP[now][j] = (DP[last][j - 1] + DP[last][j]) % Number;
			else DP[now][j] = DP[last][j];
	}
}

inline void print() {
	printf("Case #%d: %04d\n", casei, DP[now][plen - 1]);
}

int main() {
	//freopen("Bin.txt", "r", stdin);
	//freopen("C-small-attempt0.in", "r", stdin);
	//freopen("C-small-attempt0.out", "w", stdout);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	scanf("%d", &cases); gets(text);
	for (casei = 1; casei <= cases; ++casei) {
		init();
		process();
		print();
	}

	return 0;
}
