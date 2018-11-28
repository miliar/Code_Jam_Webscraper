#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

ifstream fin("A-large (1).in");
ofstream fout("1c_alarge.out");

//#define fout cout

vector<string> d;

bool check(int x, int y)
{
	return d[x][y] == '#' && d[x+1][y] == '#' && d[x][y+1] == '#'&& d[x+1][y+1]=='#'; 
}

int main()
{
	int T;
	fin >> T;
	for (int cases =0; cases< T; cases++)
	{
		fout <<"Case #" << cases+1 << ":\n";
		int m, n;
		fin >> m >> n;
		d.clear();
		for(int i=0; i<m; i++)
		{
			string s;
			fin >> s;
			d.push_back(s);
		}

		bool success = true;
		for (int i=0; i<m-1; i++)
		{
			for (int j=0; j<n-1; j++)
				if (d[i][j] == '#')
					if (check(i,j))
					{
						d[i][j]='/';
						d[i][j+1] = '\\';
							d[i+1][j] = '\\';
							d[i+1][j+1] = '/';
					}
					else {success=false; goto out;}
		}
		for (int i=0; i<m; i++)
		{
			for (int j=0; j<n; j++)
				if (d[i][j] == '#')
				{
					success=false;
					goto out;
				}
		}
out:
		if (success)
		{
			for (int i=0; i<m; i++) fout << d[i] << '\n';
		}
		else fout << "Impossible\n";
	}
	return 0;
}
