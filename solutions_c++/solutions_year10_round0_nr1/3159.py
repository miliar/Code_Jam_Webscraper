#include <stdio.h>
#include <fstream.h>

int main() {
	int T, N, K;
	int t = 1;
	FILE* f1 = fopen("a.in", "r"); FILE* f2 = fopen("a.out", "w");
	fscanf(f1, "%d", &T); 
	while (t <= T) {
		fscanf(f1, "%d", &N); fscanf(f1, "%d", &K);
		int r = (1 << N) -1;
		if ( (K & r) == r)
			fprintf(f2, "Case #%d: ON\n", t);
		else
			fprintf(f2, "Case #%d: OFF\n", t);
		t ++;
	}
	return 0;
}


