#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
	FILE *fp;
	if((fp=fopen(argv[1],"r"))==NULL) {
		printf("Cannot open file.\n");
		exit(1);
	}

	unsigned int T, N, S, p, Score, MaxS, Rem, Quo, i, j, Sol;

	fscanf_s(fp, "%d%*c", &T);
	for (i = 1; i <= T; i++) {
		Sol = 0;

		fscanf_s(fp, "%d%d%d", &N, &S, &p);
		for (j = 1; j <= N; j++) {
			fscanf_s(fp, "%d", &Score);
			Rem = Score % 3;
			Quo = Score / 3;

			if (Rem == 0)
				MaxS = Quo;
			else
				MaxS = Quo + 1;

			if (MaxS >= p) {
				Sol++;
			} else {
				if ( (MaxS + 1 == p) && (S > 0) && (Rem != 1) && (Score > 1) ) {
					Sol++;
					S--;
				}
			}
		}

		printf ("Case #%d: %d\n", i, Sol);
		fscanf_s(fp, "%*c");
	}
	fclose(fp);
	return 0;
}