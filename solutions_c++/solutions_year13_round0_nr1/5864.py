#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<stdlib.h>

bool checkRow(int row, char player);
bool checkColumn(int column, char player);
bool checkDiagonal(int diagonal, char player);

char grid[5][4];
FILE *input;
FILE *output;

int main(int argC, char *argV[]) {
	char *fileIn = argV[1];
	
	input = fopen(argV[1], "r");
	output = fopen("A.out", "w");

	char buff[255] = {0};

	int lines;

	fgets(buff, 255, input);
	sscanf(buff, "%d", &lines);

	for (int i = 0; i < lines; i++) {
		bool flag = false;
		bool filled = true;
		fprintf(output, "Case #%d: ", i + 1);
		for (int j = 0; j < 4; j++) {
			fscanf(input, "%s\n", buff);
			memset(grid[j], 0, 5);
			strncpy(grid[j], buff, 4);
			char *pcheck = strchr(grid[j], '.'); 
			if (filled && pcheck != NULL)
				filled = false;
		}

		//check rows
		for (int r = 0; r < 4; r++) {
			if (checkRow(r, 'X') || checkRow(r, 'O')) {
				flag = true;
				break;
			}
		}
		
		if (flag)
			continue;

		//check columns
		for (int c = 0; c < 4; c++) {
			if (checkColumn(c, 'X') || checkColumn(c, 'O')) {
				flag = true;
				break;
			}
		}
		
		if (flag)
			continue;

		//check diagonal
		if (checkDiagonal(0, 'X') || checkDiagonal(0, 'O') ||
			checkDiagonal(1, 'X') || checkDiagonal(1, 'O')) {
				continue;
		}

		if (filled)
			fprintf(output, "Draw\n");
		else
			fprintf(output, "Game has not completed\n");
	}

	fclose(input);
	fclose(output);
	return 0;
}

bool checkRow(int row, char player) {
	for (int i = 0; i < 4; i++){
		if (grid[i][row] != player && grid[i][row] != 'T') {
			return false;
		}
	}
	fprintf(output, "%c won\n", player);
	return true;
}

bool checkColumn(int column, char player) {
	for (int i = 0; i < 4; i++){
		if (grid[column][i] != player && grid[column][i] != 'T') {
			return false;
		}
	}
	fprintf(output, "%c won\n", player);
	return true;
}

bool checkDiagonal(int diagonal, char player) {
	for (int i = 0; i < 4; i++){
		int column = diagonal ? i : 3 - i;
		if (grid[column][i] != player && grid[column][i] != 'T') {
			return false;
		}
	}
	fprintf(output, "%c won\n", player);
	return true;
}