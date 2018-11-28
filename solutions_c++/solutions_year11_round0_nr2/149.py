#include <cstdio>

int main() {
	int T;
	scanf("%d", &T);
	for (int Ti = 0; Ti < T; ++Ti) {
		char combine[300][300] = {};
		bool oppo[300][300] = {};
		int c;
		scanf("%d", &c);
		for (int i = 0; i < c; ++i) {
			char s[5];
			scanf("%s", s);
			combine[s[1]][s[0]] = combine[s[0]][s[1]] = s[2];
		}
		scanf("%d", &c);
		for (int i = 0; i < c; ++i) {
			char s[5];
			scanf("%s", s);
			oppo[s[1]][s[0]] = oppo[s[0]][s[1]] = true;
		}
		int n;
		scanf("%d ", &n);
		char list[400];
		int len = 0;
		for (int i = 0; i < n; ++i) {
			char ch;
			scanf("%c", &ch);
			list[len++] = ch;
			while (len >= 2 && combine[list[len - 1]][list[len - 2]] != 0) {
				list[len - 2] = combine[list[len - 1]][list[len - 2]];
				--len;
			}
			for (int j = 0; j < len; ++j) {
				if (oppo[list[j]][list[len - 1]])
					len = 0;
			}
		}
		printf("Case #%d: [", Ti + 1);
		for (int i = 0; i < len; ++i) {
			if (i)
				printf(", ");
			printf("%c", list[i]);
		}
		printf("]\n");
	}
}
