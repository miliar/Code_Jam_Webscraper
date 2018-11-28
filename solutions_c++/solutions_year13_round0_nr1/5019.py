#include <stdio.h>

int main () {
	char c[10][10];
	int t, a, b;
	scanf ("%d", &t);
	for (int k = 0; k < t; k++) {
		a = b = 0;
		int draw = 1;
		for (int i = 0; i < 4; i++) 
			for (int j = 0; j < 4; j++) {
				scanf (" %c", &c[i][j]);
				if (c[i][j] == '.')
					draw = 0;
			}


		int fav, fah, fbh, fbv;
		for (int i = 0; i < 4; i++) {
			fav = fah = fbh = fbv = 1;
			for (int j = 0; j < 4; j++) {
				fav *= (c[i][j] == 'X' || c[i][j] == 'T');
				fah *= (c[j][i] == 'X' || c[j][i] == 'T');
				fbv *= (c[i][j] == 'O' || c[i][j] == 'T');
				fbh *= (c[j][i] == 'O' || c[j][i] == 'T');
			}
			if (fav == 1 || fah == 1)
				a = 1;
			if (fbv == 1 || fbh == 1)
				b = 1;
		}
		int fa = 1, fb = 1;
		for (int i = 0; i < 4; i++) {
			fa *= (c[i][i] == 'X' || c[i][i] == 'T');
			fb *= (c[i][i] == 'O' || c[i][i] == 'T');
		}
		if (fa == 1)
			a = 1;
		if (fb == 1)
			b = 1;
		fa = fb = 1;
		for (int i = 0; i < 4; i++) {
			fa *= (c[3 - i][i] == 'X' || c[3 - i][i] == 'T');
			fb *= (c[3 - i][i] == 'O' || c[3 - i][i] == 'T');
		}
		if (fa == 1)
			a = 1;
		if (fb == 1)
			b = 1;

		printf ("Case #%d: ", k + 1);
		if (a == 1)
			printf ("X won\n");
		else if (b == 1)
			printf ("O won\n");
		else if (draw == 1)
			printf ("Draw\n");
		else 
			printf ("Game has not completed\n");
	}
	return 0;
}
