#include <stdio.h>

int main(void)
{
	int T, t;
	int N, K;
	FILE *fin = fopen("input.txt", "r");
	FILE *fout = fopen("output.txt", "w");
	fscanf(fin, "%d", &T);
	for (t=1;t<=T;++t){
		fscanf(fin, "%d %d", &N, &K);
		fprintf(fout, "Case #%d: ", t);
		if ((K&((1<<N)-1)) == ((1<<N)-1)) fprintf(fout, "ON\n");
		else fprintf(fout, "OFF\n");
	}
	return 0;
}