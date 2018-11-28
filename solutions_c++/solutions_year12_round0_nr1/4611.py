#include<stdio.h>
#include<string.h>

int main()
{
	int T, i, l, j;
	char str[200];
	FILE *fin, *fout;
	fin = fopen("A-small-attempt4.in", "r");
	fout = fopen("out.txt", "w");
	fscanf(fin, "%d\n",&T);
	for (i = 0; i < T; i++)
	{
		//fscanf(fin, "%s\n", &str);
		fgets(str, 200, fin);
		l = strlen(str);
		for (j = 0; j < l; j++)
		{
			if (str[j] == 'a') {str[j] = 'y'; continue;}
			if (str[j] == 'b') {str[j] = 'h'; continue;}
			if (str[j] == 'c') {str[j] = 'e'; continue;}
			if (str[j] == 'd') {str[j] = 's'; continue;}
			if (str[j] == 'e') {str[j] = 'o'; continue;}
			if (str[j] == 'f') {str[j] = 'c'; continue;}
			if (str[j] == 'g') {str[j] = 'v'; continue;}
			if (str[j] == 'h') {str[j] = 'x'; continue;}
			if (str[j] == 'i') {str[j] = 'd'; continue;}
			if (str[j] == 'j') {str[j] = 'u'; continue;}
			if (str[j] == 'k') {str[j] = 'i'; continue;}
			if (str[j] == 'l') {str[j] = 'g'; continue;}
			if (str[j] == 'm') {str[j] = 'l'; continue;}
			if (str[j] == 'n') {str[j] = 'b'; continue;}
			if (str[j] == 'o') {str[j] = 'k'; continue;}
			if (str[j] == 'p') {str[j] = 'r'; continue;}
			if (str[j] == 'q') {str[j] = 'z'; continue;}
			if (str[j] == 'r') {str[j] = 't'; continue;}
			if (str[j] == 's') {str[j] = 'n'; continue;}
			if (str[j] == 't') {str[j] = 'w'; continue;}
			if (str[j] == 'u') {str[j] = 'j'; continue;}
			if (str[j] == 'v') {str[j] = 'p'; continue;}
			if (str[j] == 'w') {str[j] = 'f'; continue;}
			if (str[j] == 'x') {str[j] = 'm'; continue;}
			if (str[j] == 'y') {str[j] = 'a'; continue;}
			if (str[j] == 'z') {str[j] = 'q'; continue;}
		}
		fprintf(fout, "Case #%d: %s", i + 1, str);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}