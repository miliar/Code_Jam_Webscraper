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
char mm[50][50];

int n, m;
int dy[] = {-1,0,1,0};
int dx[] = {0,1,0,-1};
bool valid(int y, int x)
{
	return (y>=0 && y<n && x>=0 && x<m);
}


int val[50][50];
int py[50][50], px[50][50];

int nq;
int qy[1000], qx[1000];
int oy, ox;

int val2[50][50];

void bfs(int y, int x, int val[50][50])
{
	int i, j;
	for (i=0; i<n; i++) for (j=0; j<m; j++) val[i][j] = -1;

	nq = 1;
	qy[0] = y;
	qx[0] = x;
	val[y][x] = 0;

	int it;
	int ny, nx;
	for (it=0; it<nq; it++)
	{
		y = qy[it];
		x = qx[it];
		for (i=0; i<4; i++)
		{
			ny = y + dy[i];
			nx = x + dx[i];
			if (valid(ny,nx) && mm[ny][nx] != '.' && val[ny][nx] == -1)
			{
				val[ny][nx] = val[y][x] + 1;
				qy[nq] = ny;
				qx[nq] = nx;

				py[ny][nx] = y;
				px[ny][nx] = x;
				nq++;
			}
		}
	}
}

bool must[50][50];

void trace(int y, int x)
{
	int ny, nx;
	while (y || x)
	{
		must[y][x] = true;
		ny = py[y][x];
		nx = px[y][x];
		y = ny; x = nx;
	}
	must[y][x] = true;
}

int main()
{
	FILE* fi = fopen("D-small.in","r");
	FILE* fo = fopen("D-small.out","w");

	fscanf(fi,"%d",&ntc);
	int res;
	int i, j;
	for (tc=1; tc<=ntc; tc++)
	{
		fscanf(fi,"%d %d",&n,&m);
		for (i=0; i<n; i++)
			fscanf(fi,"%s", mm[i]);
		// go to the other forest

		for (i=0; i<n; i++) for (j=0; j<m; j++) if (mm[i][j] == 'T') {oy=i; ox=j;}

		memset(must, 0, sizeof(must));
		bfs(0, 0, val);
		trace(oy, ox);
		bfs(oy, ox, val2);

		res = 0;
		for (i=0; i<n; i++) for (j=0; j<m; j++) if (mm[i][j] != '.')
		{
			if (must[i][j]) res += val[i][j];
			else res += min(val[i][j], val2[i][j]);
		}

		fprintf(fo, "Case #%d: %d\n", tc, res);
		printf("Case #%d: %d\n", tc, res);
	}


	fclose(fi); fclose(fo);
	return 0;
}