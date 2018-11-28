#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct trip {
	char a1, a2, b;
} trip;

int main() {
	FILE *fin = fopen("magica.txt", "r");
	int T;
	trip com[80], opp[80];
	char str[500], out[500];
	bool flag[500];
	
	fscanf(fin, "%d", &T);
	
	for (int t = 1; t <= T; t++) {
		int C, D, N;
		//get input
		fscanf(fin, "%d", &C);
		for (int c = 0; c < C; c++) {
			char tmp1, tmp2, tmp3;
			tmp1 = fgetc(fin);
			tmp1 = fgetc(fin);
			tmp2 = fgetc(fin);
			tmp3 = fgetc(fin);
			
			com[c].a1 = tmp1;
			com[c].a2 = tmp2;
			com[c].b = tmp3;
			com[c+C].a1 = tmp2;
			com[c+C].a2 = tmp1;
			com[c+C].b = tmp3;
		}
		C = 2*C;
		fscanf(fin, "%d", &D);
		for (int d = 0; d < D; d++) {
			char tmp1, tmp2, tmp3;
			tmp1 = fgetc(fin);
			tmp1 = fgetc(fin);
			tmp2 = fgetc(fin);
			tmp3 = fgetc(fin); // I think this gets rid of the space for me
			
			opp[d].a1 = tmp1;
			opp[d].a2 = tmp2;
			opp[d+D].a1 = tmp2;
			opp[d+D].a2 = tmp1;
		}
		D = 2*D;
		fscanf(fin, "%d", &N);
		fgetc(fin);
		fgets(str, 101, fin);
		
		for (int n = 0; n < 500; n++) flag[n] = false;
		
		int m = 0;
		for (int n = 0; n < N; n++) {
			char tmp = str[n];
			//combined then opposed
			for (int k = 0; k < C; k++) {
				if (m-1 >= 0 && com[k].a1 == tmp && com[k].a2 == out[m-1]) {
					out[m-1] = com[k].b;
					goto end;
				}
			}
			for (int k = 0; k < D; k++) {
				for (int j = 0; j < m; j++) {
					//clear the entire list
					if (opp[k].a1 == tmp && opp[k].a2 == out[j]) {
						out[0] = 0;
						m = 0;
						goto end;
					}
				}
			}
			out[m] = tmp;
			m++;
end:
			continue;
		}
		out[m] = 0;
		
		printf("Case #%d: [", t);
		for (int k = 0; k < m-1; k++) {
			printf("%c, ", out[k]);
		}
		if (m-1 >= 0) printf("%c", out[m-1]);
		printf("]\n");
	}
	
	return 0;
}