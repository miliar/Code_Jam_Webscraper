#include <stdio.h>


int main() {
	int T;
	scanf("%d", &T);
	for(int z = 1; z <= T; z++) {
		int n, pos[100] = {0};
		scanf("%d", &n);
		for (int i = 1; i <= n; i++) {
			char s[100];
			scanf("%s", s);
			for (int j = 0; s[j] != 0; j++)
				if (s[j] == '1') pos[i] = j + 1;
		}

		int swap = 0;
		for (int i = 1; i <= n; i++) {
			if (pos[i] > i) {
				for (int j = i + 1; j <= n; j++) {
					if (pos[j] <= i) {
						for (int k = j - 1; k >= i; k--) {
							int t = pos[k];
							pos[k] = pos[k + 1];
							pos[k + 1] = t;
							swap++;
						}
						break;
					}
				}
			}
		}
		
		printf("Case #%d: %d\n", z, swap);
	}
	return 0;
}
