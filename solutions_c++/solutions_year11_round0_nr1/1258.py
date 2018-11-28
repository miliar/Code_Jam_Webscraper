#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>

#define MAX 128

using namespace std;
FILE *in; FILE *out;

struct State
{
	int idx1, idx2, cur;
};

int n;
int a[MAX][2];
queue <State> q;
int dir[3] = {-1, 0, +1};
int vis[MAX][MAX][MAX], steps[MAX][MAX][MAX];

int bfs()
{
	State cur, nxt;
	memset(vis, 0, sizeof(vis));
	while (!q.empty()) q.pop();
	
	nxt.idx1 = 1; nxt.idx2 = 1; nxt.cur = 0;
	q.push(nxt);
	vis[nxt.idx1][nxt.idx2][nxt.cur] = 1;
	steps[nxt.idx1][nxt.idx2][nxt.cur] = 0;
	
	while (!q.empty())
	{
		cur = q.front(); q.pop();
		if (cur.cur >= n) return steps[cur.idx1][cur.idx2][cur.cur];

		for (int i = 0; i < 3; i++)
		{
			nxt.cur = cur.cur;
			nxt.idx1 = cur.idx1 + dir[i]; if (nxt.idx1 < 1 || nxt.idx1 > 100) continue;
			if (i == 1 && a[cur.cur][0] == 0 && a[cur.cur][1] == nxt.idx1)
				nxt.cur = cur.cur + 1;
			
			for (int c = 0; c < 3; c++)
			{
				nxt.idx2 = cur.idx2 + dir[c]; if (nxt.idx2 < 1 || nxt.idx2 > 100) continue;
				if (c == 1 && a[cur.cur][0] == 1 && a[cur.cur][1] == nxt.idx2)
					nxt.cur = cur.cur + 1;
				if (vis[nxt.idx1][nxt.idx2][nxt.cur] == 0)
				{
					vis[nxt.idx1][nxt.idx2][nxt.cur] = 1;
					steps[nxt.idx1][nxt.idx2][nxt.cur] = steps[cur.idx1][cur.idx2][cur.cur] + 1;
					q.push(nxt);
				}
				if (c == 1 && a[cur.cur][0] == 1 && a[cur.cur][1] == nxt.idx2)
					nxt.cur = cur.cur;
			}
		}
	}
	return -1;
}

void doWork(int testNum)
{
	fscanf(in, "%d", &n);
	for (int i = 0; i < n; i++)
	{
		char buff[32]; int where;
		fscanf(in, "%s %d", buff, &where);
		a[i][0] = ((buff[0] == 'O') ? 0 : 1);
		a[i][1] = where;
	}
	fprintf(out, "%d\n", bfs());
}

int main(void)
{
	unsigned sTime = clock();
	in = fopen("BotTrust.in", "rt");
	out = fopen("BotTrust.out", "wt");
	
	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++)
	{
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d: ", test);
		doWork(test);
	}
	
	fprintf(stderr, "Total execution time %.3lf seconds.\n", (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	system("pause");
	return 0;
}
