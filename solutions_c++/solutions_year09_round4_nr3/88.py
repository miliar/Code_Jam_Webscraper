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
int mat[256][256];

int flow(const vector<vector<int> >& neighbours)
{
	int n = neighbours.size();
	int res = 0;
	int sink = n - 1;
	int cur;
	while(1)
	{
		queue<int> toProcess;
		vector<int> fathers(neighbours.size(), -1);
		toProcess.push(0);
		fathers[0] = -2;
		while(fathers[sink] == -1 && !toProcess.empty())
		{
			cur = toProcess.front();
			toProcess.pop();
			for(int i = 0; i < neighbours[cur].size(); i++)
			{
				if(mat[cur][neighbours[cur][i]] > 0 && fathers[neighbours[cur][i]] == -1)
				{
					fathers[neighbours[cur][i]] = cur;
					toProcess.push(neighbours[cur][i]);
				}
			}
		}
		if(fathers[sink] == -1)
			return res;
		
		cur = sink;
		int minm = 1e9;
		while(fathers[cur] != -2)
		{
			minm = min(minm, mat[fathers[cur]][cur]);
			cur = fathers[cur];
		}
		res += minm;
		cur = sink;
		while(fathers[cur] != -2)
		{
			mat[cur][fathers[cur]] += minm;
			mat[fathers[cur]][cur] -= minm;
			cur = fathers[cur];
		}
	}
}
vector<vector<int> > v;
bool isSmaller(int i, int j)
{
	for(int k = 0; k < v[i].size(); k++)
	{
		if(v[i][k] >= v[j][k])
			return false;
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
		int n, k;
		cin >> n >> k;
		v.clear();
		v.resize(n);
		for(int i = 0; i < n; i++)
		{
			v[i].resize(k);
			for(int j = 0; j < k; j++)
				scanf("%d", &v[i][j]);
		}
		vector<vector<int> > neighbours(2 * n + 2);
		for(int i = 1; i <= n; i++)
		{
			neighbours[0].push_back(i);
			mat[0][i] = 1;
			mat[i][0] = 0;
		}
		for(int i = n + 1; i <= 2 * n; i++)
		{
			neighbours[i].push_back(2 * n + 1);
			mat[i][2 * n + 1] = 1;
			mat[2 * n + 1][i] = 0;
		}
		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
			{
				if(i == j)
					continue;
				if(isSmaller(i, j))
				{
					neighbours[i + 1].push_back(j + n + 1);
					neighbours[j + n + 1].push_back(i + 1);
					mat[i + 1][j + n + 1] = 1;
					mat[j + n + 1][i + 1] = 0;
				}
			}
		cout << n - flow(neighbours) << endl;
	}
	return 0;
}
