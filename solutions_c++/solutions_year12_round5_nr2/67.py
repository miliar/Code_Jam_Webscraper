#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;

#define SIZE 128

bool vis[SIZE][SIZE];

set<int> corner[SIZE][SIZE];
set<int> edge[SIZE][SIZE];

int fathers[SIZE][SIZE][2];
int s, m;
bool is_in(int x, int y)
{
	return x >= 1 && x <= 2 * s - 1 && y >= 1 && y <= 2 * s - 1 && abs(x - y) <= s - 1;
}

bool tmpVis[SIZE][SIZE];
int mat[6][2] = {{1, 1}, {-1, -1}, {1, 0}, {0, 1}, {-1, 0}, {0, -1}};
bool hasRing()
{
	memset(tmpVis, false, sizeof(tmpVis));
	for (int i = 1; i < 2 * s; i++)
	{
		for (int j = 1; j < 2 * s; j++)
		{
			if(!vis[i][j] && !tmpVis[i][j] && is_in(i, j))
			{
				tmpVis[i][j] = true;
				queue<pair<int, int> >toProcess;
				toProcess.push(make_pair(i, j));
				
				pair<int, int> cur;
				bool found = false;
				int x, y;
				while(!toProcess.empty())
				{
					cur = toProcess.front();
					toProcess.pop();
					for (int k = 0; k < 6; k++)
					{
						x = cur.first + mat[k][0];
						y = cur.second + mat[k][1];
						if (!is_in(x, y))
						{
							found = true;
							continue;
						}
						if (tmpVis[x][y] || vis[x][y])
							continue;
						tmpVis[x][y] = true;
						toProcess.push(make_pair(x, y));
					}
				}
				if (!found)
					return true;
			}
		}
	}
	return false;
}

pair<int, int> findFather(int x, int y)
{
	int tmpX;
	queue<pair<int, int> > passed;
	while(fathers[x][y][0] != -1)
	{
		passed.push(make_pair(x, y));
		tmpX = fathers[x][y][0];
		y = fathers[x][y][1];
		x = tmpX;
	}
	pair<int, int> cur;
	while(!passed.empty())
	{
		cur = passed.front();
		passed.pop();
		fathers[cur.first][cur.second][0] = x;
		fathers[cur.first][cur.second][1] = y;
	}
	return make_pair(x, y);
}

int compSize[SIZE][SIZE];

void merge(int x1, int y1, int x2, int y2)
{
	pair<int, int> p1 = findFather(x1, y1);
	pair<int, int> p2 = findFather(x2, y2);

	if (p1 == p2)
		return;

	for (set<int>::iterator itr = corner[p1.first][p1.second].begin(); itr != corner[p1.first][p1.second].end(); ++itr)
	{
		corner[p2.first][p2.second].insert(*itr);
	}
	for (set<int>::iterator itr = edge[p1.first][p1.second].begin(); itr != edge[p1.first][p1.second].end(); ++itr)
	{
		edge[p2.first][p2.second].insert(*itr);
	}

	for (set<int>::iterator itr = corner[p2.first][p2.second].begin(); itr != corner[p2.first][p2.second].end(); ++itr)
	{
		corner[p1.first][p1.second].insert(*itr);
	}
	for (set<int>::iterator itr = edge[p2.first][p2.second].begin(); itr != edge[p2.first][p2.second].end(); ++itr)
	{
		edge[p1.first][p1.second].insert(*itr);
	}

	if (compSize[p1.first][p1.second] > compSize[p2.first][p2.second])
	{
		fathers[p2.first][p2.second][0] = p1.first;
		fathers[p2.first][p2.second][1] = p1.second;
		compSize[p1.first][p1.second] += compSize[p2.first][p2.second];
	}
	else
	{
		fathers[p1.first][p1.second][0] = p2.first;
		fathers[p1.first][p1.second][1] = p2.second;
		compSize[p2.first][p2.second] += compSize[p1.first][p1.second];
	}
}

int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		//cerr << testCounter << endl;
		printf("Case #%d: ", testCounter + 1);
		memset(vis, false, sizeof(vis));
		
		cin >> s >> m;
		
		for (int i = 0; i < SIZE; i++)
			for (int j = 0; j < SIZE; j++)
			{
				corner[i][j].clear();
				edge[i][j].clear();
			}
		corner[1][1].insert(0); 
		corner[1][s].insert(1); 
		corner[s][1].insert(2); 
		corner[2 * s - 1][s].insert(3);
		corner[s][2 * s - 1].insert(4); 
		corner[2 * s - 1][2 * s - 1].insert(5);

		for (int i = 2; i < s; i++)
		{
			edge[i][1].insert(0);
			edge[1][i].insert(1);
			edge[s - 1 + i][i].insert(4);
			edge[i][s - 1 + i].insert(5);
		}
		for (int i = s + 1; i < 2 * s - 1; i++)
		{
			edge[2 * s - 1][i].insert(2);
			edge[i][2 * s - 1].insert(3);
		}

		memset(fathers, -1, sizeof(fathers));
		int x, y;

		for (int i = 0; i < SIZE; i++)
			for (int j = 0; j < SIZE; j++)
			{
				compSize[i][j] = 1;
			}
		bool printed = false;
		for (int i = 0; i < m; i++)
		{
			cin >> x >> y;
			if (printed)
				continue;
			vis[x][y] = true;

			for (int j = 0; j < 6; j++)
			{
				if (is_in(x + mat[j][0], y + mat[j][1]) && vis[x + mat[j][0]][y + mat[j][1]])
				{
					merge(x, y, x + mat[j][0], y + mat[j][1]);
				}
			}
			pair<int, int> father = findFather(x, y);
			bool ring = false, fork = false, bridge = false;
			ring = hasRing();
			fork = edge[father.first][father.second].size() >= 3;
			bridge = corner[father.first][father.second].size() >= 2;

			if (ring && fork && bridge) { cout << "bridge-fork-ring in move " << i + 1 << endl; printed = true; continue; }
			else if (ring && fork)  { cout << "fork-ring in move " << i + 1 << endl; printed = true; continue; }
			else if (fork && bridge)  { cout << "bridge-fork in move " << i + 1 << endl; printed = true; continue; }
			else if (ring && bridge)  { cout << "bridge-ring in move " << i + 1 << endl; printed = true; continue; }
			else if (ring)  { cout << "ring in move " << i + 1 << endl; printed = true; continue; }
			else if (bridge)  { cout << "bridge in move " << i + 1 << endl; printed = true; continue; }
			else if (fork)  { cout << "fork in move " << i + 1 << endl; printed = true; continue; }

		}
		if (!printed)
		{
			cout << "none" << endl;
		}
	}
	return 0;
}
