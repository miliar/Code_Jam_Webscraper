#include <iostream>

#include <string.h>

using namespace std;

char s[501], crke[] = " welcome to code jam";
int pos[20], len, n, dp[20][501];

int najdi(int start, char c) {
	for (; start < len; start++)
		if (s[start] == c)
			return start;
	return -1;
}

int solve(int p) {
	if (p == 20)
		return 1;
	if (dp[p][pos[p - 1] + 1]) {
		//cout << p << " " << pos[p - 1] + 1 << endl;
		return dp[p][pos[p - 1] + 1] - 1;
	}
	int c = 0;
	pos[p] = pos[p - 1];
	while ((pos[p] = najdi(pos[p] + 1, crke[p])) != -1) {
		c += solve(p + 1);
		c %= 10000;
	}
	dp[p][pos[p - 1] + 1] = c + 1;
	return c;
}

int main() {
	pos[0] = -1;
	cin >> n; gets(s);
	for (int t = 0; t < n; t++) {
		memset(dp, 0, sizeof(dp));
		gets(s);
		len = strlen(s);
		solve(1);
		printf("Case #%d: %04d\n", t + 1, solve(1));
	}
}

