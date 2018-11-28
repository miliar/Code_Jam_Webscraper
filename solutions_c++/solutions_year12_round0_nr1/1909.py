#include <iostream>
using namespace std;

int main(int argc, char *argv[]) {
	FILE *fp;
	if((fp=fopen(argv[1],"r"))==NULL) {
		printf("Cannot open file.\n");
		exit(1);
	}

	char Eng[26];
	Eng['a'-'a'] = 'y';
	Eng['b'-'a'] = 'h';
	Eng['c'-'a'] = 'e';
	Eng['d'-'a'] = 's';
	Eng['e'-'a'] = 'o';
	Eng['f'-'a'] = 'c';
	Eng['g'-'a'] = 'v';
	Eng['h'-'a'] = 'x';
	Eng['i'-'a'] = 'd';
	Eng['j'-'a'] = 'u';
	Eng['k'-'a'] = 'i';
	Eng['l'-'a'] = 'g';
	Eng['m'-'a'] = 'l';
	Eng['n'-'a'] = 'b';
	Eng['o'-'a'] = 'k';
	Eng['p'-'a'] = 'r';
	Eng['q'-'a'] = 'z';
	Eng['r'-'a'] = 't';
	Eng['s'-'a'] = 'n';
	Eng['t'-'a'] = 'w';
	Eng['u'-'a'] = 'j';
	Eng['v'-'a'] = 'p';
	Eng['w'-'a'] = 'f';
	Eng['x'-'a'] = 'm';
	Eng['y'-'a'] = 'a';
	Eng['z'-'a'] = 'q';

	int T, i, j;
	char Buf[128];

	fscanf_s(fp, "%d%*c", &T);
	for (i = 1; i <= T; i++) {
		printf ("Case #%d: ", i);

		fscanf(fp, "%[a-z ]s", Buf);
		for (j = 0; j < strlen(Buf); j++)
			if (Buf[j] == ' ')
				printf (" ");
			else
				printf ("%c", Eng[Buf[j]-'a']);

		printf ("\n");
		fscanf_s(fp, "%*c");
	}
	fclose(fp);
	return 0;
}