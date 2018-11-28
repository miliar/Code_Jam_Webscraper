#include <stdio.h>

char in[200];
char result[200];
char table[30] = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	FILE *fp = fopen("A-small-attempt0.in", "r");
	FILE *fout = fopen("output.txt", "w");
	int T;

	fscanf(fp, "%d\n", &T);
	for (int i=0; i<T; i++) {
		fgets(in, 200, fp);

		int len=0;
		while (1) {
			if (in[len] == '\0') {
				result[len] = '\0';
				break;
			}

			if (in[len] != ' ')
				result[len] = table[in[len] - 'a'];
			else
				result[len] = ' ';

			len++;
		}

		fprintf(fout, "Case #%d: ", i+1);
		for (int i=0; result[i] != '\0'; i++)
			fprintf(fout, "%c", result[i]);
		fprintf(fout, "\n");
	}

	return 0;
}