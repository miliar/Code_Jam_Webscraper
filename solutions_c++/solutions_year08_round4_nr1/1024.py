
#include <iostream>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <queue>
#include <map>
#include <vector>
#include <ctime>
#include <cctype>
using namespace std;

	int tree[40];
	int changeable[40];
	int minc[40];
	int m, v;
	int value[40];

bool calculate(int node, int v)
{
	if (2*node > m)
	{
		return tree[node] == v;
	}

	minc[node] = 100;

	if ((tree[node] == 0 || changeable[node]) && (v == 0)) // X OR Y = 0
	{
		if (calculate(2*node, 0) && calculate(2*node+1, 0))
		{
			minc[node] = min(minc[node],
				minc[2*node] + minc[2*node+1]
				+ (tree[node] == 0 ? 0 : 1));

		}
	}

	if ((tree[node] == 0 || changeable[node]) && (v == 1)) // X OR Y = 1
	{
		bool lb = calculate(2*node, 1), rb = calculate(2*node+1, 1);
		if (lb || rb)
		{
			int l = lb ? minc[2*node] : 100;
			int r = rb ? minc[2*node+1] : 100;

			minc[node] = min(minc[node],
				min(l, r)
				+ (tree[node] == 0 ? 0 : 1));
		}
	}
	if ((tree[node] == 1 || changeable[node]) && (v == 0)) // X AND Y = 0
	{
		bool lb = calculate(2*node, 0), rb = calculate(2*node+1, 0);
		if (lb || rb)
		{
			int l = lb ? minc[2*node] : 100;
			int r = rb ? minc[2*node+1] : 100;

			minc[node] = min(minc[node],
				min(l, r)
				+ (tree[node] == 1 ? 0 : 1));
			}
	}
	if ((tree[node] == 1 || changeable[node]) && (v == 1)) // X AND Y = 1
	{
		if (calculate(2*node, 1) && calculate(2*node+1, 1))
		{
			minc[node] = min(minc[node], 
				minc[2*node] + minc[2*node+1]
				+ (tree[node] == 1 ? 0 : 1));
		}
	}

	return minc[node] < 100;
}

void solve(int testcase)
{

	memset(minc, 0, sizeof(minc));

	cin >> m >> v;
	for (int i = 1; i <= (m-1)/2; i++)
	{
		cin >> tree[i];
		cin >> changeable[i];
	}

	for (int i = (m-1)/2+1; i <= m; i++)
	{
		cin >> tree[i];
	}

	/*for (int i = 1; i <= m; i++)
		printf("%d/%d ", tree[i], changeable[i]);*/
	calculate(1, v);

	if (minc[1] == 100)
	printf("Case #%d: IMPOSSIBLE\n", testcase);
	else
	printf("Case #%d: %d\n", testcase, minc[1]);
	
}

int main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
		solve(i+1);
	return 0;
}
