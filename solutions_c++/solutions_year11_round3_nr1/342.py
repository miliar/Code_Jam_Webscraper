#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
using namespace std;
#define MAX 52

bool vis[MAX][MAX];

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	int r, c;
	vector<string> v;
	for(int test = 1; test <= t; test++)
	{
		memset(vis, 0, sizeof(vis));
		cin >> r >> c;
		v.clear();
		v.resize(r);
		bool f = true;
		for(int i = 0; i < r; i++)
		{
			cin >> v[i];
		}
		for(int i = 0; i < v.size(); i++)
		{
			for(int j = 0; j < v[i].size(); j++)
			{
				if(v[i][j] == '#' && !vis[i][j])
				{
					f = true;
					vis[i][j] = true;
					if((i + 1 < r && v[i + 1][j] != '#') || i + 1 >= r)
					{
						f = false;
					}
					if((j + 1 < c && v[i][j + 1] != '#') || j + 1 >= c)
					{
						f = false;
					}
					if((i + 1 < r && j + 1 < c && v[i + 1][j + 1] != '#') || i + 1 >= r || j + 1 >= c)
					{
						f = false;
					}
					if(f)
					{
						v[i][j] = '/';
						v[i][j + 1] = '\\';
						v[i + 1][j] = '\\';
						v[i + 1][j + 1] = '/';
					}
					vis[i][j] = true;
					if(i + 1 < r)
						vis[i + 1][j] = true;
					if(j + 1 < c)
						vis[i][j + 1] = true;
					if(j + 1 < c && i + 1 < r)
						vis[i + 1][j + 1] = true;
				}
			}
		}
		f = true;
		for(int i = 0; i < v.size(); i++)
		{
			for(int j = 0; j < v[i].size(); j++)
			{
				if(v[i][j] == '#')
				{
					f = false;
					break;
				}
			}
		}
		cout << "Case #" << test << ":" << endl;
		if(!f)
		{
			cout << "Impossible" << endl;
		}
		else
		{
			for(int i = 0; i < v.size(); i++)
			{
				for(int j = 0; j < v[i].size(); j++)
				{
					cout << v[i][j];
				}
				cout << endl;
			}
		}
	}
	return 0;
}