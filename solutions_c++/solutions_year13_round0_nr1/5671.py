#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>


char check (char b[4][4]) {
	char r[4] = {b[0][0],b[1][0],b[2][0],b[3][0]};
	char c[4]= {b[0][0],b[0][1],b[0][2],b[0][3]};
	char d[2] = {b[0][0], b[0][3]};
	bool done = true;
	for (int i = 0; i < 4; ++i) {
		if (d[0] != 'N' && d[0] != b[i][i] && b[i][i] != 'T') {
			d[0] = 'N';
		}
		if (d[1] != 'N' && d[1] != b[i][3-i] && b[i][3-i] != 'T') {
			d[1] = 'N';
		}

		for (int j = 0; j < 4; ++j) {
			if (b[i][j] != 'T') {
				if (done && b[i][j] == '.') {
					done = false;
				}
				if (r[i] != 'N' && r[i] != b[i][j]) {
					r[i] = 'N';
				}
				if (c[j] != 'N' && c[j] != b[i][j]) {
					c[j] = 'N';
				}
			}
		}
	}

	if (d[1] != 'N' && d[1]  != '.') {
		return d[1];
	}
	if (d[0] != 'N' && d[0]  != '.') {
		return d[0];
	}
	for (int i = 0; i < 4; ++i) {
		if (r[i] != 'N' && r[i] != '.') {
			return r[i];
		}
		if (c[i] != 'N' && c[i] != '.') {
			return c[i];
		}
	}
	if (done) {
		return 'D';
	}
	return 'N';
}

int main () {
	int total, T;
	char board[4][4];

	FILE * file = fopen("test.txt", "r");
	FILE * result = fopen("result.txt", "w");

	fscanf(file, "%d\n", &total);
	T = total;
	while (total) {
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				fscanf(file, "%c", &board[i][j]);
			}
			fscanf(file, "\n");
		}
		char val = check(board);
		switch (val) {
		case 'D':
			fprintf(result, "Case #%d: Draw\n", T-total+1);
			break;
		case 'N':
			fprintf(result, "Case #%d: Game has not completed\n", T-total+1);
			break;
		default:
			fprintf(result, "Case #%d: %c won\n", T-total+1, val);
			break;
		}
		total--;
	}
	fprintf(result, "\n");
	fclose(result);
	fclose(file);
	return 0;
}
