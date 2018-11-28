#include <fstream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

#define  INPUT "inputA"
#define  OUTPUT "outputA"

ifstream fin;
char buffer[100000];

float WP[100], OWP[100], OOWP[100];
int table[100][100];
int games[100];

char *processTest()
{
	int N;
	
	int offset=0;
	*buffer=0;

	fin >> N;

	int won;
	char line[200], g;
	for (int t=0; t<N; t++)
	{
		fin >> line;
		won = 0;
		games[t]=0;
		for (int o=0; o<N; o++)
		{
			g = line[o];
			if ('.' == g)
			{
				table[t][o]=-1;
			} else {
				games[t]++;
				if ('1' == g)
				{
					table[t][o]=1;
					won++;
				} else { //'0'
					table[t][o]=0;
				}
			}
		}
		WP[t] = (float)won / (float)games[t];
	}

	//CALC OWP
	float total;
	int count;
	for (int t=0; t<N; t++)
	{
		total = 0;
		count = 0;
		for (int o=0; o<N; o++)
		{
			if (-1 != table[t][o])
			{
				count++;
				total += ((WP[o] * games[o]) - table[o][t]) / (games[o] - 1);
			}
		}
		OWP[t] = total / (float)count;
	}

	//CALC OOWP
	float RPI;
	for (int t=0; t<N; t++)
	{
		total = 0;
		count = 0;
		for (int o=0; o<N; o++)
		{
			if (-1 != table[t][o])
			{
				count++;
				total += OWP[o];
			}
		}
		OOWP[t] = (total / (float)count);
		RPI = 0.25 * WP[t] + 0.50 * OWP[t] + 0.25 * OOWP[t];
		offset += snprintf(buffer + offset, sizeof(buffer) - offset, "\n%f", RPI);
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
