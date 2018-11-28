// SquareTiles.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <stdio.h>

char table[50][50];
char result[50][50];
char preRow[50];

int C, R;

bool check() {
	for(int i = 0; i < 50; i++) 
		preRow[i] = 0;

	int blueCount = 0;
	for(int j = 0; j < C; j++) {
		if(table[0][j] == '.')
			result[0][j] = '.';
		else if(table[0][j] == '#') {
			if(blueCount % 2 == 0) {
				result[0][j] = '/';
				preRow[j] = 1;
			}else {
				result[0][j] = '\\';
				preRow[j] = 2;
			}
			blueCount++;
		}
	}

	if(blueCount % 2 != 0)
		return false;

	for(int i = 1; i< R; i++) {
		blueCount = 0;
		for(int j = 0; j < C; j++) {
			if(table[i][j] == '.') {
				if(preRow[j] != 0)
					return false;
				else
					result[i][j] = '.';
			}
			if(table[i][j] == '#') {
				if(blueCount % 2 == 0) {
					if(j == C -1) return false;
					if(preRow[j] == 0) {
						if(preRow[j + 1] != 0)
							return false;
						else {
							result[i][j] = '/';
							preRow[j] = 1;
						}
					} else if(preRow[j] == 1){
						result[i][j] = '\\';
						preRow[j] = 0;
					} else {
						return false;
					}
				} else {
					if(preRow[j] == 2) {
						result[i][j] = '/';
						preRow[j] = 0;
					} else if(preRow[j] == 0) {
						result[i][j] = '\\';
						preRow[j] = 2;
					} else {
						return false;
					}
				}

				blueCount++;
			}
		}
		if(blueCount % 2 != 0)
			return false;
	}

	for(int i = 0; i < C; i++)
		if(preRow[i] != 0)
			return false;

	return true;
}

void printResult(FILE* out) {
	for(int i = 0; i < R; i++) {
		for(int j = 0; j < C; j++)
			fprintf(out, "%c", result[i][j]);
		fprintf(out, "\n");
	}
}

void printInput()
{
	for(int i = 0; i < R; i++) {
		for(int j = 0; j < C; j++)
			printf("%c", table[i][j]);
		printf("\n");
	}
}
int _tmain(int argc, _TCHAR* argv[])
{
	FILE* ifile = fopen("A-large.in", "r");
	if(ifile == NULL) {
		printf("open file error!");
		return -1;
	}
	FILE* out = fopen("out", "w");

	int recordNo;
	fscanf(ifile, "%d", &recordNo);
	printf("Record: %d\n", recordNo);

	int i = 1;

	char temp;
	fscanf(ifile, "%c", &temp);
	while(i <= recordNo) {
		fscanf(ifile, "%d%d", &R, &C);
		fscanf(ifile, "%c", &temp);
		for(int r = 0; r < R; r++) {
			for(int c = 0; c < C; c++) {
				fscanf(ifile, "%c", &temp);
				table[r][c] = temp;
			}
			fscanf(ifile, "%c", &temp);
		}

		//printInput();

		fprintf(out, "Case #%d: \n", i);
		bool ret = check();
		if(ret == true) {
			printResult(out);
		} else {
			fprintf(out, "Impossible\n");
		}
		i++;
	}
	return 0;
}

