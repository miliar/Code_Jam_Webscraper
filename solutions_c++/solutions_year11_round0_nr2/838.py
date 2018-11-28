#include <stdio.h>
#include <string.h>

int main()
{
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; ++Case) {
		char combine[26][26];
		int opposed[26][26];
		memset(combine, 0, sizeof(combine));
		memset(opposed, 0, sizeof(opposed));
		int C, D, N;
		scanf("%d", &C);
		for (int i = 0; i < C; ++i) {
			char str[4];
			scanf("%s", str);
			combine[str[0] - 'A']
				[str[1] - 'A']
				= str[2];
			combine[str[1] - 'A']
				[str[0] - 'A']
				= str[2];
		}
		scanf("%d", &D);
		for (int i = 0; i < D; ++i) {
			char str[4];
			scanf("%s", str);
			opposed[str[0] - 'A']
				[str[1] - 'A']
				= 1;
			opposed[str[1] - 'A']
				[str[0] - 'A']
				= 1;
		}
		scanf("%d", &N);
		char invoke[101];
		char list[101];
		scanf("%s", invoke);
		int k = 0;
		for (int i = 0; i < N; ++i) {
			list[k++] = invoke[i];
			if (k < 2)
				continue;
			while ((1)) {
				if (k < 2)
					break;
				int x = list[k - 1] - 'A';
				int y = list[k - 2] - 'A';
				if (combine[x][y]) {
					k -= 2;
					list[k++] = combine[x][y];
				} else
					break;
			}
			for (int p = 0; p < k; ++p) {
				for (int q = p + 1; q < k; ++q) {
					int x = list[p] - 'A';
					int y = list[q] - 'A';
					if (opposed[x][y])
						k = 0;
				}
			}
		}
		printf("Case #%d: [", Case);
		if (k)
			printf("%c", list[0]);
		for (int i = 1; i < k; ++i)
			printf(", %c", list[i]);
		printf("]\n");
	}
	return 0;
}

