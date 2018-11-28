#include <stdio.h>
#include <string.h>


int main() {
	int T;
	scanf("%d", &T);

	for (int z = 1; z <= T; z++) {
		char s[30] = {'0'};
		int c[10] = {0};

		scanf("%s", s + 1);
		int len = strlen(s);
		
		int done = 0;
		for (int i = len - 1; !done && i >= 0; i--) {
			c[s[i] - '0']++;
			for (int j = s[i] - '0' + 1; !done && j <= 9; j++) {
				if (c[j]) {
					done = 1;
					s[i] = j + '0';
					c[j]--;
					int p = i + 1, k = 0;
					while (p < len && k <= 9) {
						if (c[k]) {
							c[k]--;
							s[p++] = k + '0';
						} else k++;
					}
				}
			}
		}
		
		printf("Case #%d: ", z);
		if (s[0] > '0') printf("%c", s[0]);
		printf("%s\n", s + 1);
		
	}
	return 0;
}
