#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

typedef pair<long long, long long> pll;
typedef pair<int, int> pii;
typedef pair<long double, long double> plld;
typedef pair<double, double> pd;

vector<string> solve(vector<string> v)
{
	int n = v.size();
	int m = v[0].size();
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (v[i][j] == '#')
			{
				if (i + 1 < n && j + 1 < m && v[i + 1][j] == '#' && v[i][j + 1] == '#' && v[i + 1][j + 1] == '#')
				{
					v[i][j] = '/';
					v[i + 1][j] = '\\';
					v[i + 1][j + 1] = '/';
					v[i][j + 1] = '\\';
				}
				else
				{
					v.clear();
					return v;
				}
			}
		}
	}
	return v;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int n, m;
		cin >> n >> m;
		vector<string> v(n);
		for (int j = 0; j < n; j++)
			cin >> v[j];
		vector<string> ans = solve(v);
		printf("Case #%d:\n", i + 1);
		//print ans
		if (ans.size() == 0)
		{
			cout << "Impossible" << endl;
		}
		else
		{
			for (int j = 0; j < n; j++)
				cout << ans[j] << endl;
		}
	}
	return 0;
}