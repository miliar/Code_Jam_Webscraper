#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

char state[2][4] = {"OFF", "ON"};

int Toggle(int n, long k)
{
	long mask;

	mask = pow(2,n) -1;
	k %= (mask+1);

	if(k == mask)
		return 1;

	else
		return 0;
}


void main()
{
	int numOfTestCase=0;
	int numOfSnappers=0;
	long numOfSnaps=0;
	int j=0;

	FILE *fp, *out;


	fp = fopen("A-large.in", "rt");
	out = fopen("output2.txt", "wt");

	fscanf(fp, "%d", &numOfTestCase);

	for(j=0; j<numOfTestCase; j++)
	{
		fscanf(fp, "%d %ld", &numOfSnappers, &numOfSnaps);

		fprintf(out,"Case #%d: %s\n", j+1, state[Toggle(numOfSnappers, numOfSnaps)]);
	}


	fclose(fp);
	fclose(out);
	getch();

}
