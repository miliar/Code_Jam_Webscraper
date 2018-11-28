#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <algorithm>
#include <iomanip>
#include <cmath>

using namespace std;

ifstream fin;
ofstream fout;

int a [1024][1204];

int main (int argc, char * argv [])
{

	if (argc  == 1)  
	{
		fin.open("input.txt");
		fout.open("output.txt");
	}
	else 
	{
		fin.open(argv[1]);
		fout.open(argv[2]);
	}

	int tests = 0;
	fin >> tests;

	while (tests -- > 0)
	{

		int n, m; 
		int r;

		fin >> n >> m >> r;

		memset (a, 0, sizeof (a));

		int x, y;

		for (int i = 0; i < r; ++ i)
		{
			fin >> x >> y;
			a [x][y] = -1;
		}

		a[1][1] = 1;

		for (int i = 1; i <= n; ++ i)
			for (int j = 1; j <= m; ++ j)
				if (i + j > 2)
					if (a[i][j] != -1)
					{
						if (i - 2 >= 1 && j - 1 >= 1)
							if (a[i - 2][j - 1] != -1) a[i][j] += a[i - 2][j - 1];

						if (i - 1 >= 1 && j - 2 >= 1)
							if (a[i - 1][j - 2] != -1) a[i][j] += a[i - 1][j - 2];

						a[i][j] %= 10007;
					}

		static int caseNum = 0;
		fout << "Case #" <<  (++ caseNum) << ": " << a[n][m] << endl;
	}

	return 0;
}