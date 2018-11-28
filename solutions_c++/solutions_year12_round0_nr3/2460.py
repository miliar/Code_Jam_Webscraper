#include <cstdio>
#include <cstring>

int visit[2222222];

int solve(int low, int num) {
	char str[16], newstr[16];
	sprintf(str, "%d", num);
	size_t len = strlen(str);
	int newnum, result = 0;
	for (size_t i = 1; i < len; ++ i) {
		memcpy(newstr, str + i, len - i);
		memcpy(newstr + len - i, str, i);
		newstr[len] = '\0';
		sscanf(newstr, "%d", &newnum);
		if (low <= newnum && newnum < num) {
			result += visit[newnum] < num;
			visit[newnum] = num;
		}
	}
	return result;
}

int solve() {
	int l, r, result = 0;
	scanf("%d%d", &l, &r);
	memset(visit, 0, sizeof(visit));
	for (int i = l; i <= r; ++ i) {
		result += solve(l, i);
	}
	return result;
}

int main() {
	int testCases;
	scanf("%d", &testCases);
	for (int t = 1; t <= testCases; ++ t) {
		printf("Case #%d: %d\n", t, solve());
	}
	return 0;
}
