#include<stdio.h>
#include<string.h>

int nCase;
char comb[128][128], opps[128][128];

int main() {
	int len;
	char str[128], out[128];
	scanf("%d", &nCase);
	for(int cs = 1; cs <= nCase; ++cs) {
		int C, D, N;
		memset(comb, 0, sizeof(comb));
		memset(opps, 0, sizeof(opps));
		for(scanf("%d", &C); C > 0; --C) {
			scanf(" %s", str);
			comb[str[0]][str[1]] = str[2];
			comb[str[1]][str[0]] = str[2];
		}
		for(scanf("%d", &D); D > 0; --D) {
			scanf(" %s", str);
			opps[str[0]][str[1]] = 1;
			opps[str[1]][str[0]] = 1;
		}
		scanf("%d %s", &N, str);
		len = 0;
		for(int i = 0; i < N; ++i) {
			if(len > 0 && comb[out[len-1]][str[i]] != 0)
				out[len-1] = comb[out[len-1]][str[i]];
			else {
				int j;
				for(j = 0; j < len; ++j)
					if(opps[out[j]][str[i]]) break;
				if(j < len) len = 0;
				else out[len++] = str[i];
			}
		}
		printf("Case #%d: [", cs);
		if(len > 0) printf("%c", out[0]);
		for(int i = 1; i < len; ++i)
			printf(", %c", out[i]);
		printf("]\n");
	}
}

