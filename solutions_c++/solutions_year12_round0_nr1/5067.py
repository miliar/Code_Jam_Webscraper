/*
ID: brook.t1
PROG: speak
LANG: C++
*/

#define forzo(lim) for(int i = 0; i < lim; i++)

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;

char trans(char c)
{
	if(c == 'a') return 'y';
	if(c == 'b') return 'h';
	if(c == 'c') return 'e';
	if(c == 'd') return 's';
	if(c == 'e') return 'o';
	if(c == 'f') return 'c';
	if(c == 'g') return 'v';
	if(c == 'h') return 'x';
	if(c == 'i') return 'd';
	if(c == 'j') return 'u';
	if(c == 'k') return 'i';
	if(c == 'l') return 'g';
	if(c == 'm') return 'l';
	if(c == 'n') return 'b';
	if(c == 'o') return 'k';
	if(c == 'p') return 'r';
	if(c == 'q') return 'z';
	if(c == 'r') return 't';
	if(c == 's') return 'n';
	if(c == 't') return 'w';
	if(c == 'u') return 'j';
	if(c == 'v') return 'p';
	if(c == 'w') return 'f';
	if(c == 'x') return 'm';
	if(c == 'y') return 'a';
	if(c == 'z') return 'q';
	return c;
}

int main()
{
	FILE * input = fopen("speak.in", "r");
	FILE * output = fopen("speak.out", "w+");

	int n, cnew = 1;
	char temp;
	fscanf(input, " %d ", &n);
	fprintf(output, "CASE #1: ");
	while(cnew <= n)
	{
		fscanf(input, "%c", &temp);
		if(temp == '\n')
		{
			cnew++;
			if(cnew <= n) fprintf(output, "\nCASE #%d: ", cnew);
			continue;
		}
		fprintf(output, "%c", trans(temp));
	}

	fclose(input);
	fclose(output);
	return 0;
}
