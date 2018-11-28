#include <stdio.h>

#define max(a, b) a > b ? a : b
#define min(a, b) a < b ? a : b
#define fr(i, n) for(i = 0; i < n; i++)
#define frd(i, n) for(i = n-1; i >= 0; i--)
#define lo(i, a, b) for(i = a; i < b; i++)
#define lod(i, a, b) for(i = a; i > b; i--)

#define pb push_back

#define Eps 1e-09
#define Inf 0x7fffffff

FILE *inf = fopen("D.in", "r"), *outf = fopen("D.out", "w");

int H, W, R, An;
int map[ 200][ 200];
int Mod = 10007;

void plus(int x, int y, int pl)
{
	if(map[x][y] == -1)
		return;

	map[x][y] = (map[x][y] + pl) % Mod;
}

void input()
{
	int i, j;
	int x, y;
	fscanf(inf, "%d%d%d", &H, &W, &R);

	fr(i, H)
	{
		fr(j, W)
			map[i][j] = 0;
	}

	map[0][0] = 1;

	fr(i, R)
	{
		fscanf(inf, "%d%d", &x, &y);
		x--, y--;
		map[x][y] = -1;
	}

	An = 0;

	fr(i, H)
	{
		fr(j, W)
		{
			if(map[i][j] > 0)
			{
				plus(i+2, j+1, map[i][j]);
				plus(i+1, j+2, map[i][j]);
			}
		}
	}

	if(map[H-1][W-1] < 0)
		map[H-1][W-1] = 0;
}

void output(int x)
{
	fprintf(outf, "Case #%d: %d\n", x, map[H-1][ W-1]);
}

int main()
{
	int i, T;
	fscanf(inf, "%d", &T);

	fr(i, T)
	{
		input();
		output(i+1);
	}
	return 0;
}