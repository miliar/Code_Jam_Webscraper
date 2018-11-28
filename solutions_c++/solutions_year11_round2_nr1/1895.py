#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <string.h>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

#define MAX_LIM 101

int n;

string a[MAX_LIM];
long    games[MAX_LIM];
long    wins[MAX_LIM];
long double WP[MAX_LIM];
long double OWP[MAX_LIM];
long double OOWP[MAX_LIM];
long double RPI[MAX_LIM];

void computeWP()
{
	for (int i = 0; i < n; i++)
	{
		games[i] = 0;
		wins[i] = 0;
		WP[i] = 0.0;

		for (int j = 0; j < n; j++)
		{
			if (a[i][j] == '.') continue;

			games[i]++;

			if (a[i][j] == '1') 
			{
				wins[i]++;
			}
		}

		if (games[i] != 0)
		{
			WP[i] = ((long double)wins[i])/games[i];
		}
	}
}

void computeOWP()
{
	for (int i = 0; i < n;  i++)
	{
		long count = 0;
		long double sum = 0.0;
		OWP[i] = 0.0;

		for (int j = 0; j < n; j++)
		{
			int w = wins[j];
			int g = games[j]-1;

			if (a[i][j] == '.') continue;

			if (a[j][i] == '1') w--;

			if (g != 0) sum += ((double)w)/g;

			count++;
		}

		if (count != 0)
		{
			OWP[i] = sum/count;
		}
	}
}


void computeOOWP()
{
	for (int i = 0; i < n; i++)
	{
		long double sum = 0;
		long count = 0;
		OOWP[i] = 0;

		for (int j = 0; j < n; j++)
		{
			if (a[i][j] == '.') continue;

			sum += OWP[j];
			count++;
		}

		if (count != 0)
		{
			OOWP[i] = sum/count;
		}
	}
}


void computeRPI()
{
	computeWP();
	computeOWP();
	computeOOWP();

	for (int i = 0; i < n; i++)
	{
		RPI[i] =  WP[i]/4 + OWP[i]/2 + OOWP[i]/4;
	}
}



int main()
{
	ifstream f;
	ofstream g;
	int nTests;

	f.open("in.txt");
	g.open("out.txt");

	f >> nTests;

	for (int k = 1; k <= nTests; k++)
	{
		f >> n;

		for (int i = 0; i< n; i++)
		{
			f >> a[i];
		}

		computeRPI();

		g << "Case #" << k << ":\n";

		for (int i = 0; i < n; i++)
		{
			g << setprecision(12) << RPI[i];

			if (i != n-1)
			{
				g << "\n";
			}
		}

		if (k != nTests)
			g << "\n";
	}

	f.close();
	g.close();

	return 0;
}