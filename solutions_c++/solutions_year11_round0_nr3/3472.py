#include <stdio.h>

FILE *fin, *fout;
int process(void)
{
	int N, B[1010][22]={0};
	int sum[22], ret=0, min = 9999999;
	fscanf(fin, "%d", &N);
	int i, j, x;
	for (i=0;i<N;++i){
		fscanf(fin, "%d", &x);
		if (min > x) min = x;
		ret = ret + x;
		for (j=0;j<20;++j){
			B[i][j] = (x & 1);
			sum[j] += B[i][j];
			x = x >> 1;
		}
	}
	for (i=0;i<20;++i){
		if ((sum[i]&1) == 1) return -1;
	}
	return ret-min;
}
int main(void)
{
	fin = fopen("input.txt", "r");
	fout = fopen("output.txt", "w");
	int T, t, o;
	fscanf(fin, "%d", &T);
	for (t=1;t<=T;++t){
		o = process();
		if (o >= 0)
			fprintf(fout, "Case #%d: %d\n", t, o);
		else
			fprintf(fout, "Case #%d: NO\n", t);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}