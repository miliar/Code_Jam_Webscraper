#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <cstdio>
#include <vector>
#include <limits.h>
#include <string>

using namespace std;

typedef long long int64;

#define y1 PALEVO

int c[1000][1000];

int n;

vector <pair<int, int> > del, cre;


void process()
{
	for (int i = 0; i < (int)del.size(); i++)
		c[del[i].first][del[i].second] = 0;
	for (int i = 0; i < (int)cre.size(); i++)
		c[cre[i].first][cre[i].second] = 1;
	del.clear();
	cre.clear();
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	for (int test = 0; test < t; test++)
	{
		memset(c, 0, sizeof c);
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int x = x1; x <= x2; x++)
				for (int y = y1; y <= y2; y++)
					c[x][y] = 1;
		}
		int ans = 0;
		while (true)
		{
			bool ok = false;
			for (int i = 0; i <= 100; i++)
			{
				for (int j = 0; j <= 100; j++)
				{
					if (c[i][j] == 1)
					{
						ok = true;
						if (c[i - 1][j] == 0 && c[i][j - 1] == 0)
						{
							del.push_back(make_pair(i, j));
						}
					}
					else
					{
						if (c[i - 1][j] == 1 && c[i][j - 1] == 1)
						{
							cre.push_back(make_pair(i, j));
						}

					}
				}
			}
			if (!ok)
				break;
			process();
			++ans;

		}
		printf("Case #%d: ", test + 1);
		cout << ans << endl;
	}
	return 0;
}