#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	//freopen("test.in", "w", stdout);
	int k,n,t;
	char buf;
	int m[51][51] = {0};
	int kx = 0;
	int dx[8] = {1,-1,0,0,1,-1,1,-1};
	int dy[8] = {0,0,1,-1,-1,1,1,-1};
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		scanf("%d %d ", &n, &k);
		memset(m,0,sizeof(int)* 2601);
		for (int j = 0; j < n; j++)
		{
			for (int h = 0; h < n; h++)
			{
				scanf("%c ", &buf);
				if (buf != '.')
				{
					m[j][kx] = buf;
					kx++;
				}
			}
			kx = 0;
		}
		bool r,b;
		bool rg = false,bg = false;
		int bu = 0;
		int x, y;
		int wer = n - 1;
		for (int j = 0; j < n; j++)
		{
			wer = n - 1;
			for (int h = n - 1; h >= 0; h--)
				if (m[j][h] != 0)
					swap(m[j][h], m[j][wer--]);
		}
		for (int j = 0; j < n; j++)
		{
			for (int h = 0; h < n; h++)
			{
				if (m[j][h] == 'R')
				{
					bu = m[j][h];
					r = true;
					x = h;
					y = j;
					for (int w = 0; w < 8; w++)
					{
						r = true;
						x = h;
						y = j;
						for (int q = 0; q < k - 1; q++)
						{
							if (((x + dx[w]) >= n) ||
								((x + dx[w]) < 0) ||
								((y + dy[w]) >= n) ||
								((y + dy[w]) < 0)){r = false;continue;}
							x += dx[w];
							y += dy[w];
							if (m[y][x] != bu)
							{
								r = false;
								break;
							}
						}
						if (r)
						{
							rg = true;
							break;
						}
					}
					
				}
				if (m[j][h] == 'B')
				{
					bu = m[j][h];
					b = true;
					x = h;
					y = j;
					for (int w = 0; w < 8; w++)
					{
						b = true;
						x = h;
						y = j;
						for (int q = 0; q < k - 1; q++)
						{
							if (((x + dx[w]) >= n) ||
								((x + dx[w]) < 0) ||
								((y + dy[w]) >= n) ||
								((y + dy[w]) < 0)){b = false;continue;}
							x += dx[w];
							y += dy[w];
							if (m[y][x] != bu)
							{
								b = false;
								break;
							}
						}
						if (b)
						{
							bg = true;
							break;
						}
					}
				}
			
			}
		}
			if (rg && bg)
			{
				printf("Case #%d: Both\n", i + 1);
				continue;
			}
			if (rg)
			{
				printf("Case #%d: Red\n", i + 1);
				continue;
			}
			if (bg)
			{
				printf("Case #%d: Blue\n", i + 1);
				continue;
			}
			printf("Case #%d: Neither\n", i + 1);

	}
	return 0;
}