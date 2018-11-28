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

#define MAX 1024
#define MOD 10007
#define DYN 128

using namespace std;
FILE *in; FILE *out;

int h, w, r;
int a[MAX][2];
int dyn[DYN][DYN];

int recurse(int row, int col)
{
	int i;
	int flag, ans = 0;
	
	if (dyn[row][col] != -1) return dyn[row][col];
	if (row > h || col > w) return 0;
	if (row == h && col == w) return 1;
	
	flag = 1;
	for (i=0; i<r; i++) if ((a[i][0] == row + 1) && (a[i][1] == col + 2)) {flag = 0; break;}
	if (flag) ans += recurse(row + 1, col + 2);
	
	flag = 1;
	for (i=0; i<r; i++) if ((a[i][0] == row + 2) && (a[i][1] == col + 1)) {flag = 0; break;}
	if (flag) ans += recurse(row + 2, col + 1);
	
	ans %= MOD;
	dyn[row][col] = ans;
	return ans;
}


void doWork(int testNum)
{
	int i, c;
	int ans = 0;

	fscanf(in, "%d %d %d", &h, &w, &r);
	for (i=0; i<r; i++) fscanf(in, "%d %d", &a[i][0], &a[i][1]);
	
	memset(dyn, -1, sizeof(dyn));
	ans = recurse(1, 1);
	
	fprintf(out, "%d\n", ans);	
	return;
}

int main(void)
{
	int tests, i;
	
	in = fopen("EndlessKnight.in", "rt");
	out = fopen("EndlessKnight.out", "wt");
	
	fscanf(in, "%d", &tests);
	for (i=0; i<tests; i++)
	{
		fprintf(out, "Case #%d: ", i+1);
		doWork(i + 1);
	}
	
	return 0;
}
