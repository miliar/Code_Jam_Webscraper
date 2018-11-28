#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <math.h>
#include <map>
#include <set>
#include <algorithm>
using namespace std;


typedef vector <int> vi;
typedef vector <string> vs;
typedef pair <int,int> pii;
typedef vector <double> vd;

char mm[20][20];
int tc, ntc;
int n, m;

int dp[15][15][1<<15][2];

int doit(int y, int x, int mask, bool left)
{
	if (y == n) return 0;
	if (x == m) return doit(y+1, 0, mask, 0);

	int& res = dp[y][x][mask][left];
	if (res != -1) return res;

	res = 0;
	int tmp;
	if (mm[y][x] == '.' || mm[y][x] == '?')
	{
		res = max(res, doit(y, x+1, mask & ~(1<<x), 0));
	}

	if (mm[y][x] == '#' || mm[y][x] == '?')
	{
		tmp = 4;
		if (left) tmp -= 2;
		if (mask & (1<<x)) tmp -= 2;
		res = max(res, tmp + doit(y, x+1, mask | (1<<x), 1));
	}

	return res;
}

int main()
{
	FILE* fi = fopen("E-small.in","r");
	FILE* fo = fopen("E-small.out","w");

	fscanf(fi,"%d",&ntc);
	int i, j;
	int res;
	for (tc=1; tc<=ntc; tc++)
	{
		fscanf(fi,"%d %d",&n,&m);
		for (i=0; i<n; i++) fscanf(fi,"%s", mm[i]);

		memset(dp, -1, sizeof(dp));
		res = doit(0, 0, 0, 0);

		printf("Case #%d: %d\n", tc, res);
		fprintf(fo, "Case #%d: %d\n", tc, res);
	}

	fclose(fi); fclose(fo);
	return 0;
}