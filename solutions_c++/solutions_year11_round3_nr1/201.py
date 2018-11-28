#include<iostream>
#include<string>
#include<fstream>
#include<cmath>
#include<vector>
#include<cstdio>
#include<algorithm>
using namespace std;


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	cin >> t;
	for(int test = 1; test <= t; test++)
	{
		int n, m;
		cin >> n >> m;
		vector<string> g(n);
		for(int i = 0; i < n; i++)
			cin >> g[i];
		for(int i = 0; i < n-1; i++)
		{
			for(int j = 0; j < m-1; j++)
			{
				if(g[i][j] == '#' && g[i][j+1] == '#' && g[i+1][j] == '#' && g[i+1][j+1] == '#')
				{
					g[i][j] = '/';
					g[i][j+1] = '\\';
					g[i+1][j] = '\\';
					g[i+1][j+1] = '/';
				}
			}
		}

		bool ok = true;
		for(int i = 0; ok && i < n; i++)
			for(int j = 0; ok && j < m; j++)
				if(g[i][j] == '#')
					ok = false;

		cout << "Case #" << test << ":" << endl;
		if(ok)
			for(int i = 0; i < n; i++)
				cout << g[i] << endl;
		else
			cout << "Impossible" << endl;

	}



	return 0;
}