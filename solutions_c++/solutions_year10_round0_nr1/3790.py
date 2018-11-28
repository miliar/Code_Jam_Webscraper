#include <iostream>
#include <fstream>

int r[31];

int main (int argc, char * const argv[]) {
    // insert code here...
	r[0] = 1;
    for (int i = 1; i < 31; i++) {
		r[i] = r[i-1] * 2;
	}
	
	int T, N, K;
	
	FILE* fp = fopen("A-large.in.txt", "r");
	FILE* out = fopen("out", "w");
	fscanf(fp, "%d", &T);
	for (int t = 1; t <= T; t++) {
		
		fscanf(fp, "%d %d", &N, &K);
		fprintf(out, "Case #%d: ", t);
		if (K == 0) {
			fprintf(out, "OFF\n");
		} else {
			if( (K+1) % r[N] == 0)
				fprintf(out, "ON\n");
			else {
				fprintf(out, "OFF\n");
			}
		}
	}
	
	fclose(fp);
	fclose(out);
	
    return 0;
}
