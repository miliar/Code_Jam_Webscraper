#include <stdio.h>
#include <string.h>
#include <stdlib.h>

FILE *fin, *fout;

int main(void) {
	int T;
	int i, j, k;
	char side;
	char flag;
	char board[4][4];
	char full;
	fin = fopen("t.in", "r");
	fout = fopen("t.out", "w+");
	
	fscanf(fin, "%d\n", &T);
	for(i = 1; i <= T; i++) {
		full = true;
		flag = true;
		for(j = 0; j < 4; j++) {
			for(k = 0; k < 4; k++) {
				board[j][k] = fgetc(fin);
				if(board[j][k]=='.')
					full = false;
			}
			fgetc(fin);
		}
		fgetc(fin);
		for(j = 0; flag && j < 4; j++) {
			side = board[j][0];
			if(side == 'T') {
				side = board[j][1];
			}
			flag = false;
			for(k = 0; k < 4; k++) {
				if(board[j][k] != side && board[j][k] != 'T') {
					flag = true;
					break;
				}
				if(board[j][k] == '.') {
					flag = true;
					break;
				}
			}
		}
		if(!flag) {
			fprintf(fout, "Case #%d: %c won\n", i, side);
			continue;
		}
		for(j = 0; flag && j < 4; j++) {
			side = board[0][j];
			if(side == 'T') {
				side = board[1][j];
			}
			flag = false;
			for(k = 0; k < 4; k++) {
				if(board[k][j] != side && board[k][j] != 'T') {
					flag = true;
					break;
				}
				if(board[k][j] == '.') {
					flag = true;
					break;
				}
			}
		}
		if(!flag) {
			fprintf(fout, "Case #%d: %c won\n", i, side);
			continue;
		}
		side = board[0][0];
		if(side == 'T') {
			side = board[1][1];
		}
		flag = false;
		for(k = 0; k < 4; k++) {
			if(board[k][k] != side && board[k][k] != 'T') {
				flag = true;
				break;
			}
			if(board[k][k] == '.') {
				flag = true;
				break;
			}
		}
		if(!flag) {
			fprintf(fout, "Case #%d: %c won\n", i, side);
			continue;
		}
		
		side = board[0][3];
		if(side == 'T') {
			side = board[1][2];
		}
		flag = false;
		for(k = 0; k < 4; k++) {
			if(board[k][3-k] != side && board[k][3-k] != 'T') {
				flag = true;
				break;
			}
			if(board[k][3-k] == '.') {
				flag = true;
				break;
			}
		}
		if(!flag) {
			fprintf(fout, "Case #%d: %c won\n", i, side);
			continue;
		}
		if(full) {
			fprintf(fout, "Case #%d: Draw\n", i);
		}
		else {
			fprintf(fout, "Case #%d: Game has not completed\n", i);
		}
	}
	return 0;
}
