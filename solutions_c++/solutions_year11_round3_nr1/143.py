#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cstring>

using namespace std;

const int MaxN = 55;
int N;
int R, C;
string Map[MaxN];

bool inside (int x, int y)
{
	if (x < 0 || x >= R && y < 0 && y >= C) return false;
	if (Map[x][y] != '#') return false;
	return true;
}

int main()
{
	int Ncase;
	freopen("a_large.in", "r", stdin);
	freopen("a_large.out", "w", stdout);
	cin >> Ncase;
	for (int run = 0; run < Ncase; ++run)
	{
		cin >> R >> C;
		for (int i = 0; i < R; ++i)
			cin >> Map[i];

		bool ok = true;
		for (int i = 0; i < R; ++i)
		{
			for (int j = 0; j < C; ++j)
			{
				if (Map[i][j] == '#')
				{
					if (inside(i, j+1) && inside(i+1, j) && inside(i+1, j+1))
					{
						Map[i][j] = '/';
						Map[i][j+1] = '\\';
						Map[i+1][j] = '\\';
						Map[i+1][j+1] = '/';
					}
					else
					{
						ok = false;
						break;
					}
				}
			}
			if (!ok) break;
		}
		cout << "Case #" << run+1 << ":" << endl;
		if (!ok) cout << "Impossible" << endl;
		else
		{
			for (int i = 0; i < R; i++)
				cout << Map[i] << endl;
		}
	}
}
