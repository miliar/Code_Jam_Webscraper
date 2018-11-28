// snapper.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <malloc.h>
#include <string.h>

#define MAXN 100


 long x[1000];
long y[1000];
int flags[1000];

int main(int argc, char* argv[])
{
	int numCases;
	int i, j, k;
	int points;
	FILE *fp;
	 long xd, yd;
	int cnt;

	fp = fopen("A-small.in", "r");
	fscanf(fp, "%d\n", &numCases);

	for (i = 0; i < numCases; i++)
	{
		fscanf(fp, "%d\n", &points);
		for (j = 0; j < points; j++)
		{
			fscanf(fp, "%ld %ld\n", &x[j], &y[j]);
			//flags[j] = 0;
		}
		cnt = 0;
		int intr;
		for (j = 0; j < points - 1; j++)
		{
			for (k = j + 1; k < points; k++)
			{
				xd = x[j] - x[k];
				yd = y[j] - y[k];

				intr = 0;
				if (xd < 0)
				{
					if (yd > 0)
						intr = 1;
				}
				if (xd > 0)
				{
					if (yd < 0)
						intr  = 1;
				}
				if (intr)
					cnt++;
			}
		}

		printf("Case #%d: %d\n", i + 1, cnt);
	}

	
	fclose(fp);

	return 0;
}

