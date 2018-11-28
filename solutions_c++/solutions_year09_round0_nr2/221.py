#include <stdio.h>
#include <algorithm>
using namespace std;

const int INF = 1000*1000*1000;

const int MAX_T = 100;
const int MAX_H = 100;
const int MAX_W = 100;

int map[MAX_H][MAX_W];
int tmp[MAX_H][MAX_W];
int ng[MAX_H][MAX_W][2];

char dr[30];

struct Dir { int dx, dy; };

Dir dir[4] = {{0,-1}, {-1,0}, {1,0}, {0,1}};

int nbT, h, w;

int isValid(int x, int y)
{
	if (x >= 0 && x < w && y >= 0 && y < h)
		return 1;
	return 0;
}

int isSink(int x, int y)
{
	int minA = INF;
	int md = -1;
	for (int i = 3; i >= 0; i--)
		if (isValid(x+dir[i].dx,y+dir[i].dy))
			if (map[y+dir[i].dy][x+dir[i].dx] <= minA) {
				minA = map[y+dir[i].dy][x+dir[i].dx];
				md = i;
			}
	if (minA >= map[y][x])
		return 1;
	ng[y][x][0] = x+dir[md].dx;
	ng[y][x][1] = y+dir[md].dy;
	return 0;
}

int currS = -1;
void dfs(int x, int y)
{
	if (isValid(x,y) == 0)
		return;

	if (tmp[y][x] > -1)
		return;

	tmp[y][x] = currS;
	for (int i = 0; i < 4; i++)
		if (ng[y+dir[i].dy][x+dir[i].dx][0] == x && ng[y+dir[i].dy][x+dir[i].dx][1] == y)
			dfs(x+dir[i].dx, y+dir[i].dy);
}

int main()
{
	FILE *fin = fopen("waterB.in", "r");
	FILE *fout = fopen("waterB.out","w");
	
	fscanf(fin, "%d", &nbT);
	for (int i = 0; i < nbT; i++) {
		fscanf(fin, "%d %d", &h, &w);
		for (int j = 0; j < h; j++)
			for (int k = 0; k < w; k++)
				fscanf(fin, "%d", &map[j][k]);

		int nbS = 0;
		for (int j = 0; j < h; j++)
			for (int k = 0; k < w; k++)
				tmp[j][k] = -1;

		for (int j = 0; j < h; j++)
			for (int k = 0; k < w; k++)
				if (isSink(k,j)) {
					tmp[j][k] = nbS;
					nbS++;
				}

		for (int j = 0; j < h; j++)
			for (int k = 0; k < w; k++)
				if (isSink(k,j)) {
					currS = tmp[j][k];
					tmp[j][k] = -1;
					dfs(k,j);
				}

		for (int j = 0; j < 30; j++)
			dr[j] = 0;
		int nbD = 0;
		for (int j = 0; j < h; j++)
			for (int k = 0; k < w; k++)
				if (dr[tmp[j][k]] == 0) {
					dr[tmp[j][k]] = 'a' + nbD;
					nbD++;
				}

		fprintf(fout, "Case #%d:\n", i+1);
		for (int j = 0; j < h; j++)
			for (int k = 0; k < w; k++) {
				fprintf(fout, "%c", dr[tmp[j][k]]);
				if (k == w-1)
					fprintf(fout, "\n");
				else
					fprintf(fout, " ");
			}
	}

	fclose(fin);
	fclose(fout);

	return 0;
}
