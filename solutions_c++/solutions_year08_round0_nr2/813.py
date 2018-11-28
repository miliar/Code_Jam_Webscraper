#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

struct voyage
{
	int minStart;
	int minEnd;
	int type; /* 0 - for A, 1 - for B */
	int noNew;
} dep[201];

int mCmp( const void *arg1, const void *arg2 )
{
	if (((struct voyage *) arg1)->minStart > ((struct voyage *) arg2)->minStart)
		return 1;
	else if (((struct voyage *) arg1)->minStart < ((struct voyage *) arg2)->minStart)
		return -1;
	else if (((struct voyage *) arg1)->minEnd > ((struct voyage *) arg2)->minEnd)
		return 1;
	else if (((struct voyage *) arg1)->minEnd < ((struct voyage *) arg2)->minEnd)
		return -1;
	return 0;
}

void runAnal(FILE* out, int city, int t)
{
	int i, j;
	int NA = 0, NB = 0;
	int cTime;

	for (i = 0; i < t; i++)
	{
		cTime = dep[i].minEnd;
		for (j = i+1; j < t; j++)
		{
			if (dep[j].minStart >= cTime && dep[j].type != dep[i].type && dep[j].noNew == 0)
			{
				dep[j].noNew = 1;
				break;
			}
		}
	}

	for (i = 0; i < t; i++)
	{
		if (dep[i].noNew == 0)
		{
			if (dep[i].type == 0)
				NA++;
			else
				NB++;
		}
	}

	fprintf(out, "Case #%d: %d %d\n", city+1, NA, NB);

}

int main ()
{
	int N, NA, NB, T;
	int i, j, t;
	int h1, h2, m1, m2;
	FILE *in, *out;
	
	in = fopen("input.txt", "rt");
	out = fopen("output.txt", "wt");

	fscanf(in, "%d", &N);
	for (i = 0; i < N; i++)
	{
		t = 0;
		fscanf(in, "%d %d %d", &T, &NA, &NB);
		for (j = 0; j < NA; j++)
		{
			fscanf(in, "%d:%d %d:%d", &h1, &m1, &h2, &m2);
			dep[t].minStart = h1*60 + m1;
			dep[t].minEnd = h2*60 + m2 + T;
			dep[t].type = 0;
			dep[t].noNew = 0;
			t++;
		}
		for (j = 0; j < NB; j++)
		{
			fscanf(in, "%d:%d %d:%d", &h1, &m1, &h2, &m2);
			dep[t].minStart = h1*60 + m1;
			dep[t].minEnd = h2*60 + m2 + T;
			dep[t].type = 1;
			dep[t].noNew = 0;
			t++;
		}
		qsort(dep, t, sizeof(struct voyage), mCmp);
		
		runAnal(out, i, t);
	}

	fclose(in);
	fclose(out);

	return 0;
}

