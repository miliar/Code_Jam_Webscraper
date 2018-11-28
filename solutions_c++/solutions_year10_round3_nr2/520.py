#include <stdio.h>

int main (int argc, char * const argv[]) {
    // insert code here...
    
	int L, P, C;
	
	FILE *in = fopen("B-small-attempt0.in.txt", "r");
	FILE *out = fopen("B-small.out.txt", "w");
	
	int T;
	fscanf(in, "%d", &T);
	for (int t=1; t<=T; t++) {
	
	fscanf(in, "%d %d %d", &L, &P, &C);
	int segment = 0;
	for (int i=L; i<P; i*=C)
		++segment;
	--segment;
	int cnt = 0;
	int k=segment;
	while (k!=0) {
		k=k/2;
		++cnt;
	}
	
	fprintf(out, "Case #%d: %d\n", t, cnt);
		
	}
	
	fclose(in);
	fclose(out);
	
    return 0;
}
