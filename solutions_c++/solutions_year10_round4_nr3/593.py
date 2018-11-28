#include <stdio.h>
#include <string.h>

int main()
{
	int cas , n , res;
	int a[105][105] , b[105][105];

	freopen("C-small-attempt0.in" , "r" , stdin);
	freopen("C-small-attempt0.out" , "w" , stdout);
	scanf("%d" , &cas);
	for (int t = 1; t <= cas; t ++)
	{
		scanf("%d" , &n);
		memset(a , 0 , sizeof(a));
		memset(b , 0 , sizeof(b));
		for (int k = 0; k < n; k ++)
		{
			int x1 , y1 , x2 , y2;
			scanf("%d %d %d %d" , &x1 , &y1 , &x2 , &y2);
			for (int j = x1; j <= x2; j ++)
				for (int i = y1; i <= y2; i ++)
					a[i][j] = 1;
		}
		res = 0;
		while (1)
		{
			int ok = 1;
			for (int i = 1; i <= 100; i ++)
				for (int j = 1; j <= 100; j ++)
				{
					if (a[i][j] == 1)
					{
						ok = 0;
						if (a[i-1][j] + a[i][j-1] > 0) b[i][j] = 1;
						else b[i][j] = 0;
					}
					else
					{
						if (a[i-1][j] + a[i][j-1] == 2) b[i][j] = 1;
						else b[i][j] = 0;
					}
				}
			if (ok) break;
			res ++;
			for (int i = 1; i <= 100; i ++)
				for (int j = 1; j <= 100; j ++) a[i][j] = b[i][j];
		}
		printf("Case #%d: %d\n" , t , res);
	}
	return 0;

}