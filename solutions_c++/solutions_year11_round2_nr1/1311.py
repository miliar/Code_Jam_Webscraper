#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

vector<long double> solve(vector<string> &v)
{
	int n = v.size();
	vector<long double> ans(n, 0);
	vector<long double> wp(n, 0), owp(n, 0), oowp(n, 0);
	vector<int> games(n, 0);
	vector<int> wins(n, 0);
	vector<vector<int>> opps(n);
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (v[i][j] != '.')
			{
				games[i]++;
				wins[i] += (v[i][j] - '0');
				opps[i].push_back(j);
			}
		}
	}
	for (int i = 0; i < n; i++)
	{
		wp[i] = (wins[i] * 1.0) / games[i];
	}
	vector<vector<long double>> twp(n, vector<long double>(n, 0));
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (v[i][j] == '.')
				twp[i][j] = wp[i];
			else
			{
				twp[i][j] = ((wins[i] - (v[i][j] - '0')) * 1.0) / (games[i] - 1);
			}
		}
	}
	for (int i = 0; i < n; i++)
	{
		long double sum = 0;
		for (int j = 0; j < opps[i].size(); j++)
		{
			sum += twp[opps[i][j]][i];
			//	wp[opps[i][j]];
		}
		if (opps[i].size() == 0)
			owp[i] = 0;
		else
			owp[i] = sum / opps[i].size();
	}
	for (int i = 0; i < n; i++)
	{
		long double sum = 0;
		for (int j = 0; j < opps[i].size(); j++)
		{
			sum += owp[opps[i][j]];
		}
		if (opps[i].size() == 0)
			oowp[i] = 0;
		else
			oowp[i] = sum / opps[i].size();
	}
	for (int i = 0; i < n; i++)
	{
		ans[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
	}
	return ans;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int n; 
		cin >> n;
		vector<string> v(n);
		for (int j = 0; j < n; j++)
			cin >> v[j];
		vector<long double> ans = solve(v);
		printf("Case #%d:\n", i + 1);
		for (int j = 0; j < ans.size(); j++)
			cout << ans[j] << endl;
	}
	return 0;
}