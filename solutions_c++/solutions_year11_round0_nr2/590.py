#include <stdio.h>

int main() {
	int t,c;
	scanf("%d",&t);
	for (c=1;c<=t;++c) {
		int C,d,n;
		char comb[100][5];
		char opp[100][5];
		char line[1000];
		scanf("%d ", &C);
		for (int i = 0; i < C; i++)
			scanf("%s ", comb[i]);
		scanf("%d ", &d);
		for (int i = 0; i < d; i++)
			scanf("%s ", opp[i]);
		scanf("%d ", &n);
		int j = 0;
		for (int i = 0; i < n; i++) {
			scanf("%c", &line[j]);
			// combine:
			if (j) {
				for (int k = 0; k < C; k++) {
					if (line[j-1] == comb[k][0] && line[j] == comb[k][1] ||
						line[j-1] == comb[k][1] && line[j] == comb[k][0]) {
						line[j-1] = comb[k][2];
						j--;
					}
				}
			}
			j++;
			for (int k = 0; k < d; k++) {
				int l;
				for (l = 0; l < j; l++)
					if (line[l] == opp[k][0])
						break;
				if (l == j)
					continue;
				for (l = 0; l < j; l++)
					if (line[l] == opp[k][1])
						break;
				if (l == j)
					continue;
				j = 0;
				break;
			}
			line[j] = 0;
		}
		printf("Case #%d: [",c);
		for (int k = 0; k < j; k++)
			if (k < j - 1)
				printf("%c, ", line[k]);
			else
				printf("%c", line[k]);
		printf("]\n");
	}
	return 0;
}
