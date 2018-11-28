#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <ctime>

#define MAX 128

using namespace std;
FILE *in; FILE *out;

int n, m;
int a[MAX][MAX];
int vis[MAX*MAX];
char ans[MAX][MAX];
vector <int> v[MAX*MAX];
int dir[4][2] = { {-1, 0}, {0, -1}, {0, 1}, {1, 0} };

void fill(int row, int col, char letter)
{
	queue <int> q;
	q.push(row * MAX + col); vis[row * MAX + col] = 1;
	
	while (!q.empty())
	{
		int cur = q.front(); q.pop();
		ans[cur / MAX][cur % MAX] = letter;
		
		for (int i=0; i<(int)v[cur].size(); i++)
			if (!vis[v[cur][i]]) q.push(v[cur][i]), vis[v[cur][i]] = 1;
	}
}

void doWork(int testNum)
{
	fscanf(in, "%d %d", &n, &m);
	
	memset(a, 11, sizeof(a));
	memset(ans, 'X', sizeof(ans));

	for (int i=1; i<=n; i++)
		for (int c=1; c<=m; c++)
			fscanf(in, "%d", &a[i][c]);
	
	for (int i=0; i<MAX*MAX; i++)
		v[i].clear();
	
	for (int i=1; i<=n; i++)
	{
		for (int c=1; c<=m; c++)
		{
			int row = -1, col = -1, minn = MAX*MAX;
			for (int j=0; j<4; j++)
			{
				int nrow = i + dir[j][0];
				int ncol = c + dir[j][1];
				if (a[nrow][ncol] >= a[i][c]) continue;				
				if (minn > a[nrow][ncol]) {minn = a[nrow][ncol]; row = nrow; col = ncol;}
			}
			if (row != -1 && col != -1)
				v[row * MAX + col].push_back(i * MAX + c);
		}
	}

	memset(vis, 0, sizeof(vis));
	char nextLetter = 'A';
	for (int i=1; i<=n; i++)
	{
		for (int c=1; c<=m; c++)
		{
			int isSink = 1;
			for (int j=0; j<4; j++)
			{
				int nrow = i + dir[j][0];
				int ncol = c + dir[j][1];
				if (a[nrow][ncol] < a[i][c]) {isSink = 0; break;}
			}
			if (isSink) fill(i, c, nextLetter++);
		}
	}

	nextLetter = 'a';
	for (int i=1; i<=n; i++)
	{
		for (int c=1; c<=m; c++) if (isupper(ans[i][c]))
		{
			char mark = ans[i][c];
			for (int j=1; j<=n; j++)
				for (int k=1; k<=m; k++)
					if (ans[j][k] == mark) ans[j][k] = nextLetter;
			nextLetter++;
		}
	}

	for (int i=1; i<=n; i++)
		for (int c=1; c<=m; c++)
			fprintf(out, "%c%c", ans[i][c], c == m ? '\n' : ' ');
	
	return;
}

int main(void)
{
	unsigned sTime = clock();
	in = fopen("Watersheds.in", "rt");
	out = fopen("Watersheds.out", "wt");
	
	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++)
	{
		fprintf(stderr, "Currently executing test %d...\n", test);
		fprintf(out, "Case #%d:\n", test);
		doWork(test);
	}
	
	fprintf(stderr, "Total execution time %.3lf seconds.\n", (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	system("pause");
	return 0;
}
