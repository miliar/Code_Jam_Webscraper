#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 256

char comb[MAX][MAX], opps[MAX][MAX], str[MAX], out[MAX];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T, t, c, d, n, i, j, k, f;
	char last, pr[10];
	scanf("%d", &T);
	for(t = 1; t <= T; t++){
		memset(comb, 0, sizeof(comb));
		memset(opps, 0, sizeof(opps));
		scanf("%d", &c);
		for(i = 0; i < c; i++){
			scanf("%s", pr);
			comb[pr[0]][pr[1]] = comb[pr[1]][pr[0]] = pr[2];
		}
		scanf("%d", &d);
		for(i = 0; i < d; i++){
			scanf("%s", pr);
			opps[pr[0]][pr[1]] = opps[pr[1]][pr[0]] = 1;
		}
		scanf("%d %s", &n, str);
		last = j = 0;
		for(i = 0; i < n; i++){
			if(comb[last][str[i]]){
				out[j-1] = comb[last][str[i]];
				last = out[j-1];
			}
			else{
				f = 0;
				for(k = 0; k < j; k++){
					if(opps[str[i]][out[k]]){
						f = 1;
						break;
					}
				}
				if(f) last = j = 0;
				else {
					last = out[j] = str[i];
					j++;
				}
			}/*
			for(int ii = 0; ii < j; ii++){
				if(ii) printf(", ");
				printf("%c", out[ii]);
			}
			printf("\n");*/
		}
		printf("Case #%d: [", t);
		for(i = 0; i < j; i++){
			if(i) printf(", ");
			printf("%c", out[i]);
		}
		printf("]\n");
	}
	
	return 0;
}
