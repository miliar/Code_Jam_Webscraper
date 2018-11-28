#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin("A-large.in.txt");
ofstream fout("A-large.out.txt");

int n, m, v;
int gate[10240], change[10240];
int son[10240];
int value[10240];

unsigned int ans[10240][2];

int main()
{

	fin >> n;
	for (int cases = 1; cases <= n; cases++)
	{
		fin >> m >> v;

		for (int i = 1; i <= (m-1)/2; i++)
		{
			fin >> gate[i] >> change[i];
			son[i] = 0;
		}
		
		for (int i = (m-1)/2 + 1; i <= m; i++)
		{
			fin >> value[i];
			son[i] = 1;
		}

		for (int i = 1; i <= m; i++) ans[i][0] = ans[i][1] = 10240;

		int x, y, res;

		for (int i = m; i >= 1; i--)
		{
			if (son[i] == 1)
				ans[i][value[i]] = 0;
			else
			{
				x = i * 2;
				y = i * 2 + 1;

				for (int a = 0; a < 2; a++)
					for (int b = 0; b < 2; b++)
					{
						if (gate[i] == 1)
							res = a & b;
						else
							res = a | b;
						if (ans[x][a] + ans[y][b] < ans[i][res])
							ans[i][res] = ans[x][a] + ans[y][b];

						if (change[i] == 1)
						{
							if (gate[i] == 1)
								res = a | b;
							else
								res = a & b;
							if (ans[x][a] + ans[y][b] + 1 < ans[i][res])
								ans[i][res] = ans[x][a] + ans[y][b] + 1;
						}
					}
			}	
		}

		if (ans[1][v] == 10240)
			fout << "Case #" << cases << ": IMPOSSIBLE" << endl;
		else
			fout << "Case #" << cases << ": " << ans[1][v] << endl;

	}

	return 0;
}
