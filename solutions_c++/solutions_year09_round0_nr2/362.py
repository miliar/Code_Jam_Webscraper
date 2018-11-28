#include<stdio.h>
#include<algorithm>
using namespace std;

int f[10500], h, w;
int dy[] = {-1, 0, 0, 1};
int dx[] = {0, -1, 1, 0};
int v[110][110];
char ans[110][110];



int fp(int x)
{
	return x == f[x] ? x : f[x] = fp(f[x]);
}

bool in(int y, int x)
{
	return y >= 0 && y < h && x >= 0 && x < w;
}

void con(int x, int y)
{
	fp(x);
	fp(y);
	if (f[x] > f[y])
		f[f[x]] = f[y];
	else
		f[f[y]] = f[x];
}

void solve()
{
	int ty, tx;
	for (int i = 0; i < 10500; i++)
		f[i] = i;
	for (int y = 0; y < h; y++)
	{
		for (int x = 0; x < w; x++)
		{
			int minv = 2000000000, I;
			for (int i = 0; i < 4; i++)
			{
				ty = y + dy[i];
				tx = x + dx[i];
				if (!in(ty, tx) || v[ty][tx] >= v[y][x])
					continue;
				if (v[ty][tx] < minv)
				{
					minv = v[ty][tx];
					I = ty*w+tx;
				}
			}
			if (minv < 2000000000)
			{
				con(I, y*w+x);
//				printf("%d %d -- %d %d\n", y, x, I/w, I%w);
			}
		}
	}
	for (int y = 0; y < h; y++)
	{
		for (int x = 0; x < w; x++)
		{
			fp(y*w+x);
		}
	}
	char cnt = 'a';
	int tmp;
	for (int y = 0; y < h; y++)
	{
		for (int x = 0; x < w; x++)
		{
			if (f[y*w+x] == y*w+x)
			{
				ans[y][x] = cnt;
				cnt++;
			}
			else
			{
				tmp = f[y*w+x]; 
				ans[y][x] = ans[tmp/w][tmp%w];
			}
			printf("%c%c", ans[y][x], x<w-1?' ':'\n');
//			printf("%d%d%c%c", f[y*w+x], y*w+x, ans[tmp/w][tmp%w], x<w-1?' ':'\n');
		}
	}
}	

int main()
{
	int tc;
	scanf("%d", &tc);
	for (int i = 1; i <= tc; i++)
	{
		scanf("%d %d", &h, &w);
		for (int y = 0; y < h; y++)
		{
			for (int x = 0; x < w; x++)
			{
				scanf("%d", &v[y][x]);
			}
		}
		printf("Case #%d:\n", i);
		solve();
	}
	return 0;
}
