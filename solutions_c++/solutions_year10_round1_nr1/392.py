#include <stdio.h>

int main()
{
	freopen("A-large.in" , "r" , stdin);
	freopen("A-large.out" , "w" , stdout);
	int t ,cas;
	int n , k;
	int a[70][70];
	int b[70][70];
	char row[70];
	int ok , rr , bb , x , y;
	int p[4][2] = {{1 , 0} , {0 , 1} , {1 , 1} , {-1 , 1}};

	scanf("%d" , &t);
	for (cas = 1; cas <= t; cas ++)
	{
		scanf("%d %d" , &n , &k);
		for (int i = 0; i < n; i ++)
		{
			scanf("%s" , row);
			for (int j = 0; j < n; j ++)
				if (row[j] == '.') a[i][j] = 0;
				else if (row[j] == 'R') a[i][j] = 1;
				else a[i][j] = 2;
		}
		printf("Case #%d: " , cas);
		for (int i = 0; i < n; i ++)
			for (int j = 0; j < n; j ++)
				b[j][n-i-1] = a[i][j];
		for (int j = 0; j < n; j ++)
		{
			int i = n-1;
			int x = n-1;
			while (x >= 0)
			{
				if (b[x][j] > 0) b[i--][j] = b[x][j];
				x --;
			}
			while (i >= 0) b[i--][j] = 0;
		}

		rr = 0; bb = 0;
		for (int i = 0; i < n; i ++)
			for (int j = 0; j < n; j ++)
				if (b[i][j] > 0)
				{
					for (int h = 0; h < 4; h ++)
					{
						ok = b[i][j];
						if ((i + p[h][0] * k <= n) && (j + p[h][1] * k <= n)
							&& (i + p[h][0] * k >= -1) && (j + p[h][1] * k >= -1))
						{
							x = i; y = j;
							for (int z = 1; z < k; z ++)
							{
								x += p[h][0];
								y += p[h][1];
								if (b[x][y] != ok) {ok = -ok; break;}
							}
						}
						else {ok = -ok;}

						if (ok == 1) rr = 1;
						else if (ok == 2) bb = 1;
					}
				}
		if (rr == 0 && bb == 0) printf("Neither\n");
		else if (rr == 1 && bb == 1) printf("Both\n");
		else if (rr == 1) printf("Red\n");
		else printf("Blue\n");
	}
	return 0;
}