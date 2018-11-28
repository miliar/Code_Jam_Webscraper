#include <stdio.h>
#include <stdlib.h>

int main() {
	int t, tc, n, nc, in, tot0, tot1, min;
	
	FILE *ifile, *ofile;
	ifile = fopen("input","r");
	ofile = fopen("output", "w");

	fscanf(ifile, "%d\n", &t);

	for(tc = 0; tc < t; tc++) {
		fscanf(ifile, "%d\n", &n);
		tot0 = 0;
		tot1 = 0;
		min = 0xfffffff;
		
		for(nc = 0; nc < n; nc++) {
			fscanf(ifile, "%d ", &in);
			tot1 += in;
			tot0 ^= in;
			if(in < min)
				min = in;
		}
		if(tot0 != 0)
			fprintf(ofile, "Case #%d: NO\n", tc+1);
		else
			fprintf(ofile, "Case #%d: %d\n", tc+1, tot1-min);
	}
}
