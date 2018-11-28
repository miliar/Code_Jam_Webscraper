// Snapper Chain.cpp: определяет точку входа для консольного приложения.
//

#include <stdio.h>

int T;

int main()
{
	FILE* in = fopen("A-large.in", "r+");
	if(in == NULL) return 1;

	FILE* out = fopen("A-large.out", "w+");

	fscanf(in, "%d", &T);
	
	for(int t=0; t<T; t++){
		printf("\rCase #%d", t+1);
		unsigned int N;
		unsigned long K;

		fscanf(in, "%d %d", &N, &K);

		unsigned long mask = 0;
		mask = ~mask;
		mask = mask<<N;
		K = K|mask;
		K = ~K;
		fprintf(out, "Case #%d: %s\n", t+1, K?"OFF":"ON");
	}
	fclose(out);
	fclose(in);
	return 0;
}

