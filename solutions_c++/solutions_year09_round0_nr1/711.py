#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <conio.h>
int l, d, n;
FILE *f, *g;

char dict[5002][15];
int nr_test;

int aux[16][40];
void rezolva() {

	int i, j;
	for (i=0; i<l; i++) {
		for (j='a'; j<='z'; j++) {
			aux[i][j-'a'] = 0;
		}
	}

	char buf[512];

	fgets(buf, 512, f);
	int lg = strlen(buf);
	buf[lg-1] = 0;

	int poz = 0;
	int paranteza = 0;
	for (i=0; i<lg; i++) {
		char ch = buf[i];
		if (ch == '(') {
			paranteza = 1;
		} else

		if ((ch >= 'a') && (ch <= 'z')) {
			aux[poz][ch-'a'] = 1;

			if (paranteza == 0) poz++;

		} else

		if (ch == ')') {
			poz++;
			paranteza = 0;
		}
	}

    if (poz != 15) {
       getch();
    }
	int nr_cuv = 0;
	// calculez numarul de aparitii
	for (i=0; i<d; i++) {
		char* cuv = dict[i];
		int ok = 1;

		for (j=0; j<l; j++) {

			char ch = cuv[j];
			if (aux[j][ch-'a']==0) {
				ok = 0;
				break;
			}

		}

		if (ok==1) {
			nr_cuv++;
		}
	}

	fprintf(g, "Case #%i: %i\n", nr_test, nr_cuv);
}

int main() {


	f=fopen("a.in", "rt");
	g=fopen("a.out", "wt");


	fscanf(f, "%i%i%i", &l, &d, &n);

	int i;

	// citesc dictionarul
	char s[16];
	for (i=0; i<d; i++) {
		fscanf(f, "%s", s);
		strcpy(dict[i], s);
	}

	char buf[512];
	fgets(buf, 512, f);

	for (nr_test=1; nr_test<=n; nr_test++) {
		rezolva();
	}

	fclose(f);
	fclose(g);
}
