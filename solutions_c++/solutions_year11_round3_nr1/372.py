#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const int MAX = 50;

int a[MAX][MAX];

int main()
{
	ofstream fout ("A-large.out");
	ifstream fin ("A-large.in");

	int t, tt;
	fin >> t;
	tt = t;
	while(t --> 0)
	{
		int n, m, c = 0;
		fin >> n >> m;
		fout << "Case #" << tt - t << ":" << endl;
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				a[i][j] = 0;
		for(int i = 0; i < n; i++)
		{
			string s;
			fin >> s;
			for(int j = 0; j < m; j++)
				if(s[j] == '#')
					a[i][j] = 1, c++;
		}
		if(c % 4 != 0)
		{	fout << "Impossible" << endl; continue;	}
		for(int i = 0; i < n - 1; i++)
			for(int j = 0; j < m - 1; j++)
				if(a[i][j] == 1 && a[i + 1][j] == 1 && a[i][j + 1] == 1 && a[i + 1][j + 1] == 1)
					a[i][j] = -1,
					a[i + 1][j] = -2,
					a[i][j + 1] = -3,
					a[i + 1][j + 1] = -4;
		bool b = false;
		for(int i = 0; i < n && !b; i++)
			for(int j = 0; j < m && !b; j++)
				if(a[i][j] == 1)
					b = true;
		if(b)
		{	fout << "Impossible" << endl; continue;	}
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < m; j++)
			{
				if(a[i][j] == 0)
					fout << '.';
				else if(a[i][j] == -1)
					fout << '/';
				else if(a[i][j] == -2)
					fout << "\\";
				else if(a[i][j] == -3)
					fout << "\\";
				else if(a[i][j] == -4)
					fout << '/';
			}
			fout << endl;
		}
	}
	return 0;
}
