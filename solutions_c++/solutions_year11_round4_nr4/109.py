#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cassert>

using namespace std;

const double eps = 1e-8;

bool Equal(double a, double b)
{
	return fabs(a-b) < eps;
}

bool Less(double a, double b)
{
	return a < b && (!Equal(a, b));
}

bool Great(double a, double b)
{
	return a > b && (!Equal(a, b));
}

int v, e;
int adjMat[50][50];

void Scan()
{	
	for (int i = 0; i < 50; i++)
		for (int j = 0; j < 50; j++)
			adjMat[i][j] = 0;
	scanf("%d%d", &v, &e);
	for (int i = 0; i < e; i++)
	{
		int a, b;
		scanf("%d,%d", &a, &b);
		assert(adjMat[a][b] == 0);
		adjMat[a][b] = adjMat[b][a] = 1;
	}
}

int queue[50];
bool mark[50];

void Bfs(int s, int *dist)
{
	for (int i = 0; i < 50; i++)
	{
		mark[i] = false;
		dist[i] = -1;
	}
	int l, r;
	l = r = 0;
	queue[0] = s;
	mark[s] = 0;
	dist[s] = 0;
	while (l <= r)
	{
		int cur = queue[l++];
		for (int i = 0; i < v; i++)
			if (adjMat[cur][i] == 1 && !mark[i])
			{
				mark[i] = true;
				dist[i] = dist[cur] + 1;
				queue[++r] = i;
			}
	}
}

int dist0[50];
int dist1[50];
int chainLen;

int chain[50];
int bestAns;

void Brute(int len = 1)
{
	if (len == chainLen)
	{
		for (int i = 0; i < 50; i++)
			mark[i] = false;
		int cnt = 0;
		for (int i = 0; i < len; i++)
		{
			mark[chain[i]] = true;
		}
		for (int i = 0; i < len; i++)
		{
			for (int j = 0; j < v; j++)
			{
				if (adjMat[chain[i]][j] == 1 && (!mark[j]))
				{
					mark[j] = true;
					cnt++;
				}
			}
		}
		if (cnt > bestAns)
		{
			bestAns = cnt;
		}
		return;
	}

	for (int i = 0; i < v; i++)
	{
		if (adjMat[chain[len-1]][i] == 1 && dist1[i] == chainLen-len)
		{
			chain[len] = i;
			Brute(len+1);
			chain[len] - 0;
		}
	}
}

void Solve()
{
	bestAns = -1;
	Bfs(0, dist0);
	Bfs(1, dist1);
	chainLen = dist0[1];
	chain[0] = 0;
	Brute();
	printf("%d %d\n", chainLen-1, bestAns);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		Scan();
		fprintf(stderr, "test %d\n", i+1);
		fprintf(stderr, "%d %d\n", v, e);
		for (int i = 0; i < v; i++)
		{
			for (int j = 0; j < v; j++)
			{
				fprintf(stderr, "%d",adjMat[i][j]);
			}
			fprintf(stderr, "\n");
		}
		printf("Case #%d: ", i+1);		
		Solve();
	}
	return 0;
}