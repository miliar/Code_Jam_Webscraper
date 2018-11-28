#include <stdio.h>

int main (int argc, char * const argv[]) {
    // insert code here...
    int N;
	int A[1001];
	int B[1001];
	
	FILE *in = fopen("A-large-1.in.txt", "r");
	FILE *out = fopen("A-large.out.txt", "w");
	
	int T;
	fscanf(in, "%d", &T);
	for (int t=1; t<=T; t++) {
	
	fscanf(in, "%d", &N);
	for (int i=0; i<N; i++) {
		fscanf(in, "%d %d", &A[i], &B[i]);
	}
	int intersect = 0;
	for (int i=0; i<N; i++) {
		for (int j=i+1; j<N; j++) {
			if ( (A[i]-A[j])*(B[i]-B[j]) < 0 ) {
				++intersect;
			}
		}
	}
	fprintf(out, "Case #%d: %d\n", t, intersect);
		
	}
	
	fclose(in);
	fclose(out);
	
    return 0;
}
