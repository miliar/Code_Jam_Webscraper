#include <fstream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

#define  INPUT "inputA"
#define  OUTPUT "_outputA"

ifstream fin;
char buffer[100000];


char *processTest()
{
	int L, C;
	char table[55][55];
	char line[55];
	
	int offset=0;
	*buffer=0;

	fin >> L >> C;

	for (int l=0; l<L; l++)
	{
		fin >> line;
		for (int c=0; c<C; c++)
		{
			table[l][c] = line[c];
		}	
	}	

	for (int l=0; l<L; l++)
	{
		for (int c=0; c<C; c++)
		{
			if ('#' == table[l][c])
			{
				if (l < L && c < C && '#' == table[l][c+1] && '#' == table[l+1][c+1] && '#' == table[l+1][c])
				{
					//cusses
					table[l][c] =    '/';
					table[l][c+1] =   '\\';
					table[l+1][c+1] = '/';
					table[l+1][c] =  '\\';
				}
				else
					return "\nImpossible";
			}
		}	
	}	
	
	for (int l=0; l<L; l++)
	{
		table[l][C] = '\0';
		offset += snprintf(buffer + offset, sizeof(buffer), "\n%s", table[l]);

	}

	return buffer;
}

int main()
{
	FILE *out;
	int T;
	char *result;

	printf("\tRead "OUTPUT"...\n");
	fin.open(INPUT);
	out = fopen(OUTPUT, "w+");

	fin >> T;

	for (int t=1; t <= T; t++)
	{
		result = processTest();
		fprintf(out, "Case #%d:%s", t, result);
		fprintf(out, "\n", t);
//printf("\t%s\n", result);
	}

	fclose(out);
	fin.close();
	printf("\n\n");
	return 0;
}
