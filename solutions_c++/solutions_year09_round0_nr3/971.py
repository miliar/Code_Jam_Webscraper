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

int ways [510][20] = {0};

char s [510] = {0};
char s0 [] = "welcome to code jam";
char ans [10] = {0};

int main ()
{
	FILE* fin, *fout;
	fin = stdin;
	fout = stdout;

	int i = 0, n = 0;
	fscanf (fin, "%d\n", &n);
	for (i = 0; i < n; i ++)
	{
		fgets (s, 505, fin);
		memset (ways, 0, sizeof (ways));
		int j = 0, k = 0;
		int l = strlen (s);

		for (j = 0; j <= l; j ++)
		{
			ways [j][0] = 1;
		}
		for (j = 1; j <= l; j ++)
		{
			for (k = 1; k <= 19; k ++)
			{
				if (s [j - 1] == s0 [k - 1])
					ways [j][k] = (ways [j - 1][k - 1] + ways [j - 1][k]) % 10000;
				else
					ways [j][k] = ways [j - 1][k];
			}
		}

		fprintf (fout, "Case #%d: ", i + 1);
		sprintf (ans, "%d", ways [l][19]);
		for (j = 0; j + strlen (ans) < 4; j ++)
			fprintf (fout, "0");
		fprintf (fout, "%d\n", ways [l][19]);
	}

	fclose (fin);
	fclose (fout);
	return 0;
}
