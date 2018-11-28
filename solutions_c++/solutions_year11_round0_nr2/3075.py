#include <stdio.h>
#include <cstring>

int main() {
	int T;
	scanf("%d", &T);
	int tc;
	int combine[26][26];
	int opp[26][26];
	int i, j, k;
	char c[1024];
	char res[1024];
	for (tc = 1; tc <= T; tc++) {
		memset(combine, 0, sizeof(combine));
		memset(opp, 0, sizeof(opp));
		scanf("%d", &i);
		for (j = 0; j < i; j++) {
			scanf("%s", c);
			combine[c[0]-'A'][c[1]-'A'] = combine[c[1]-'A'][c[0]-'A'] = c[2];
		}
		scanf("%d", &i);
		for (j = 0; j < i; j++) {
			scanf("%s", c);
			opp[c[0]-'A'][c[1]-'A'] = opp[c[1]-'A'][c[0]-'A'] = true;
		}
		memset(res, 0, sizeof(res));
		char *resit = res;
		scanf("%d %s", &i, c);
		k = 0;
		for (j = 0; j < i; j++) {
			if (k && combine[k-'A'][c[j]-'A']) {
				*(resit-1) = combine[k-'A'][c[j]-'A'];
				k = 0;
			} else {
				*(resit++) = k = c[j];
			}
			char* verit = res;
			while (*verit) {
				if (opp[k-'A'][(*verit)-'A']) {
					memset(res, 0, sizeof(res));
					resit = res;
					k = 0;
					break;
				}
				verit++;
			}
		}

		printf("Case #%d: [", tc);
		for (i = 0; i < strlen(res); i++) {
			if (i) printf(", ");
			printf("%c", res[i]);			
		}
		printf("]\n");
	}
}

