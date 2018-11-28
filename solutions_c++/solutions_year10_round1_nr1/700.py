#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

char b[60][60], m[60][60];
int n, k, sc[5];
int dy[] = {-1, 0, 1, 1};
int dx[] = {1, 1, 1, 0};

bool in(int y, int x)
{
	return y >= 0 && y < n && x >= 0 && x < n;
}

void solve()
{
	memset(m, 0, sizeof(m));
	sc[0] = sc[1] = 0;
	for (int y = 0; y < n; y++)
	{
		for (int x = 0; x < n; x++)
		{
			m[x][n-1-y] = b[y][x];
		}
	}
/*	
	puts("\n");
	for (int y = 0; y < n; y++)
		puts(m[y]);
	puts("\n");
*/
	
	for (int y = n - 1; y >= 0; y--)
	{
		for (int x = 0; x < n; x++)
		{
			if (m[y][x] != '.')
				continue;
			int tmp = y - 1;
			while (tmp >= 0 && m[tmp][x] == '.')
				tmp--;
			if (tmp >= 0)
				swap(m[tmp][x], m[y][x]);
		}
	}		

/*
	puts("\n");
	for (int y = 0; y < n; y++)
		puts(m[y]);
	puts("\n");
*/
	
	for (int y = 0; y < n; y++)
	{
		for (int x = 0; x < n; x++)
		{
			for (int i = 0; i < 4; i++)
			{
				if (m[y][x] != '.')
				{
					int ty = y, tx = x;
					while (in(ty + dy[i], tx + dx[i]) && m[ty + dy[i]][tx + dx[i]] == m[y][x])
					{
						ty = ty + dy[i];
						tx = tx + dx[i];
					}
//					printf("%d,%d %d,%d\n", y, x, ty, tx);
					sc[m[y][x] == 'R'] = max(sc[m[y][x] == 'R'], 1+max(abs(ty-y), abs(tx-x)));
				}
			}
		}
	}
//	printf("%d -- %d\n", sc[0], sc[1]);
	if (sc[0] >= k && sc[1] >= k)
		puts("Both");
	else if (sc[0] >= k && sc[1] < k)
		puts("Blue");
	else if (sc[0] < k && sc[1] >= k)
		puts("Red");
	else if (sc[0] < k && sc[1] < k)
		puts("Neither");
}

int main()
{
	int tc;
	scanf("%d", &tc);
	for (int i = 1; i <= tc; i++)
	{
		scanf("%d %d", &n, &k);
		for (int j = 0; j < n; j++)
			scanf("%s", b[j]);
		printf("Case #%d: ", i);	
		solve();
	}
	return 0;
}
