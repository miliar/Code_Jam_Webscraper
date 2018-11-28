#include <cstdio>
#include <cstring>
#include <cstdlib>

#define abs(x) (((x) > 0) ? (x) : -(x))
#define min(a, b) (((a) > (b)) ? (b) : (a))

using namespace std;

int table[401][401];

bool go(int x, int y, int m)
{
	int cx = 200 + x, cy = 200 + y;
//	x, y를 기준으로 size m
	for (int i = -m + 1; i < m; ++i)
	{
		for (int j = -m + 1; j < m; ++j)
		{
			int xx = cx + i;
			int yy = cy + j;
			int ix = cx + cx - xx;
			int iy = cy + cy - yy;
			if (table[xx][yy] == -1) continue;
			if (table[xx][yy] != table[xx][iy] && table[xx][iy] != -1) return false;
			if (table[xx][yy] != table[ix][yy] && table[ix][yy] != -1) return false;
			if (table[xx][yy] != table[ix][iy] && table[ix][iy] != -1) return false;
		}
	}
	return true;
}

int main()
{
	int T;
	int n;
	scanf("%d", &T);
	for (int qn = 1; qn <= T; ++qn)
	{
		memset(table, -1, sizeof(table));
		scanf("%d", &n);
		int start = 201;
		for (int i = -n + 1; i < n; ++i)
		{
			int p = 0;
			if (i <= 0) 
			{
				p = n + i; 
				start--;
			}
			else 
			{
				p = n - i;
				start++;
			}
			int y = start;
			for (int j = 0; j < p; ++j)
			{
				scanf("%d", &table[200 + i][y]);
				y += 2;
			}
		}
		int ret = 9876543;
		
		for (int i = -n; i <= n; ++i)
		{
			for (int j = -n; j <= n; ++j)
			{
				int abssum = abs(i) + abs(j);
//			if (abssum >= n + 1) continue;
				if (go(i, j, n + abssum))
				{
					int add = (n + abssum) * (n + abssum) - n * n;
					ret = min(ret, add);
				}
			}
		}
		printf("Case #%d: %d\n", qn, ret);
	}
}

