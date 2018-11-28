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

#define MAX 65536
#define MAX_COORD 4096
#define HALF 2048

using namespace std;
FILE *in; FILE *out;

struct Point
{
	int x, y;
	
};

int n, m;
char path[MAX]; int len;
// North, East, South, West
int d[4][2] = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };

int cnt;
Point a[MAX][2];

int blen;
char buff[128];
char vis[MAX_COORD][MAX_COORD];

int op[MAX], cl[MAX];

void doWork(int testNum)
{
	int i, c, j;
	int minn, maxx, cur;
	int minrow, maxrow, mincol, maxcol;
	int row, col, dir, ans = 0;
	
	memset(vis, 0, sizeof(vis));
	memset(path, 0, sizeof(path));
	row = HALF; col = HALF; dir = 0; len = 0;

	fscanf(in, "%d", &n);
	for (i=0; i<n; i++)
	{
		fscanf(in, "%s %d", buff, &m);
		blen = (int)strlen(buff);
		
		for (c=0; c<m; c++)
			for (j=0; j<blen; j++) path[len++] = buff[j];
	}
	
	cur = 0; cnt = 0;
	while (cur < len)
	{
		if (path[cur] == 'F')
		{
			int count = 0;
			while (path[cur] == 'F' && cur < len) {count++; cur++;}
			a[cnt][0].x = row; a[cnt][0].y = col;
			row += count * d[dir][0];
			col += count * d[dir][1];
			a[cnt][1].x = row; a[cnt][1].y = col;
			cnt++;
		}
		else
		{
			if (path[cur] == 'R') {dir++; if (dir > 3) dir = 0;}
			if (path[cur] == 'L') {dir--; if (dir < 0) dir = 3;}
			cur++;
		}
	}
	
//	for (i=0; i<cnt; i++)
//		fprintf(out, "Line from (%d, %d) to (%d, %d)\n", a[i][0].x, a[i][0].y, a[i][1].x, a[i][1].y);
	
	// Horizontal
	memset(op, 0, sizeof(op));
	memset(cl, 0, sizeof(cl));
	
	minrow = MAX_COORD; maxrow = -MAX_COORD;
	mincol = MAX_COORD; maxcol = -MAX_COORD;

	for (i=0; i<cnt; i++)
	{
		minrow = min(minrow, a[i][0].x); maxrow = max(maxrow, a[i][0].x);
		minrow = min(minrow, a[i][1].x); maxrow = max(maxrow, a[i][1].x);
		
		mincol = min(mincol, a[i][0].y); maxcol = max(maxcol, a[i][0].y);
		mincol = min(mincol, a[i][1].y); maxcol = max(maxcol, a[i][1].y);

		if (a[i][0].x == a[i][1].x)
			for (c=min(a[i][0].y, a[i][1].y); c<max(a[i][0].y, a[i][1].y); c++) op[c]++;
	}
	
	for (i=minrow; i<=maxrow; i++)
	{
		for (j=0; j<cnt; j++)
		{
			if (a[j][0].x == i && a[j][0].x == a[j][1].x)
			{
				for (c=min(a[j][0].y, a[j][1].y); c<max(a[j][0].y, a[j][1].y); c++) {cl[c]++; op[c]--;}
			}
		}
		
		for (c=mincol; c<=maxcol; c++)
			if (cl[c] > 0 && cl[c] % 2 == 0 && op[c] > 0)
			{
				ans++;
				vis[i][c] = 1;
			}
	}
	
	// Vertical
	memset(op, 0, sizeof(op));
	memset(cl, 0, sizeof(cl));
	
	minrow = MAX_COORD; maxrow = -MAX_COORD;
	mincol = MAX_COORD; maxcol = -MAX_COORD;

	for (i=0; i<cnt; i++)
	{
		minrow = min(minrow, a[i][0].x); maxrow = max(maxrow, a[i][0].x);
		minrow = min(minrow, a[i][1].x); maxrow = max(maxrow, a[i][1].x);
		
		mincol = min(mincol, a[i][0].y); maxcol = max(maxcol, a[i][0].y);
		mincol = min(mincol, a[i][1].y); maxcol = max(maxcol, a[i][1].y);

		if (a[i][0].y == a[i][1].y)
			for (c=min(a[i][0].x, a[i][1].x); c<max(a[i][0].x, a[i][1].x); c++) op[c]++;
	}
	
	for (i=mincol; i<=maxcol; i++)
	{
		for (j=0; j<cnt; j++)
		{
			if (a[j][0].y == i && a[j][0].y == a[j][1].y)
			{
				for (c=min(a[j][0].x, a[j][1].x); c<max(a[j][0].x, a[j][1].x); c++) {cl[c]++; op[c]--;}
			}
		}
		
		for (c=minrow; c<=maxrow; c++)
			if (cl[c] > 0 && cl[c] % 2 == 0 && op[c] > 0 && vis[c][i] == 0)
			{
				ans++;
			}
	}

	fprintf(out, "%d\n", ans);
	return;
}

int main(void)
{
	int tests, i;
	
	in = fopen("Pockets.in", "rt");
	out = fopen("Pockets.out", "wt");
	
	fscanf(in, "%d", &tests);
	for (i=0; i<tests; i++)
	{
		fprintf(out, "Case #%d: ", i+1);
		doWork(i + 1);
	}
	
	return 0;
}
