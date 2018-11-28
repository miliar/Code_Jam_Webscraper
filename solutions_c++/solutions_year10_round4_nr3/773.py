#include <iostream>
using namespace std;
int map[101][101];
int temp[101][101];
int main()
{
	int t, i, j, n, m, cas = 0, r, k;
	int x1, x2, y1, y2;
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	scanf("%d", &t);
	while(t--)
	{
		int res = 0;
		memset(map, 0, sizeof(map));
		scanf("%d", &r);
		for(i = 0; i < r; i ++)
		{
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for(j = x1;  j <= x2 ; j ++)
			{
				for(k = y1; k <= y2; k ++)
					map[j][k] = 1;
			}
		}
		while(1)
		{
			bool flag = 0;
			for(i = 1; i <= 100 ; i ++)
			{
				for(j = 1; j <= 100; j ++)
				{
					if(!map[i][j] && map[i-1][j] && map[i][j-1])
						temp[i][j] = 1;
					else if(map[i][j] == 1 && !(map[i-1][j] || map[i][j-1]))
						temp[i][j] = 0;
					else temp[i][j] = map[i][j];
				}
			}
			for(i = 1; i <= 100; i ++)
			{
				for(j = 1; j <= 100; j ++)
				{
					map[i][j] = temp[i][j];
					if(map[i][j] == 1)
						flag = 1;
				}
			}
			res ++;
			if(!flag)
				break;
		}
		printf("Case #%d: %d\n", ++cas, res);
	}
}