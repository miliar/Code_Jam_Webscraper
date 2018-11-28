// snapper.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <malloc.h>
#include <string.h>

typedef struct
{
	int numSnappers;
	long numSnaps;
} xcase;

xcase cases[10000];

#define MAX_SNAPS 100000000L
#define MAX_SNAPPERS 30

int main(int argc, char* argv[])
{
	int state[MAX_SNAPPERS + 1], power[MAX_SNAPPERS + 1];
	long numSnaps;
	int numCases;
	int numSnappers;
	long i, iSnaps, iSnapper;
	FILE *fp;
	char *flags[MAX_SNAPPERS];

	long size = sizeof(char) * (MAX_SNAPS / 8 + 1);
	for (i = 0; i < MAX_SNAPPERS; i++)
	{
		flags[i] = (char *)malloc(size);
		if (flags[i] == NULL)
		{
			printf("No mem\n");
			return 0;
		}
		memset(flags[i], 0, size);
	}
		
	fp = fopen("A-large.in", "r");
	fscanf(fp, "%d\n", &numCases);

	for (i = 0; i < numCases; i++)
	{
		fscanf(fp, "%d %ld\n", &numSnappers, &numSnaps);
		cases[i].numSnappers = numSnappers;
		cases[i].numSnaps = numSnaps;
	}

	for (iSnapper = 1; iSnapper <= MAX_SNAPPERS; iSnapper++)
	{
		state[iSnapper] =  0;
		power[iSnapper] =  0;
	}

	int pwr;

	power[1] = 1;

	for (iSnaps = 1; iSnaps <= MAX_SNAPS; iSnaps++)
	{
		for (iSnapper = 1; iSnapper <= MAX_SNAPPERS; iSnapper++)
		{
			if (iSnapper == 1)
			{
				state[iSnapper] = !state[iSnapper];
			}
			else
			{
				if (power[iSnapper])
					state[iSnapper] = !state[iSnapper];
				power[iSnapper] = power[iSnapper - 1] && state[iSnapper - 1];
			}

			if (power[iSnapper] && state[iSnapper])
				flags[iSnapper - 1][iSnaps / 8] = flags[iSnapper - 1][iSnaps / 8] | (1 << (7 - iSnaps % 8));
		}
	}

	int res;
	int iSnap;
	for (i = 0; i < numCases; i++)
	{
		printf("Case #%d: ", i + 1);
		if (cases[i].numSnaps == 0)
			res = 0;
		else
		{
			iSnap = cases[i].numSnaps;
			res = flags[cases[i].numSnappers - 1][iSnap / 8] & (1 << (7 - iSnap % 8));
		}
		printf("%s\n", res ? "ON" : "OFF");
	}
	
	fclose(fp);

	return 0;
}

