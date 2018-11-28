#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool isopp[256][256];

int main()
{
	int cases;
	scanf("%d", &cases);
	for (int cas = 1; cas <= cases; cas++) {
		int n, c, i, d;
		char comb[50][5], opp[50][5], str[200];
		scanf("%d", &c);
		for (int i = 0; i < c; i++) scanf("%s", comb[i]);
		memset(isopp, 0, sizeof(isopp));
		scanf("%d", &d);
		for (int i = 0; i < d; i++) {
			scanf("%s", opp[i]);
			isopp[opp[i][0] - 'A'][opp[i][1] - 'A'] = true;
			isopp[opp[i][1] - 'A'][opp[i][0] - 'A'] = true;
		}
		scanf("%d%s", &n, str);
		char res[200];
		int len = 0, j;
		for (i = 0; i < n; i++) {
			res[len] = 0;
			bool act = false;
			if (len > 0) {
				for (j = 0; j < c; j++) {
					if ((res[len - 1] == comb[j][0] && str[i] == comb[j][1]) ||
							(res[len - 1] == comb[j][1] && str[i] == comb[j][0])) {
						res[len - 1] = comb[j][2];
						act = true;
						break;
					}
				}
				if (!act) {
					for (j = 0; j < len; j++) {
						if (isopp[str[i] - 'A'][res[j] - 'A']) {
							len = 0;
							act = true;
							break;
						}
					}
				}
			}
			if (!act) {
				res[len++] = str[i];
			}
		}
		printf("Case #%d: [", cas);
		for (i = 0; i < len; i++) {
			if (i > 0) printf(", ");
			printf("%c", res[i]);
		}
		printf("]\n");
	}
	return 0;
}
