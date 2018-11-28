#include <stdio.h>
#include <stdlib.h>

char comb[36][3], opp[28][2], out[100];

int search(int ctr, char match) {
	int ctr_temp;
	for(ctr_temp = ctr-1; ctr_temp > -1; ctr_temp--)
		if(match == out[ctr_temp])
			return ctr_temp;
	return ctr;
}

int main() {
	int t, tc, c, cc, d, dc, n, nc, ctr, ctr_temp;
	char in, match;

	FILE *ifile, *ofile;
	ifile = fopen("input", "r");
	ofile = fopen("output", "w");

	fscanf(ifile, "%d\n", &t);

	for(tc = 0; tc < t; tc++) {
		fscanf(ifile, "%d ", &c);
		for(cc = 0; cc < c; cc++) {
			fscanf(ifile, "%c%c%c ", &comb[cc][0], &comb[cc][1], &comb[cc][2]);
		}
		
		fscanf(ifile, "%d ", &d);
		for(dc = 0; dc < d; dc++) {
			fscanf(ifile, "%c%c ", &opp[dc][0], &opp[dc][1]);
		}

		fscanf(ifile, "%d ", &n);
		for(nc = 0, ctr = 0; nc < n; nc++) {
			fscanf(ifile, "%c", &in);
			
			for(cc = 0; cc < c; cc++) {
				if(comb[cc][0] == in) {
					if(ctr > 0 && (out[ctr-1] == comb[cc][1])) {
						out[ctr-1] = comb[cc][2];
						break;
					}
				}
				else {
					if(comb[cc][1] == in) {
						if(ctr > 0 && (out[ctr-1] == comb[cc][0])) {
							out[ctr-1] = comb[cc][2];
							break;
						}
					}
				}
			}

			if(cc != c)
				continue;

			for(dc = 0; dc < d; dc++) {
				if(opp[dc][0] == in) {
					ctr_temp = search(ctr, opp[dc][1]);
					if(ctr != ctr_temp) {
						ctr = 0;
						break;
					}
				}
				else {
					if(opp[dc][1] == in) {
						ctr_temp = search(ctr, opp[dc][0]);
						if(ctr != ctr_temp) {
							ctr = 0;
							break;
						}
					}
				}
			}
			if(dc == d) {
				out[ctr++] = in;
			}
		}

		if(ctr == 0)
			fprintf(ofile, "Case #%d: []\n", tc+1);
		else {
			fprintf(ofile, "Case #%d: [%c", tc+1, out[0]);
			for(ctr_temp = 1; ctr_temp < ctr; ctr_temp++){
				fprintf(ofile, ", %c", out[ctr_temp]);
			}
			fprintf(ofile, "]\n");
		}
	}
}
