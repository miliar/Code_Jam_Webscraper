#include <cstdio>

void get_arguments(char *table, bool *_spaces) {
	char c; bool spaces = false;
	scanf("%c", &c); // character new line between cases
	for (int i = 0, p = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j, ++p) {
			scanf("%c", &table[p]);
			if (!spaces && table[p] == '.') spaces = true;
		}
		scanf("%c", &c); // character new line
	}
	*_spaces = spaces;
}

bool find_line(char *table, char c, int x, int y, int incx, int incy, bool Ts) {
	bool ret = true;
	for (int p = x+incx+(y+incy)*4, i = 0; ret && i < 3; ++i, p += incx + incy*4) {
		if (table[p] != c) {
			if (table[p] == 'T' && Ts) Ts = false;
			else ret = false;
		}
	}
	return ret;
}

int solve_problem(char *table, bool spaces) {
	int ret = 0, draw = spaces ? 0 : 3;
	if (table[0] != '.') {
		if (table[0] == 'T') {
			if (find_line(table, 'X', 0, 0, 1, 0, false) || find_line(table, 'X', 0, 0, 0, 1, false) || find_line(table, 'X', 0, 0, 1, 1, false)) ret = 1;
			else if (find_line(table, 'O', 0, 0, 1, 0, false) || find_line(table, 'O', 0, 0, 0, 1, false) || find_line(table, 'O', 0, 0, 1, 1, false)) ret = 2;
		} else {
			if (table[0] == 'X') { if (find_line(table, 'X', 0, 0, 1, 0, true) || find_line(table, 'X', 0, 0, 0, 1, true) || find_line(table, 'X', 0, 0, 1, 1, true)) ret = 1; }
			else { if (find_line(table, 'O', 0, 0, 1, 0, true) || find_line(table, 'O', 0, 0, 0, 1, true) || find_line(table, 'O', 0, 0, 1, 1, true)) ret = 2;}
		}
	}
	if (table[3] != '.') {
		if (table[3] == 'T') {
			if (find_line(table, 'X', 3, 0, -1, 1, false)) ret = 1;
			else if (find_line(table, 'O', 3, 0, -1, 1, false)) ret = 2;
		} else {
			if (table[3] == 'X') { if (find_line(table, 'X', 3, 0, -1, 1, true)) ret = 1; }
			else { if (find_line(table, 'O', 3, 0, -1, 1, true)) ret = 2;}
		}
	}
	for (int i = 1, j = 4; ret == 0 && i < 4; ++i, j += 4) {
		if (table[i] == 'T') {
			if (find_line(table, 'X', i, 0, 0, 1, false)) ret = 1;
			else if (find_line(table, 'O', i, 0, 0, 1, false)) ret = 2;
		} else {
			if (table[i] == 'X') { if (find_line(table, 'X', i, 0, 0, 1, true)) ret = 1; }
			else { if (find_line(table, 'O', i, 0, 0, 1, true)) ret = 2;}
		}

		if (table[j] == 'T') {
			if (find_line(table, 'X', 0, i, 1, 0, false)) ret = 1;
			else if (find_line(table, 'O', 0, i, 1, 0, false)) ret = 2;
		} else {
			if (table[j] == 'X') { if (find_line(table, 'X', 0, i, 1, 0, true)) ret = 1; }
			else { if (find_line(table, 'O', 0, i, 1, 0, true)) ret = 2;}
		}
	}
	return ret == 0 ? draw : ret;
}

int main(int argc, char *argv[]) {
	int ncases;
	char table[16];
	bool spaces;
	scanf("%d", &ncases);
	for (int i = 0; i < ncases; ++i) {
		get_arguments(table, &spaces);
		printf("Case #%d: ", i+1);
		switch(solve_problem(table, spaces)) {
		case 0:
			printf("Game has not completed\n");
			break;
		case 1:
			printf("X won\n");
			break;
		case 2:
			printf("O won\n");
			break;
		default:
			printf("Draw\n");
		}
	}
	return 0;
}