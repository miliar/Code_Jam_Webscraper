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
int heights[2048];
long long solution[2048];
int n;
bool canSolve;
long long factors[2048][2];
void solve(int beg, int end)
{
	if (!canSolve)
		return;
	if (beg + 1 >= end)
		return;
	for (int i = beg + 1; i < end; i++)
	{
		if (heights[i] == end)
		{
			int x = end - i;
			long long y = min(solution[beg], solution[end]) - 1;
			for (int j = end + 1; j < n; j++)
			{
				if(solution[j] == -1 || solution[j] < solution[end])
					continue;
				y = min(y, solution[end] - ((solution[j] - solution[end]) * (end - i) + j - end - 1) / (j - end));
			}
			solution[i] = y;
			solve(beg, i);
			solve(i, end);
			return;
		}
		if (heights[i] > end)
		{
			canSolve = false;
			return;
		}
	}
}

bool checkSolution()
{
	for (int i = 0; i < n - 1; i++)
	{
		vector<pair<double, double> > v;
		for (int j = i + 1; j < n; j++)
		{
			v.push_back(make_pair((double)(solution[j] - solution[i]) / (double)abs(j - i), -j));
		}
		sort(v.rbegin(), v.rend());
		if (-v[0].second != heights[i])
		{
			cout << "Problem for " << i << " it is " << -v[0].second << " and not " << heights[i] << endl;
			return false;
		}
	}
	return true;
}
int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		cin >> n;
		for (int i = 0; i < n - 1; i++)
		{
			cin >> heights[i];
			heights[i]--;
		}
		memset(solution, -1, sizeof(solution));
		int idx = 0;
		canSolve = true;
		factors[0][0] = 0;
		factors[0][1] = 1;
		while(idx < n - 1)
		{
			solution[idx] = solution[heights[idx]] = 1000000000;
			factors[heights[idx]][0] = 0;
			factors[heights[idx]][1] = 1;
			solve(idx, heights[idx]);
			idx = heights[idx];
		}
		

		if (!canSolve)
		{
			cout << "Impossible" << endl;
			continue;
		}
		else
		{
			cout << solution[0];
			for (int i = 1; i < n; i++)
				cout << " " << solution[i];
			cout << endl;
			//checkSolution();
		}
	}
	return 0;
}
