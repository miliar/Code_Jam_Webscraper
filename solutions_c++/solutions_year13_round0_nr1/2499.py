#include <stdio.h>
#include <string>
#include <set>
#include <math.h>

#ifndef MAX_STR
#define MAX_STR 4
#endif
#ifndef X_WON
#define X_WON (char*)"X won"
#endif
#ifndef O_WON
#define O_WON (char*)"O won"
#endif
#ifndef DRAW
#define DRAW (char*)"Draw"
#endif
#ifndef NOT_COMP
#define NOT_COMP (char*)"Game has not completed"
#endif

using namespace std;

FILE *in, *out;
char mat[MAX_STR][MAX_STR];
int T;
char* res;

char* state() {
	int x = 0, o = 0, t = 0, comp = 0;
	for (int i = 0; i < 4; ++i) {
		x = 0, o = 0, t = 0;
		for (int j = 0; j < 4; ++j) {
			x += mat[i][j] == 'X';
			o += mat[i][j] == 'O';
			t = mat[i][j] == 'T';
		}
		if (x+t == 4)
			return X_WON;
		if (o+t == 4)
			return O_WON;
		if (x+o+t == 4)
			comp += 1;
	}
	for (int j = 0; j < 4; ++j) {
		x = 0, o = 0, t = 0;
		for (int i = 0; i < 4; ++i) {
			x += mat[i][j] == 'X';
			o += mat[i][j] == 'O';
			t = mat[i][j] == 'T';
		}
		if (x+t == 4)
			return X_WON;
		if (o+t == 4)
			return O_WON;
	}
	x = 0, o = 0, t = 0;
	for (int i = 0, j = 0; i < 4; ++i, ++j) {
		x += mat[i][j] == 'X';
		o += mat[i][j] == 'O';
		t = mat[i][j] == 'T';
		if (x+t == 4)
			return X_WON;
		if (o+t == 4)
			return O_WON;
	}
	x = 0, o = 0, t = 0;
	for (int i = 0, j = 3; i < 4; ++i, --j) {
		x += mat[i][j] == 'X';
		o += mat[i][j] == 'O';
		t = mat[i][j] == 'T';
		if (x+t == 4)
			return X_WON;
		if (o+t == 4)
			return O_WON;
	}
	if (comp == 4)
		return DRAW;
	return NOT_COMP;
}

int main() {
	in = fopen("A-small-attempt0.in", "r");
	out = fopen("A.out", "w");
	
	fscanf(in, "%d ", &T);
	
	for(int t = 1; t <= T; ++t)
	{
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				fscanf(in, "%c ", &mat[i][j]);
		res = state();
		fprintf(out, "Case #%d: %s\n", t, res);
	}
	
	return 0;
}
