#include <stdio.h>
#include <cstring>
#include <cmath>


int main() {
	FILE *fin = fopen("A-small-attempt1.in","r");
	FILE *fout = fopen("out.txt","w");


	int T;
	fscanf(fin,"%d\n",&T);

	for (int t=1; t<=T; t++) {
		int N, PD, PG;
		fscanf(fin,"%d %d %d",&N,&PD,&PG);


		if ((PG == 0 && PD > 0) || (PG == 100 && PD < 100)) {
			fprintf(fout,"Case #%d: Broken\n",t);
		}
		else {
			bool possible = false;

			if (N >= 100) {
				possible = true;
			}
			else {
				for (int i=1; i<=50; i++) {
					if (i > N) break;
					if (100%i == 0) {
						int d = 100/i;
						if (PD%d == 0) {
							possible = true;
							break;
						}
					}
				}
			}

			if (possible) {
				fprintf(fout,"Case #%d: Possible\n",t);
			}
			else {
				fprintf(fout,"Case #%d: Broken\n",t);
			}
		}
	}
}
