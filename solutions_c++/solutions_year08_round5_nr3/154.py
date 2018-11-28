#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin("C-large.in.txt");
ofstream fout("C-large.out.txt");

char map[100][100];
int num[100][100];

int C, n, m;
int tot[2];

int dire[6][2] = {{0,-1},{0,1},{-1,-1},{-1,1},{1,-1},{1,1}};
int edge[2][4000][6];

int opy[4000];
int usey[4000];
int usex[4000];
int ans;

bool fill(int x)
{
	for (int i = 0; i < 6; i++)
	if (edge[0][x][i] != -1 &&   usey[edge[0][x][i]] == 0  )
	{
		int y = edge[0][x][i];
		usey[y] = 1;

		if (opy[y] == -1 || fill(opy[y]) == true)
		{
			usex[x] = 1;
			opy[y] = x;
			return true;
		}
	}

	return false;
}

int main()
{
	fin >> C;
	for (int cases = 1; cases <= C; cases++)
	{
		fin >> n >> m;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				fin >> map[i][j];
			}
		}

		tot[0] = tot[1] = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				num[i][j] = -1;

		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			if (map[i][j] == '.')
			{
				num[i][j] = tot[j%2];
				tot[j % 2]++;				
			}

		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			if (map[i][j] == '.')
			{
				int x, y;

				for (int k = 0; k < 6; k++)
				{
					x = i + dire[k][0];
					y = j + dire[k][1];
				

					if (x >= 0 && x < n && y >= 0 && y < m && map[x][y] == '.')
						edge[j%2][num[i][j]][k] = num[x][y];
					else
						edge[j%2][num[i][j]][k] = -1;
				}
			}

		for (int i = 0; i < tot[1]; i++)
			opy[i] = -1;

		ans = 0;
		memset(usex, 0, sizeof(usex));

		bool ok = true;
		while (ok)
		{
			ok = false;
			for (int i = 0; i < tot[0]; i++)
			{
				memset(usey, 0, sizeof(usey));
				if (usex[i] == 0 && fill(i) == true)
				{
					ans++;
					ok = true;
				}
			}
		}

		fout << "Case #" << cases << ": " << tot[0]+tot[1]-ans << endl;

	}
	
	return 0;
}