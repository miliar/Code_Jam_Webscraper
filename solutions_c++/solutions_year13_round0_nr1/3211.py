#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

#define min(a, b) ((a)<(b)?(a):(b))
#define max(a, b) ((a)<(b)?(a):(b))

using namespace std;

unsigned int tesztDB;
char palya[4][4];

unsigned int felDB(char kar, int x, int y) {
	if (y < 0) return 0;
	if (palya[x][y] == kar || palya[x][y] == 'T') return 1+felDB(kar, x, y-1);
	return 0;
}

unsigned int balDB(char kar, int x, int y) {
	if (x < 0) return 0;
	if (palya[x][y] == kar || palya[x][y] == 'T') return 1+balDB(kar, x-1, y);
	return 0;
}

unsigned int felBalDB(char kar, int x, int y) {
	if (x < 0 || y < 0) return 0;
	if (palya[x][y] == kar || palya[x][y] == 'T') return 1+felBalDB(kar, x-1, y-1);
	return 0;
}

unsigned int felJobbDB(char kar, int x, int y) {
	if (x >= 4 || y < 0) return 0;
	if (palya[x][y] == kar || palya[x][y] == 'T') return 1+felJobbDB(kar, x+1, y-1);
	return 0;
}

string valasz(bool betelt, bool oNyert, bool xNyert) {
	if (oNyert) return "O won";
	if (xNyert) return "X won";
	if (betelt) return "Draw";
	return "Game has not completed";
}

int main(int argc, char **argv) {
	unsigned int i, j, k;
	bool betelt, xNyert, oNyert;
	string tar;
	ifstream ifile("A-large.in");
	FILE *ofile = fopen("out.txt", "w");
	ifile >> tesztDB;
	for (i = 0; i < tesztDB; i++) {
		betelt = true;
		getline(ifile, tar);
		for (j = 0; j < 4; j++) {
			getline(ifile, tar);
			for (k = 0; k < 4; k++) {
				palya[j][k] = tar[k];
				if (tar[k] == '.') betelt = false;
			}
		}
		/*for (j = 0; j < 4; j++) {
			for (k = 0; k < 4; k++) {
				printf("%c", palya[j][k]);
			}printf("\n");
		}printf("-------\n");*/
		xNyert = false;
		oNyert = false;
		for (j = 0; j < 4; j++) {
			for (k = 0; k < 4; k++) {
				if (felDB('O', j, k) == 4) oNyert = true;
				if (balDB('O', j, k) == 4) oNyert = true;
				if (felBalDB('O', j, k) == 4) oNyert = true;
				if (felJobbDB('O', j, k) == 4) oNyert = true;
				if (felDB('X', j, k) == 4) xNyert = true;
				if (balDB('X', j, k) == 4) xNyert = true;
				if (felBalDB('X', j, k) == 4) xNyert = true;
				if (felJobbDB('X', j, k) == 4) xNyert = true;
			}
		}
		fprintf(ofile, "Case #%i: %s\n", i+1, valasz(betelt, oNyert, xNyert).c_str());
	}
	ifile.close();
	fclose(ofile);
	return 0;
}
