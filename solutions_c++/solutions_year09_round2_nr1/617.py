#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define LMax 105

FILE *fin = fopen("date.in", "rt");
FILE *fout = fopen("date.out", "wt");

int tests, test;

int L, A;
char tree[LMax][LMax], t[LMax * LMax], lent;

int n;
char name[LMax], feature[LMax][LMax];
double cute, w;
char featur[LMax];
int left;

int animal_is(char * featur)
{
	for (int i = 0; i < n; i++)
		if (!strcmp(featur, feature[i]))
			return 1;
	return 0;
}

void go_cute(int poz)
{
	sscanf(t + poz, "(%lf %s", &w, featur);
	cute *= w;

	if (featur[0] == ')') // leaf
		return;
	else
	{
		if (animal_is(featur))
			left = 1; // left
		else
			left = 0; // right

		for (int i = poz + 1; t[i] != '('; i++);
		if (left)
			go_cute(i);
		else
		{
			int nrp = 1;

			for (i = i + 1; nrp; i++)
			{
				if (t[i] == '(')
					nrp++;
				if (t[i] == ')')
					nrp--;
			}

			//nrp == 0
			while (t[i] != '(')
				i++;
			go_cute(i);
		}	
	}
}


int main()
{
	int i, j;
	fscanf(fin, "%d\n", &tests);

	for (test = 1; test <= tests; test++)
	{
		fscanf(fin, "%d\n", &L);

		for (i = 0; i < LMax * LMax; i++)
			t[i] = 0;
		lent = 0;
		for (i = 0; i < L; i++)
		{
			fgets(tree[i], LMax, fin);
			tree[i][strlen(tree[i]) - 1] = 0;
			for (j = 0; j < strlen(tree[i]); j++)
				t[lent++] = tree[i][j];
			
		}

		fscanf(fin, "%d\n", &A);

		fprintf(fout, "Case #%d:\n", test);
		while (A--)
		{

			fscanf(fin, "%s %d ", name, &n);

			for (i = 0; i < n; i++)
				fscanf(fin, "%s", feature[i]);

			cute = 1;
			go_cute(0);
			fprintf(fout, "%.7lf\n", cute);
		}

		i = i;

	}

	fclose(fin);
	fclose(fout);

	return 0;
}
