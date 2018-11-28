#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define LMax 50

FILE *fin = fopen("date.in", "rt");
FILE *fout = fopen("date.out", "wt");

int tests, test, len;

char N[LMax];
char nou[LMax];
char min[LMax];

void copy(char *to, char *from)
{
	for (int i = 0; i < LMax; i++)
		to[i] = from[i];	
}

int greater(char *a, char *b)
{
	if (strlen(a) > strlen(b))
		return 1;
	if (strlen(a) < strlen(b))
		return 0;
	for (int i = 0; i < strlen(a); i++)
	{
		if (a[i] > b[i])
			return 1;
		if (a[i] < b[i])
			return 0;
	}
	return 0;
}

void new_zero(char *nou, int p0)
{
	int i;
	for (i = 0; i <= LMax; i++)
		nou[i] = 0;

	for (i = 0; i <= p0; i++)
		nou[i] = N[i];
	nou[i] = '0';
	for (i = p0 + 1; i < len; i++)
		nou[i + 1] = N[i];
}

void new_switch(char *nou, int p0, int p1)
{
	for (int i = 0; i < LMax; i++)
		nou[i] = N[i];
	
	nou[p0] = N[p1];
	nou[p1] = N[p0];
}

int cmpCh(const void *a, const void *b)
{
	return (*(char*)a) - (*(char*)b);
}


int ap[10];
int same(int nn, int ii)
{
	int i;
	for (i = 1; i <= 9; i++)
		ap[i] = 0;

	while (nn)
	{
		ap[nn%10] ++;
		nn /= 10;
	}
	while (ii)
	{
		ap[ii%10] --;
		ii /= 10;
	}
	for (i = 1; i <= 9; i++)
	{
		if (ap[i] != 0)
			return 0;
	}
	return 1;
}

int main()
{
	int i, j;
	fscanf(fin, "%d", &tests);

	for (test = 1; test <= tests; test++)
	{
		fscanf(fin, "%s", N);
		len = strlen(N);

		if (len == 1)
		{
			fprintf(fout, "Case #%d: %s0\n", test, N);
			continue;
		}

		// add one zero

		for (i = 0; i < LMax; i++)
			nou[i] = min[i] = 0;

		new_zero(nou, 0);
		int pmin = -1;

		for (i = 2; i <= len; i++)
		{
			if (nou[i] != '0' && 
			   (pmin == -1 || nou[i] < nou[pmin]))
			{
				pmin = i;
			}
		}
		if (pmin != -1) {
			char aux = nou[0];
			nou[0] = nou[pmin];
			nou[pmin] = aux;
		}


		qsort(nou + 1 + 1, len - 1, sizeof(nou[0]), cmpCh);
			if (greater(nou, N))
			{
				if (min[0] == 0 || greater(min, nou))
				{
					copy(min, nou);
				}
			}

		/*
		for (i = 0; i < len - 1; i++)
		{
			new_zero(nou, i);
			if (greater(nou, N))
			{
				if (min[0] == 0 || greater(min, nou))
				{
					copy(min, nou);
				}
			}
		}*/

		for (i = 0; i < len; i++) //poz unde cresc
		{
			for (j = 0; j < LMax; j++)
				nou[j] = N[j];

			int pmin = -1;
			for (j = i + 1; j < len; j++)
			{
				if (nou[j] > nou[i])
				{
					if (pmin == -1 || nou[j] < nou[pmin])
						pmin = j;
				}
			}
			if (pmin != -1)
			{
				nou[pmin] = N[i];
				nou[i] = N[pmin];
				qsort(nou + i + 1, len - i - 1, sizeof(nou[0]), cmpCh);
				


				if (greater(nou, N))
				{
					if (min[0] == 0 || greater(min, nou))
					{
						copy(min, nou);
					}
				}
			}
		}

		fprintf(fout, "Case #%d: %s\n", test, min);
	}

	fclose(fin);
	fclose(fout);


	/*
	fin = fopen("date.in", "rt");
	FILE *fout2 = fopen("date2.out", "wt");

	fscanf(fin, "%d", &tests);
	int nn, ii;

	for (test = 1; test <= tests; test++)
	{
		printf("test %d\n", test);
		fscanf(fin, "%d", &nn);

		for (ii = nn + 1; !same(nn, ii); ii++);

		fprintf(fout2, "Case #%d: %d\n", test, ii);
	}
	fclose(fout2);

	

	*/
	

	return 0;
}
