// Using libUtil from libGlov (Graphics Library of Victory) available at http://bigscreensmallgames.com/libGlov
#include "utils.h"
#include "file.h"
#include "strutil.h"
#include "assert.h"
#include "array.h"
#include <string.h>
#include <stdio.h>
#include <stdarg.h>
#include <conio.h>
#include "rand.h"
#include <vector>
using namespace std;

static int dx[] = {0, 1, 0, -1};
static int dy[] = {-1, 0, 1, 0};

static int W, H;
static int cx, cy;
bool b[15][15];
int dw[15][15];
int dc[15][15];
int didit[15][15];
struct State
{
	//int x, y;
	int predx, predy;
	int cost;
	bool inw;
	bool touched;
};
State sb[15][15];
struct {
	int x;
	int y;
} work[15*15];
int workc;

bool isw(int x, int y)
{
	if (x<0 || x>=W || y<0 || y>=H)
		return true;
	return b[x][y];
}

int getdw(int x, int y)
{
	if (x<0 || x>=W || y<0 || y>=H)
		return -1;
	return dw[x][y];
}
int getdc(int x, int y)
{
	if (x<0 || x>=W || y<0 || y>=H)
		return 1000;
	return dc[x][y];
}

int doit()
{
	while (workc)
	{
		// find min cost
		State *s = &sb[work[0].x][work[0].y];
		int si=0;
		for (int i=1; i<workc; i++) {
			if (sb[work[i].x][work[i].y].cost < s->cost) {
				s = &sb[work[i].x][work[i].y];
				si=i;
			}
		}
		int x=work[si].x;
		int y = work[si].y;
		work[si] = work[workc-1];
		workc--;
		s->inw = false;
		if (x==cx && y==cy)
			return s->cost;
		// Find all adjacent successors
		for (int i=0; i<4; i++) {
			int x2 = x + dx[i];
			int y2 = y + dy[i];
			int newc = s->cost + 1;
			if (!isw(x2, y2))
			{
				if (!sb[x2][y2].touched || 
					newc < sb[x2][y2].cost)
				{
					if (!sb[x2][y2].inw) {
						sb[x2][y2].inw = true;
						work[workc].x = x2;
						work[workc++].y = y2;
					}
					sb[x2][y2].cost = newc;
					sb[x2][y2].predx = x;
					sb[x2][y2].predy = y;
					sb[x2][y2].touched = true;
				}
			}
		}
		// Find all portal
		for (int i=0; i<4; i++) {
			int x2=x;
			int y2=y;
			while (!isw(x2, y2)) {
				x2 += dx[i];
				y2 += dy[i];
			}
			x2-=dx[i];
			y2-=dy[i];
			assert(dw[x][y]>=0);
			int newc = s->cost + dw[x][y] + 1;
			if (!sb[x2][y2].touched || 
				newc < sb[x2][y2].cost)
			{
				if (!sb[x2][y2].inw) {
					sb[x2][y2].inw = true;
					work[workc].x = x2;
					work[workc++].y = y2;
				}
				sb[x2][y2].cost = newc;
				sb[x2][y2].touched = true;
				sb[x2][y2].predx = x;
				sb[x2][y2].predy = y;
			}
		}
	}
	return -1;
}

void printit(int x, int y)
{
	if (sb[x][y].predx!=-1) {
		if (sb[x][y].predx == x && sb[x][y].predy == y)
			printf("");
		printit(sb[x][y].predx, sb[x][y].predy);
	}
	printf("%d %d c: %d\n", x, y, sb[x][y].cost);
}

char *doB(char **&toks)
{
	memset(sb, 0, sizeof(sb));
	int x0, y0;
	H = atoi(*toks++);
	W = atoi(*toks++);
	for (int i=0; i<H; i++) {
		char *r = *toks++;
		for (int j=0; j<W; j++) {
			b[j][i] = 0;
			switch( r[j])
			{
			case 'O':
				x0 = j; y0 = i;
				break;
			case 'X':
				cx = j; cy = i;
				break;
			case '#':
				b[j][i] = 1;
			}
		}
	}
	for (int i=0; i<W; i++) {
		for (int j=0; j<H; j++) {
			if (b[i][j]) {
                dw[i][j] = -1;
			} else {
				dw[i][j] = 1000;
			}
			if (i==cx && j==cy)
			{
				dc[i][j] = 0;
			} else {
				dc[i][j] = 1000;
			}
		}
	}

//	for (int j=0; j<H; j++) {
//		for (int i=0; i<W; i++) {
//			printf("%4d ", dw[i][j]);
//		}
//		printf("\n");
//	}

	for (int k=0; k<=W*H; k++) {
		for (int i=0; i<W; i++) {
			for (int j=0; j<H; j++) {
				for (int d=0; d<4; d++) {
					int x2 = i + dx[d];
					int y2 = j + dy[d];
					int dw2 = getdw(x2, y2) + 1;
					int dc2 = getdc(x2, y2) + 1;
					if (dw2 < dw[i][j])
						dw[i][j] = dw2;
					if (dc2 < dc[i][j])
						dc[i][j] = dc2;
				}
			}
		}
	}
//	for (int j=0; j<H; j++) {
//	for (int i=0; i<W; i++) {
//		printf("%2d ", dw[i][j]);
//	}
//	printf("\n");
//	}

	work[0].x = x0;
	work[0].y = y0;
	workc = 1;
	sb[x0][y0].predx = -1;
	sb[x0][y0].cost = 0;
	sb[x0][y0].touched = true;
	sb[x0][y0].inw = true;
	int r = doit();
	//if (r!=-1)
	//	printit(cx, cy);

	if (r==-1)
		return "THE CAKE IS A LIE";

	static char buf[1024];
	sprintf(buf, "%d", r);
	return buf;
}
