#include <stdio.h>

char ma[6][6];
bool check = 0, aa = 0;

FILE *in = fopen("A-small-attempt2.in", "r");
FILE *out = fopen("A-small-attempt2.out", "w");

void print(int x, int o, int i){

	if (x == 4) {

		fprintf(out, "Case #%d: X won\n", i);
		check = 1;
		return;

	}
	if (o == 4) {

		fprintf(out, "Case #%d: O won\n", i);
		check = 1;
		return;

	}

}
int main(){

	int T, i;
	fscanf(in, "%d", &T);

	for (i = 1; i <= T; i++){

		int j, k;
		int x = 0, o = 0;

		char a;
		fscanf(in, "%c", &a);
		for (j = 1; j <= 4; j++){

			for (k = 1; k <= 4; k++){

				fscanf(in, "%c", &ma[j][k]);

			}
			if (i != T || j != 4) fscanf(in, "%c", &a);

		}

		for (j = 1; j <= 4; j++){

			//가로
			x = 0; o = 0;
			check = 0, aa = 0;
			for (k = 1; k <= 4; k++){

				if (ma[j][k] == '.') {aa = 1; break;}
				else if (ma[j][k] == 'X') x += 1;
				else if (ma[j][k] == 'O') o += 1;
				else {

					x += 1; o += 1;

				}

			}
			print(x, o, i);
			if (check == 1) break;
			//세로
			x = 0, o = 0;
			for (k = 1; k <= 4; k++){

				if (ma[k][j] == '.') {aa = 1; break;}
				else if (ma[k][j] == 'X') x += 1;
				else if (ma[k][j] == 'O') o += 1;
				else {

					x += 1; o += 1;

				}

			}
			print(x, o, i);
			if (check == 1) break;

		}
		if (!check){

			x = 0, o = 0;
			for (j = 1; j <= 4; j++){

				if (ma[j][j] == '.') {aa = 1; break;}
				else if (ma[j][j] == 'X') x += 1;
				else if (ma[j][j] == 'O') o += 1;
				else {

					x += 1; o += 1;

				}

			}
			print(x, o, i);
			if (check == 1) continue;
			
			x = 0, o = 0;
			for (j = 1; j <= 4; j++){

				if (ma[j][4 - j + 1] == '.') {aa = 1; break;}
				else if (ma[j][4 - j + 1] == 'X') x += 1;
				else if (ma[j][4 - j + 1] == 'O') o += 1;
				else {

					x += 1; o += 1;

				}

			}
			print(x, o, i);
			if (check == 1) continue;
			
			
		}else continue;
		if (check == 0 && aa == 0) fprintf(out, "Case #%d: Draw\n", i);
		if (check == 0 && aa == 1) fprintf(out, "Case #%d: Game has not completed\n", i);
	}

}