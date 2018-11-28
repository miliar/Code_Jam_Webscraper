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

#define MAX 16
#define MASK 1024

using namespace std;
FILE *in; FILE *out;

int n, m;
char a[MAX][MAX];
int dyn[MAX][MASK];


int recurse(int row, int mask)
{
	int i, c;
	int tmp, ans = 0;
	
	if (row >= n) return 0;
	if (dyn[row][mask] != -1) return dyn[row][mask];

	for (i=0; i<(1 << m); i++)
	{
		int last = 0, flag = 1;
		for (c=0; c<m; c++)
			if (i & (1 << c))
			{
				if (a[row][c] == 'x') {flag = 0; break;}
				if (last) {flag = 0; break;}
				else last = 1;
			}
			else last = 0;
		
		if (!flag) continue;
		
		for (c=0; c<m; c++) if (i & (1 << c))
		{
			if (c > 0) if (mask & (1 << c-1)) {flag = 0; break;}
			if (c < m) if (mask & (1 << c+1)) {flag = 0; break;}
		}
		if (!flag) continue;
		
		tmp = __builtin_popcount(i);
		tmp += recurse(row+1, i);
		ans = max(ans, tmp);
	}
	
	dyn[row][mask] = ans;
	return ans;
}

void doWork(int testNum)
{
	int i, c;
	int ans = 0;
	
	fscanf(in, "%d %d", &n, &m);
	for (i=0; i<n; i++) fscanf(in, "%s", a[i]);
	
	memset(dyn, -1, sizeof(dyn));
	ans = recurse(0, 0);
	
	fprintf(out, "%d\n", ans);
	return;
}

int main(void)
{
	int tests, i;
	
	in = fopen("NoCheating.in", "rt");
	out = fopen("NoCheating.out", "wt");
	
	fscanf(in, "%d", &tests);
	for (i=0; i<tests; i++)
	{
		fprintf(out, "Case #%d: ", i+1);
		doWork(i + 1);
	}
	
	return 0;
}
