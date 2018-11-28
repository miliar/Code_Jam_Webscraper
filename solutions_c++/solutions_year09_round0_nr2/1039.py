
#include <stdio.h>

#include <algorithm>

#include <memory.h>

#include <math.h>

#include <string>

#include <functional>

#include <iostream>

#include <set>

#include <vector>

#include <list>

#include <map>

#include <queue>

#include <stack>

using namespace std;

const int MAX_N =  101;

const int MAX_L = 200001;

int visited[MAX_N][MAX_N];

int a[MAX_N][MAX_N];
char b[MAX_N][MAX_N];
char c[MAX_N][MAX_N];

const int dir4[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

void DFS (int i, int j, int H, int W, char label)
{
	visited[i][j] = 1;
	b[i][j] = label;
	int k = 0;
	int kk = 0;
	int x = 0;
	int y = 0;
	int xx = 0;
	int yy = 0;
	
	for (k = 0; k < 4; ++k)
	{
		x = i + dir4[k][0];
		y = j + dir4[k][1];		

		if (x >= 0 && x < H && y >= 0 && y < W && a[x][y] > a[i][j])
		{
			int lowest = 100000;
			int lowestX = 0;
			int lowestY = 0;
			for (kk = 0; kk < 4; ++kk)
			{
				xx = x + dir4[kk][0];
				yy = y + dir4[kk][1];

				if (xx >= 0 && xx < H && yy >= 0 && yy < W && a[xx][yy] < lowest)
				{
					lowest = a[xx][yy];
					lowestX = xx;
					lowestY = yy;
				}
			}

			if (lowestX == i && lowestY == j && !visited[x][y])
			{
				DFS (x, y, H, W, label);
			}
		}
	}
}


void DFS2 (int i, int j, int H, int W, char label)
{
	visited[i][j] = 1;
	c[i][j] = label;
	int k = 0;
	int x = 0;
	int y = 0;
	
	for (k = 0; k < 4; ++k)
	{
		x = i + dir4[k][0];
		y = j + dir4[k][1];

		if (x >= 0 && x < H && y >= 0 && y < W && !visited[x][y] && b[x][y] == b[i][j])
		{
			DFS2 (x, y, H, W, label);
		}
	}
}


void Work ()
{
	// freopen ("data.in", "r", stdin);
	// freopen ("data.out", "w", stdout);
	
	int T = 0;
	int H = 0;
	int W = 0;

	int i = 0;
	int j = 0;
	int k = 0;
	int t = 0;


	scanf ("%d", &T);

	for (t = 1; t <= T; ++t)
	{	
		scanf ("%d%d", &H, &W);

		vector <pair<int, pair<int, int> > > s;
		for (i = 0; i < H; ++i)
		{
			for (j = 0; j < W; ++j)
			{
				scanf ("%d", &a[i][j]);
				s.push_back(make_pair(a[i][j], make_pair(i, j)));
			}
		}

		char label = 'a';

		sort (s.begin(), s.end());
		memset (visited, 0, sizeof (visited));
		for (i = 0; i < s.size(); ++i)
		{
			j = s[i].second.first;
			k = s[i].second.second;

			if (!visited[j][k])
			{
				DFS(j, k, H, W, label);
				++label;
			}
		}

		memset (visited, 0, sizeof (visited));
		label = 'a';
		for (i = 0; i < H; ++i)
		{
			for (j = 0; j < W; ++j)
			{
				if (!visited[i][j])
				{
					DFS2(i, j, H, W, label);
					++label;
				}
			}
		}

		printf ("Case #%d:\n", t);
		for (i = 0; i < H; ++i)
		{
			for (j = 0; j < W - 1; ++j)
			{
				printf ("%c ", c[i][j]);
			}
			printf ("%c\n", c[i][j]);
		}
	
	}

	
}



int main()
{
	Work ();

	return 0;
}

