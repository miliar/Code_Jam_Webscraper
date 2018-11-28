#include <iostream>
#include <cctype>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <map>
#include <set>

#define MAX 10002
using namespace std;
FILE *in; FILE *out;

int n;
int a[MAX][3];
char cov[MAX];
set <int> used;
map <string, int> q; int cnt;


int getCol(string col)
{
	if (q.find(col) == q.end())
		q[col] = cnt++;

	return q[col];
}

void doWork(void)
{
	int i, c, j;
	int ans = MAX;
	char buff[128];
	
	q.clear(); cnt = 0;
	fscanf(in, "%d", &n);
	
	for (i=0; i<n; i++)
	{
		fscanf(in, "%s", buff);
		fscanf(in, "%d %d", &a[i][0], &a[i][1]);	
		a[i][2] = getCol(buff);
	}
	
	for (i=0; i<(1 << n); i++)
	{
		if (__builtin_popcount(i) > ans) continue;
		
		used.clear();
		memset(cov, 0, sizeof(cov));

		for (c=0; c<n; c++) if (i & (1 << c))
		{
			for (j=a[c][0]; j<=a[c][1]; j++)
				cov[j] = 1;
			
			used.insert(a[c][2]);
		}
		if (used.size() > 3) continue;

		int flag = 1;
		for (c=1; c<=10000; c++) if (cov[c] == 0) {flag = 0; break;}
		if (flag == 0) continue;

		ans = __builtin_popcount(i);
	}
	
	if (ans >= MAX) fprintf(out, "IMPOSSIBLE\n");
	else fprintf(out, "%d\n", ans);
	return;
}



int main(void)
{
	int t, tests;
	
	in = fopen("PaintingAFence.in", "rt");
	out = fopen("PaintingAFence.out", "wt");
	
	fscanf(in, "%d", &tests);
	for (t=1; t<=tests; t++)
	{
		fprintf(out, "Case #%d: ", t);
		doWork();
	}
	
	fclose(in); fclose(out);
    return 0;
}
