#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

ifstream fin("D-small-attempt0.in.txt");
ofstream fout("D-small-attempt0.out.txt");

int map[10][10];

int n, m;
int way[10];
int edge[10][2];
int use[10];
int c;


bool dfs(int step)
{
	if (step > m)
	{
		for (int i = 0; i < m-1; i++)
		{
			int a = way[edge[i][0]];
			int b = way[edge[i][1]];
			if (map[a][b] == 0)
				return false;
		}
			return true;
	}

	for (int i = 1; i <= n; i++)
		if (use[i] == 0)
		{
			use[i] = 1;
			way[step] = i;

			if (dfs(step+1)) return true;

			use[i] = 0;
		}
	return false;
}

int main()
{
	fin >> c;
	for (int cases = 1; cases <= c; cases++)
	{
		memset(map, 0, sizeof(map));

		fin >> n;
		for (int i = 0; i < n-1; i++)
		{
			int a, b;
			fin >> a >> b;
			map[a][b] = map[b][a] = 1;
		}

		fin >> m;
		for (int i = 0; i < m-1; i++)
		{
			fin >> edge[i][0] >> edge[i][1];
		}

		memset(use, 0, sizeof(use));

		fout << "Case #" << cases << ": ";
		if (dfs(1))
		{
			fout << "YES" << endl;

		} else fout << "NO" << endl;

	}



	return 0;
}