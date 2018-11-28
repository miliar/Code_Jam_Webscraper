// test1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdlib.h"
#include "string.h"
#include "case.h"

void tomek(FILE *fIn, FILE *fOut);
void tomekCase(FILE *fIn, FILE *fOut, int T);
int tomekCheck(char* line);

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fIn = fopen("A-large.in", "r+");
	FILE *fOut = fopen("A-large.out", "w+");

	tomek(fIn, fOut);

	fclose(fIn);
	fclose(fOut);

	return 0;
}

void tomek(FILE *fIn, FILE *fOut) {
	int T;
	fscanf (fIn, "%d\n", &T);

	char * temp = (char *)malloc(2);
	for (int i = 0; i < T; i++) {
		tomekCase(fIn, fOut, i);
		fscanf (fIn, "\n", temp);
	}
	free(temp);
}

void tomekCase(FILE *fIn, FILE *fOut, int T) {
	char matrix[4][4];

	for (int i = 0; i < 4; i++) {
		fscanf (fIn, "%c %c %c %c\n", &matrix[i][0], &matrix[i][1], &matrix[i][2], &matrix[i][3]);
	}

	int res = -1;
	int ae = 0;
	for (int i = 0; i < 4; i++) {
		char *line = matrix[i];
		res = tomekCheck(line);
		if (res == 0) {
			fprintf(fOut, "Case #%d: %s\n", T + 1, "X won");
			return;
		}
		else if (res == 1) {
			fprintf(fOut, "Case #%d: %s\n", T + 1, "O won");
			return;
		}
		else if (res == 3) {
			ae = 1;
		}
	}

	for (int i = 0; i < 4; i++) {
		char line[4];
		for (int j = 0; j < 4; j++) {
			line[j] = matrix[j][i];
		}

		res = tomekCheck(line);
		if (res == 0) {
			fprintf(fOut, "Case #%d: %s\n", T + 1, "X won");
			return;
		}
		else if (res == 1) {
			fprintf(fOut, "Case #%d: %s\n", T + 1, "O won");
			return;
		}
		else if (res == 3) {
			ae = 1;
		}
	}

	{
		char line[4];
		for (int j = 0; j < 4; j++) {
			line[j] = matrix[j][j];
		}

		res = tomekCheck(line);
		if (res == 0) {
			fprintf(fOut, "Case #%d: %s\n", T + 1, "X won");
			return;
		}
		else if (res == 1) {
			fprintf(fOut, "Case #%d: %s\n", T + 1, "O won");
			return;
		}
		else if (res == 3) {
			ae = 1;
		}
	}

	{
		char line[4];
		for (int j = 0; j < 4; j++) {
			line[j] = matrix[j][3 - j];
		}

		res = tomekCheck(line);
		if (res == 0) {
			fprintf(fOut, "Case #%d: %s\n", T + 1, "X won");
			return;
		}
		else if (res == 1) {
			fprintf(fOut, "Case #%d: %s\n", T + 1, "O won");
			return;
		}
		else if (res == 3) {
			ae = 1;
		}
	}

	if (ae == 1) {
		fprintf(fOut, "Case #%d: %s\n", T + 1, "Game has not completed");
		return;
	}
	else {
		fprintf(fOut, "Case #%d: %s\n", T + 1, "Draw");
		return;
	}
}

int tomekCheck(char* line) {
	int ax = 0, ao = 0, ae = 0;
	for (int i = 0; i < 4; i++) {
		if (line[i] == 'X') {
			ax = 1;
		}
		else if (line[i] == 'O') {
			ao = 1;
		}
		else if (line[i] == '.') {
			ae = 1;
		}
	}

	int res = -1;
	if (ae == 1) {
		res = 3;
	}
	else if (ax == 0) {
		res = 1;
	}
	else if (ao == 0) {
		res = 0;
	}

	return res;
}

