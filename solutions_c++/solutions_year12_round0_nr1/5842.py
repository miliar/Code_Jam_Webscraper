#include <stdio.h>
//#include <stdlib.h>

char pretvori(char ulazni) {
	char izlazni;
	switch (ulazni) {
		case ('a'): return 'y';
		case ('b'): return 'h';
		case ('c'): return 'e';
		case ('d'): return 's';
		case ('e'): return 'o';
		case ('f'): return 'c';
		case ('g'): return 'v';
		case ('h'): return 'x';
		case ('i'): return 'd';
		case ('j'): return 'u';
		case ('k'): return 'i';
		case ('l'): return 'g';
		case ('m'): return 'l';
		case ('n'): return 'b';
		case ('o'): return 'k';
		case ('p'): return 'r';
		case ('q'): return 'z';
		case ('r'): return 't';
		case ('s'): return 'n';
		case ('t'): return 'w';
		case ('u'): return 'j';
		case ('v'): return 'p';
		case ('w'): return 'f';
		case ('x'): return 'm';
		case ('y'): return 'a';
		case ('z'): return 'q';
		case (' '): return ' ';
		case ('\n'): return '\n';
		default: break;
	}
	return '0';
}


int main(void)
{
	int brojZadataka = 0, i, j;
	char ulaz[128];
	FILE *in, *out;

	in = fopen("A-small-0.in", "r");
	if (in == NULL) {
		printf("Greska prilikom otvaranja ulazne datoteke!\n");
		return 1;
	}

	out = fopen("A-small-0.out", "w");
	if (out == NULL) {
		printf("Greska prilikom otvaranja izlazne datoteke!\n");
		return 1;
	}

	fscanf(in, "%d\n", &brojZadataka);

	for (i = 1; i <= brojZadataka; i++) {
		if (fgets(ulaz, sizeof(ulaz), in) == NULL); // onda je greska
		fprintf(out, "%s%i: ", "Case #", i);
		for (j = 0; ulaz[j] != 0; j++) {
			fprintf(out, "%c", pretvori(ulaz[j]));
		}
		//fprintf(out, "\r\n");
	}

	/*
	for (i = 1; i <= brojZadataka; i++) {
		fscanf(in, "%s", ulaz);
		fprintf(out, "%s%i: ", "Case #", i);
		for (j = 0; ulaz[j] != 0; j++) {
			fprintf(out, "%c", pretvori(ulaz[j]));
		}
	}*/

	fclose(in);
	fclose(out);

	return 0;
}
