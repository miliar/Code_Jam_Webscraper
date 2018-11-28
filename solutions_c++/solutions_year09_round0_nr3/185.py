#include "stdafx.h"

#include <fstream>
#include <string>
#include <vector>
#include <set>
using namespace std;

int c[501][20];
char w[20] = "welcome to code jam";
char s[1000];

int main()
{
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");

	int N; // N is number of test cases
	fin >> N;
	fin.getline(s, 600); // first one gives nothing back???

	for (int z=1; z <= N; ++z)
	{
		memset(c, 0, sizeof(c));
		c[0][0] = 1;
		fin.getline(s, 600);
		int len = strlen(s);
		if (len >= 19)
		{
			for (int i=1; i<=len; ++i)
			{
				c[i][0] = 1;
				for (int j=19; j>=1; --j)
					c[i][j] = (c[i-1][j] + (s[i-1] == w[j-1] ? c[i-1][j-1] : 0)) % 10000;
			}
		}

		int result = c[len][19];
		fout << "Case #" << z << ": ";
		if (result < 1000) fout << "0";
		if (result < 100) fout << "0";
		if (result < 10) fout << "0";
		fout << result << endl;
	}

	return 0;
}

