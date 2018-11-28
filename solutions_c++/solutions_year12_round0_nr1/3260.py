#include <stdio.h>

int main () {
    FILE *fin  = fopen ("A-small-attempt0.in", "r");
    FILE *fout = fopen ("test.out", "w");
    
	int inv[26];

	inv[0] = 24;
	inv[1] = 7;
	inv[2] = 4;
	inv[3] = 18;
	inv[4] = 14;
	inv[5] = 2;
	inv[6] = 21;
	inv[7] = 23;
	inv[8] = 3;
	inv[9] = 20;
	inv[10] = 8;
	inv[11] = 6;
	inv[12] = 11;
	inv[13] = 1;
	inv[14] = 10;
	inv[15] = 17;
	inv[16] = 25;
	inv[17] = 19;
	inv[18] = 13;
	inv[19] = 22;
	inv[20] = 9;
	inv[21] = 15;
	inv[22] = 5;
	inv[23] = 12;
	inv[24] = 0;
	inv[25] = 16;

    int n, T, m, i;
	char c;
	fscanf (fin, "%d", &n);
	fscanf(fin, "%c", &c);
	for (T = 1; T <= n; T++) {
		fprintf(fout, "Case #%d: ", T);
		do {
			fscanf(fin, "%c", &c);
			if (c == '\n')
				fprintf(fout, "\n");
			else { 
				if (c == ' ')
					fprintf(fout, " ");
				else
					fprintf(fout, "%c", 'a' + inv[c - 'a']);
			}
		} while(c != '\n');
	}
    return 0;
}