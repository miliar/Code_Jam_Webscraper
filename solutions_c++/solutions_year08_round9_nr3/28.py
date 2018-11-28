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

int tc, ntc;
int n, m;
int val[5][5];

bool bomb[5][5];
bool valid(int y, int x)
{
	return (y>=0 && y<n && x>=0 && x<m);
}

int res;
bool fix(int y, int x)
{
	int i, j;
	int nbomb = 0;
	for (i=-1; i<=1; i++) for (j=-1; j<=1; j++) if (valid(y+i,x+j))
		nbomb += bomb[y+i][x+j];
	if (nbomb > val[y][x]) return false;
	if (nbomb == val[y][x]) return true;
	if (nbomb == val[y][x]-1) {bomb[y+1][x+1] = true; return true;}
	return false;
}

bool ok(int y, int x)
{
	int i, j;
	int nbomb = 0;
	for (i=-1; i<=1; i++) for (j=-1; j<=1; j++) if (valid(y+i,x+j))
		nbomb += bomb[y+i][x+j];
	return nbomb == val[y][x];
}

void proc(int mask)
{
	memset(bomb, 0, sizeof(bomb));
	int i, j;
	for (i=0; i<m; i++) if (mask & (1<<i)) bomb[0][i] = true;

	for (i=1; i<n; i++) if (mask & (1<<(m+i-1))) 
	{
		bomb[i][0] = true;
	}

	for (i=0; i<n-1; i++) for (j=0; j<m-1; j++)
	{
		if (!fix(i,j)) return;
	}

	for (i=0; i<n; i++) for (j=0; j<m; j++) if (!ok(i,j)) return;
	int tres = 0;
	int r = n/2;
	for (i=0; i<m; i++) tres += bomb[r][i];
	if (tres > res) res = tres;
}

int main()
{
	FILE* fi = fopen("C-small.in","r");
	FILE* fo = fopen("C-small.out","w");

	fscanf(fi,"%d",&ntc);
	int i, j;
	int k;
	for (tc=1; tc<=ntc; tc++)
	{
		fscanf(fi,"%d %d",&n,&m);
		for (i=0; i<n; i++) for (j=0; j<m; j++) fscanf(fi,"%d",&val[i][j]);

		k = n+m-1;
		res = -1000;

		for (i=0; i<(1<<k); i++)
		{
			proc( i );
		}

		printf("Case #%d: %d\n", tc, res);
		fprintf(fo, "Case #%d: %d\n", tc, res);
	}

	fclose(fi); fclose(fo);
	return 0;
}


