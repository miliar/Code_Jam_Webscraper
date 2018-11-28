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
int dy1, dx1;
int dy2, dx2;

bool used[101][101];
bool valid(int y, int x)
{
	return (y>=0 && y<n && x>=0 && x<m);
}

int ff(int y, int x)
{
	used[y][x] = true;
	int res = 1;

	if (valid(y+dy1,x+dx1) && !used[y+dy1][x+dx1]) res += ff(y+dy1,x+dx1);
	if (valid(y+dy2,x+dx2) && !used[y+dy2][x+dx2]) res += ff(y+dy2,x+dx2);
	return res;
}

int main()
{
	FILE* fi = fopen("B-small.in","r");
	FILE* fo = fopen("B-small.out","w");

	fscanf(fi,"%d",&ntc);
	int sy, sx;
	int res;
	for (tc=1; tc<=ntc; tc++)
	{
		fscanf(fi,"%d %d",&m,&n);
		fscanf(fi,"%d %d",&dx1,&dy1);
		fscanf(fi,"%d %d",&dx2,&dy2);

		fscanf(fi,"%d %d",&sx,&sy);

		memset(used, 0, sizeof(used));
		res = ff(sy, sx);
		printf("Case #%d: %d\n", tc, res);
		fprintf(fo,"Case #%d: %d\n", tc, res);
	}

	fclose(fi); fclose(fo);
	return 0;
}