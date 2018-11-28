#include <stdio.h>

#define MAXN 1100

int n;

int main(){
	int t, CASE, i, min, sum, ans, data;
	FILE *fpin, *fpout;
	fpin = fopen("C.in", "r");
	fpout = fopen("C.out", "a");
	fscanf(fpin, "%d", &CASE);
	for(t = 1; t <= CASE; t ++){
		fscanf(fpin, "%d", &n);
		min = 210000000;
		sum = 0;
		ans = 0;
		for(i = 0; i < n; i ++){
			fscanf(fpin, "%d", &data);
			ans = ans ^ data;
			sum += data;
			if(min > data) min = data;
		}
		fprintf(fpout, "Case #%d: ", t);
		if(ans) fprintf(fpout, "NO\n");
		else fprintf(fpout, "%d\n", sum - min);
	}
	fclose(fpin);
	fclose(fpout);
	return 0;
}
