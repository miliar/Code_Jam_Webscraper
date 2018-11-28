#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out.txt");

int n, m;
int map[2096][2096];
int t[2096];
int used[2096];

int res[2096];
bool ans;

void update(int id, int fla)
{
	res[fla] = map[id][fla];

	for (int i = 0; i < m; i++)
	if (map[i][fla] > 0 && map[i][fla] != res[fla])
		t[i]--;
}

int main()
{
	int a, b, c;
	int id;

	fin >> c;
	for (int cases = 1; cases <= c; cases ++)
	{
		memset(map, 0, sizeof(map));
		memset(t, 0, sizeof(t));
		memset(used, 0, sizeof(used));
		memset(res, 0, sizeof(res));

		fin >> n >> m;
		for (int i = 0; i < m; i++)
		{
			fin >> t[i];
			for (int j = 0; j < t[i]; j++)
			{
				fin >> a >> b;
				map[i][a] = b+1;
			}
		}

		ans = true;

		while (1)
		{
			bool ok = true;
			for (int i = 0; i < m; i++)
			{
				if (t[i] == 0)
				{
					ans = false;
					break;
				}
				if (t[i] == 1 && used[i] == 0)
				{
					used[i] = 1;
					id = i;
					ok = false;
					break;
				}
			}

			if (ans == false) break;
			if (ok == true) break;

			for (int i = 1; i <= n; i++)
				if (map[id][i] > 0 && res[i] == 0)
				{
					update(id, i);
					break;
				}
		}

		fout << "Case #" << cases <<": ";

		if (ans == true)
		{
			for (int i = 1; i <= n; i++)
			{
				if (res[i] == 0) fout << "0 ";
				if (res[i] == 1) fout << "0 ";
				if (res[i] == 2) fout << "1 ";
			}

			fout << endl;
		} else
		{
			fout << "IMPOSSIBLE" << endl;
		}

	}

	return 0;
}