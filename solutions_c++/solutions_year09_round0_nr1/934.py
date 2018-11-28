#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <ctype.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
//#include <set>
//#include <map>

using namespace std;

int l = 0, n = 0, d = 0;

int pats [500][15] = {0};
int words [5000][15] = {0};
int ans [500] = {0};

char s1 [30*15] = {0};

int main ()
{
	FILE* fin, *fout;
	fin = stdin;
	fout = stdout;

	fscanf (fin, "%d%d%d", &l, &d, &n);

	int i = 0, j = 0, k = 0, pos = 0;
	for (i = 0; i < d; i ++)
	{
		fscanf (fin, "%s", s1);
		for (j = 0; j < l; j ++)
		{
			words [i][j] = s1 [j] - 'a';
			words [i][j] = 1 << words [i][j];
		}
	}

	for (i = 0; i < n; i ++)
	{
		fscanf (fin, "%s", s1);
		pos = 0;
		k = strlen (s1);
		for (j = 0; j < k; j ++, pos ++)
		{
			if (s1 [j] != '(' && s1 [j] != ')')
			{
				pats [i][pos] = 1 << (s1 [j] - 'a');
			}
			else
			{
				for (j ++; s1 [j] != ')'; j ++)
				{
					pats [i][pos] |= (1 << (s1 [j] - 'a'));
				}
			}
		}
	}

	for (i = 0; i < n; i ++)
	{
		for (j = 0; j < d; j ++)
		{
			for (k = 0; k < l; k ++)
			{
				if ((pats [i][k] & words [j][k]) == 0)
					break;
			}
			if (k >= l)
				ans [i] ++;
		}
	}

	for (i = 0; i < n; i ++)
	{
		fprintf (fout, "Case #%d: %d\n", i + 1, ans [i]);
	}

	fclose (fin);
	fclose (fout);
	return 0;
}
