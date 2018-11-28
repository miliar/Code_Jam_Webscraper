#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <string>
#include <map>
#include <set>

using namespace std;

int cTest;
int n, m;
int mas[101][101];
int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};
int color[20001];

int FindSet(int pos)
{
	if (color[pos] == pos) return color[pos];
	else color[pos] = FindSet(color[pos]);
}

void Union(int a, int b)
{
	if (rand() % 2) color[a] = b;
	else color[b] = a;
}

map < int, char > id;
char last;
char Add(int pos)
{
	map <int,char>::iterator it = id.find(pos);
	if (it == id.end()) 
	{
		id.insert(make_pair(pos, last ++));
		return last - 1;
	}
	else return it->second;
}


int main()
{
	freopen("readme.txt","r",stdin);
	freopen("output.txt","w",stdout);

	cin >> cTest;
	for (int test = 1; test <= cTest; ++ test)
	{
		cout << "Case #" << test << ":\n";
		last = 'a';
		id.clear();
		
		cin >> n >> m;
		for (int i = 0; i < n; ++ i)
		{
			for (int j = 0; j < m; ++ j)
			{
				cin >> mas[i][j];
				color[i * m + j] = i * m + j;
			}
		}

		int X, Y;
		for (int i = 0; i < n; ++ i)
		{
			for (int j = 0; j < m; ++ j)
			{
				int to = -1;
				int best = mas[i][j];
				for (int k = 0; k < 4; ++ k)
				{
					X = i + dx[k];
					Y = j + dy[k];
					if (X < 0 || Y < 0 || X == n || Y == m)
						continue;
					if (mas[X][Y] < best)
					{
						best = mas[X][Y];
						to = k;
					}
					
				}
				if (to >= 0)
				{
					if (FindSet(i * m + j) != FindSet((i + dx[to]) * m + j + dy[to]))
						Union(FindSet(i * m + j), FindSet((i + dx[to]) * m + j + dy[to]));
				}
			}
		}

		for (int i = 0; i < n; ++ i)
		{
			for (int j = 0; j < m; ++ j)
			{
				cout << Add(FindSet(i * m + j));
				if (j != m - 1) cout << " ";
				else cout << "\n";
			}
		}

		

	}
	

	return 0;
}