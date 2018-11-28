#include <stdio.h>
#include <algorithm>

int n, len;
char s[30];
int min, pos;

int main() {
	int i, j, k;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &n);
	for (i = 1; i <= n; i++) {
		scanf("%s", s);
		for (len = 0; s[len] != (char) NULL; len++);
		for (j = len - 1; j > 0; j--)
			if (s[j - 1] < s[j]) break;
		if (j == 0) {
			s[len++] = s[0];
			s[len] = (char) NULL;
			s[0] = '0';
			std::sort(s, s + len);
			for (j = 0; s[j] == '0'; j++);
			k = s[0]; s[0] = s[j]; s[j] = k;
		} else {
			k = j - 1;
			min = INT_MAX;
			pos = -1;
			for (; j < len; j++)
				if (s[k] < s[j] && min > s[j]) {
					min = s[j];
					pos = j;
				}
			s[pos] = s[k]; s[k] = min;
			std::sort(s + k + 1, s + len);
		}
		printf("Case #%d: %s\n", i, s);
	}
	return 0;
}