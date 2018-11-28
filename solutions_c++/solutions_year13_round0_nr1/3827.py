#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char map[5][5];
FILE *fp, *fw;

int main() {
	int i, j, fo, fx, cse, g = 1, cntx, cnto, cntt, draw;
	fp = fopen("/home/uriel/workspace/A-large.in", "r");
	fw = fopen("/home/uriel/workspace/outA_l.txt", "w");
	fscanf(fp, "%d", &cse);
	while(cse--) {
		for(i = 0; i < 4; ++i) {
			fscanf(fp, "%s", map[i]);
		}
		fx = fo = draw = 0;
		for(i = 0; i < 4; ++i) {
			cntx = cnto = cntt = 0;
			for(j = 0; j < 4; ++j) {
				if(map[i][j] == 'X') cntx++;
				if(map[i][j] == 'O') cnto++;
				if(map[i][j] == 'T') cntt++;
				if(map[i][j] == '.') draw++;
			}
			if ((cntx == 4) || (cntx == 3 && cntt == 1)) fx = 1;
			if ((cnto == 4) || (cnto == 3 && cntt == 1)) fo = 1;
			cntx = cnto = cntt = 0;
			for(j = 0; j < 4; ++j) {
				if(map[j][i] == 'X') cntx++;
				if(map[j][i] == 'O') cnto++;
				if(map[j][i] == 'T') cntt++;
			}
			if ((cntx == 4) || (cntx == 3 && cntt == 1)) fx = 1;
			if ((cnto == 4) || (cnto == 3 && cntt == 1)) fo = 1;
		}
		cntx = cnto = cntt = 0;
		for(i = 0; i < 4; ++i) {
			if(map[i][i] == 'X') cntx++;
			if(map[i][i] == 'O') cnto++;
			if(map[i][i] == 'T') cntt++;
		}
		if ((cntx == 4) || (cntx == 3 && cntt == 1)) fx = 1;
		if ((cnto == 4) || (cnto == 3 && cntt == 1)) fo = 1;
		cntx = cnto = cntt = 0;
		for(i = 0; i < 4; ++i) {
			if(map[i][3 - i] == 'X') cntx++;
			if(map[i][3 - i] == 'O') cnto++;
			if(map[i][3 - i] == 'T') cntt++;
		}
		if ((cntx == 4) || (cntx == 3 && cntt == 1)) fx = 1;
		if ((cnto == 4) || (cnto == 3 && cntt == 1)) fo = 1;
		fprintf(fw, "Case #%d: ", g++);
		if(fx == 0 && fo == 0 && !draw) fprintf(fw,"Draw\n");
		else if(fx == 1) fprintf(fw, "X won\n");
		else if(fo == 1) fprintf(fw, "O won\n");
		else if(draw) fprintf(fw, "Game has not completed\n");
	}
	fclose(fp);
	fclose(fw);
	return 0;
}
