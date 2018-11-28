#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;


vector<string> a;
int m, n;


bool check()
{
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (a[i][j] == '#')
			{
				if ( (j == n-1) || a[i][j+1] != '#')
					return false;

				if ( (i == m-1) || (a[i+1][j] != '#') || (a[i+1][j+1] != '#'))
					return false;

				a[i][j] = '/';
				a[i][j+1] = '\\';
				a[i+1][j] = '\\';
				a[i+1][j+1] = '/';
			}
		}
	}

	return true;
}


int main()
{
	fstream f, g;
	int nTests;

	f.open("in.txt", ios :: in);
	g.open("out.txt", ios :: out);

	f >> nTests;

	for (int k = 1; k <= nTests; k++)
	{
		f >> m >> n;
		a.clear();

		for (int i = 0; i < m; i++)
		{
			string s;
			f >> s;
			a.push_back(s);
		}

		g << "Case #" << k << ":\n";

		if (!check())
		{
			g << "Impossible";
		}
		else
		{
			for (int i = 0; i < m; i++)
			{
				g << a[i];

				if (i != m-1)
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