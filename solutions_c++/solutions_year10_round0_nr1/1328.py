#include<stdio.h>

int masks[30];

FILE *fin, *fout;

int main(){
	fin = fopen("input.txt", "r");
	fout = fopen("output.txt", "w");

	int i;
	masks[0] = 1;
	for(i = 1; i < 30; i++)
		masks[i] = masks[i - 1] * 2 + 1;
	
	for(i = 0; i < 30; i++)
		printf("%d ", masks[i]);
	printf("\n");

	int casecnt, curcasecnt;
	fscanf(fin, "%d", &casecnt);
	curcasecnt = casecnt;
	
	while(casecnt--){
		int n, k;
		fscanf(fin, "%d %d", &n, &k);
		if((k & masks[n - 1]) == masks[n - 1])
			fprintf(fout, "Case #%d: ON\n", curcasecnt - casecnt);
		else
			fprintf(fout, "Case #%d: OFF\n", curcasecnt - casecnt);
	}

	return 0;
}