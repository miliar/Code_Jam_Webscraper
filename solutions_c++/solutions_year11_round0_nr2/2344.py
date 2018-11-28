#include <stdlib.h>
#include <stdio.h>
#include <fstream>
#include <string>

using namespace std;

char base[8] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
int  nbase = 8;
char combine[8][8];
bool oposed[8][8];

char x[101];
int  n;

char sol[400];


int getBaseIndex(char c)
{
	for (int i = 0; i < nbase; i++)
	{
		if (base[i] == c)
			return i;
	}

	return -1;
}

void init()
{
	sol[0] = '\0';

	for (int i = 0; i < nbase; i++)
		for (int j = 0; j < nbase; j++)
		{
			combine[i][j] = 0;
			oposed[i][j] = false;
		}
}


void solve()
{
	char y[400];
	int  ny = 0;
	int  inList[8];

	for (int i = 0 ; i < nbase; i++)
		inList[i] = 0;

	y[ny++] = x[0];
	inList[getBaseIndex(x[0])]++;

	for (int i = 1; i < n; i++)
	{
		y[ny++] = x[i];

		if (ny == 1) 
		{
			inList[getBaseIndex(x[i])]++;
			continue;
		}

		int idx1 = getBaseIndex(y[ny-1]);
		int idx2 = getBaseIndex(y[ny-2]);

		if ( (idx1 != -1) && (idx2 != -1) && (combine[idx1][idx2] != 0) )
		{
			ny--;
			y[ny-1] = combine[idx1][idx2];

			if (inList[idx2] > 0)
			{
				inList[idx2]--;
			}

			continue;
		}

		bool op = false;
		for (int j = 0; j < nbase; j++)
		{
			if (inList[j] == 0) continue;

			if (oposed[j][idx1])
			{
				ny = 0;

				for (int k = 0; k < nbase; k++)
				{
					inList[k] = 0;
				}

				op = true;
				break;
			}
		}

		if (op) continue;

		inList[idx1]++;
	}

	sol[0] = '[';
	int nsol = 1;

	for (int i = 0; i < ny; i++)
	{
		sol[nsol++] = y[i];

		if (i != ny-1)
		{
			sol[nsol++] = ',';
			sol[nsol++] = ' ';
		}
	}

	sol[nsol++] = ']';
	sol[nsol++] = '\0';
}


int main()
{
	fstream			f, g;
	int				tests;
	int             comp, opos;
	string          s;

	f.open("in.txt", ios :: in);
	g.open("out.txt", ios :: out);

	f >> tests;

	for (int k = 1; k <= tests; k++)
	{
		init();

		f >> comp;
		for (int i = 0; i < comp; i++)
		{
			f >> s;
			combine[getBaseIndex(s[0])][getBaseIndex(s[1])] = combine[getBaseIndex(s[1])][getBaseIndex(s[0])] = s[2];
		}

		f >> opos;
		for (int i = 0; i < opos; i++)
		{
			f >> s;
			oposed[getBaseIndex(s[0])][getBaseIndex(s[1])] = oposed[getBaseIndex(s[1])][getBaseIndex(s[0])] = true;
		}

		f >> n;
		f >> s;
		strcpy(x, s.c_str());

		solve();

		g << "Case #" << k << ": " << sol;

		if (k < tests)
		{
			g << "\n";
		}
	}

	f.close();
	g.close();
}