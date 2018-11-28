#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

char a[6100][6100];

int main()
{
	int Cases;
	scanf("%d", & Cases);
	for (int Case = 0; Case < Cases; Case++)
	{
		memset(a, 0, sizeof a);
		int L;
		scanf("%d", &L);
		int x = 3050;
		int y = 3050;
		int x1 = x, x2 = x, y1 = y, y2 = y;
		int d = 0;
		int dx[4] = {0, +1, 0, -1};
		int dy[4] = {1, 0, -1, 0};
		for (int i = 0; i < L; i++)
		{
			char s[50];
			int rep;
			scanf(" %[^ ]%d", s, & rep);
			for (int j = 0; j < rep; j++)
			{
				int n = (int) strlen(s);
				for (int k = 0; k < n; k++)
				{
					switch (s[k])
					{
					case 'L': d = (d + 3) % 4; break;
					case 'R': d = (d + 1) % 4; break;
					case 'F':
						switch (d)
						{
						case 0: a[x][y] |= 2; y++; break;
						case 1: a[x][y] |= 1; x++; break;
						case 2: y--; a[x][y] |= 2; break;
						case 3: x--; a[x][y] |= 1; break;
						}
					}
					x1 = min(x1, x);
					x2 = max(x2, x);
					y1 = min(y1, y);
					y2 = max(y2, y);
				}
			}
		}

		for (x = x1; x <= x2; x++)
		{
			int q = 0, w = 0;
			for (y = y1; y <= y2; y++)
			{
				if (a[x][y] & 1)
				{
					if (q == 0 && w > 0)
					{
						for (int yy = w; yy < y; yy++)
							a[x][yy] |= 4;
					}
					q = 1 - q;
					w = y;
				}
			}
		}


		for (y = y1; y <= y2; y++)
		{
			int q = 0, w = 0;
			for (x = x1; x <= x2; x++)
			{
				if (a[x][y] & 2)
				{
					if (q == 0 && w > 0)
					{
						for (int xx = w; xx < x; xx++)
							a[xx][y] |= 4;
					}
					q = 1 - q;
					w = x;
				}
			}
		}

		int z = 0;
		for (x = x1; x < x2; x++)
			for (y = y1; y < y2; y++)
				z += ((a[x][y] & 4) != 0);

		printf("Case #%d: %d\n", Case + 1, z);
	}
	return 0;
}
