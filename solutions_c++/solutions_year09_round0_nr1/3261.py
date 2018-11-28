#include <cstdio>
#include <iostream>
using namespace std;

const int MaxL = 16;
const int MaxD = 5001;

int L, D, n;

bool postoji[MaxL][26];
char dict[MaxD][MaxL];
char alien[MaxL * 26 * 2];

int main()
{
	FILE *fin = fopen("a_small.in", "r");
	FILE *fout = fopen("a-small.out", "w");

	fscanf(fin, "%ld %ld %ld\n", &L, &D, &n);

	for (int i = 0; i < D; i++)
		fgets(dict[i], sizeof(dict[i]), fin);

	for (int i = 1; i <= n; i++)
	{
		memset(postoji, 0, sizeof(postoji));
		fgets(alien, sizeof(alien), fin);

		bool inside = false;
		int ind = -1;
		for (int j = 0; j < strlen(alien); j++)
		{
			if (alien[j] == '(')
			{
				ind++;
				inside = true;
			}
			else if (alien[j] == ')')
				inside = false;
			else
			{
				if (!inside)
					ind++;

				postoji[ind][alien[j] - 'a'] = true;
			}
		}

		int res = 0;
		for (int j = 0; j < D; j++)
		{
			bool add = true;
			for (int c = 0; c < L; c++)
			{
				if (!postoji[c][dict[j][c] - 'a'])
				{
					add = false;
					break;
				}
			}

			if (add)
				res++;
		}

		fprintf(fout, "Case #%d: %d\n", i, res);
	}

	fclose(fin);
	fclose(fout);
}
