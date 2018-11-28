#include <iostream>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <cstdlib>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <utility>
#include <numeric>
#include <string>
#include <stack>
#include <limits>
#define MAXN 12

using namespace std;

struct coord
{
	int x, y;
};

int N, M;
static int dir[3][2] = {{-1, 0}, {0, -1}, {0, 1}};
static int dir2[3][2] = {{1, 0}, {0, -1}, {0, 1}};
static char data[MAXN][MAXN];
static char reach[MAXN][MAXN];

static map <unsigned long long, char> mem;

char CanReach (char orig[MAXN][MAXN])
{
	unsigned long long pos = 0;
	unsigned long long add = 1;
	int i, j;
	for (i = 1; i < N-1; i++)
	{
		for (j = 1; j < M-1; j++)
		{
			if (orig[i][j] == 'v') pos += add;
			add *= 2;
		}
	}
	if (mem.find(pos) != mem.end()) return 0;
	mem[pos] = 1;
	char a[MAXN][MAXN];
	int cnt = 0;
	char dirOK[3] = {1, 1, 1};
	int di, nx, ny;
	//printf("\n");
	for (i = 0; i < N; i++)
	{
		for (j = 0; j < M; j++)
		{
			//printf("%c",orig[i][j]);
			if (orig[i][j] == 'v')
			{
				cnt++;
				for (di = 0; di < 3; di++)
				{
					nx = i + dir2[di][0];
					ny = j + dir2[di][1];
					if ((orig[nx][ny] != '#') && (reach[nx][ny] != 'v')) dirOK[di] = 0;
				}
			}
		}
		//printf("\n");
	}
	if (cnt == 1) return 1;
	for (di = 0; di < 3; di++)
	{
		if (dirOK[di])
		{
			for (i = 0; i < N; i++)
			{
				for (j = 0; j < M; j++)
				{
					if (orig[i][j] == '#') a[i][j] = '#';
					else a[i][j] = '.';
				}
			}
			for (i = 0; i < N; i++)
			{
				for (j = 0; j < M; j++)
				{
					if (orig[i][j] == 'v')
					{
						nx = i + dir2[di][0];
						ny = j + dir2[di][1];
						if (orig[nx][ny] == '#') a[i][j] = 'v';
						else a[nx][ny] = 'v';
					}
				}
			}
			if (CanReach(a)) return 1;
		}
	}
	return 0;
}

int main ()
{
	int T, iT;
	scanf("%d",&T);
	static struct coord q[MAXN*MAXN];
	int r, w;
	char a[MAXN][MAXN];
	for (iT = 0; iT < T; iT++)
	{
		scanf("%d %d\n",&N,&M);
		int i, j;
		for (i = 0; i < N; i++)
		{
			scanf("%s\n",data[i]);
		}
		printf("Case #%d:\n",iT+1);
		int d;
		for (d = 0; d < 10; d++)
		{
			int x, y;
			x = -1; y = -1;
			for (i = 0; i < N; i++)
			{
				for (j = 0; j < M; j++)
				{
					if (data[i][j] == (char)(d+'0'))
					{
						x = i; y = j;
					}
				}
			}
			if (x == -1) break;
			printf("%d: ",d);
			for (i = 0; i < N; i++)
			{
				for (j = 0; j < M; j++)
				{
					if (data[i][j] == '#') a[i][j] = '#';
					else a[i][j] = '.';
				}
			}
			r = 0; w = 1;
			q[0].x = x;
			q[0].y = y;
			a[x][y] = 'v';
			while (w > r)
			{
				x = q[r].x; y = q[r].y;
				int nx, ny, di;

				for (di = 0; di < 3; di++)
				{
					nx = x + dir[di][0];
					ny = y + dir[di][1];
					if (a[nx][ny] == '.')
					{
						q[w].x = nx;
						q[w].y = ny;
						a[nx][ny] = 'v';
						w++;
					}
				}

				r++;
			}

			memcpy(reach, a, sizeof(data));

			mem = map< unsigned long long, char>();
			printf("%d ",w);
			x = q[0].x; y = q[0].y;
			if (CanReach(a)) printf("Lucky");
			else printf("Unlucky");
			printf("\n");
		}
	}
	return 0;	
}
