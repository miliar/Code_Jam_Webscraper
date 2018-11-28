#include <cstring>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>

const char *str = "yhesocvxduiglbkrztnwjpfmaq";


int main() {
	FILE *fin = fopen("A-small-attempt0.in", "r");
	FILE *fout = fopen("out.txt", "w");
	int t;
	fscanf(fin, "%d", &t);
	char ch;
	while (isspace(ch = fgetc(fin)));
	for (int i = 1; i <= t; ++i) {
		fprintf(fout, "Case #%d: ", i);
		do {
			if (ch >= 'a' && ch <= 'z') ch = str[ch - 'a'];
			fprintf(fout, "%c", ch);
			ch = fgetc(fin);
		} while (ch != '\n' && ch != EOF);
		fprintf(fout, "\n");
		while (isspace(ch = fgetc(fin)));
	}
	fclose(fout);
	fclose(fin);
	return 0;
}
