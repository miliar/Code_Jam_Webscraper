#include <stdio.h>
#include <string.h>

int main()
{
int cas;
int a[300][300];
int h , v , k;

	freopen("A-large.in" , "r" , stdin);
	freopen("A-large.out" , "w" , stdout);

	scanf("%d" , &cas);
	for (int t = 1; t <= cas; t ++)
	{
		scanf("%d" , &k);
		memset(a , 0 , sizeof(a));
		for (int i = 1; i <= k; i ++)
		{
			int n = 1;

			for (int j = 1; j <= k - i; j ++) a[i][n++] = -1;
			
			for (int j = 1; j <= i; j ++)
			{
				scanf("%d" , &a[i][n++]);
				if (j < i) a[i][n++] = -1;	//add space
			}
			for (int j = 1; j <= k - i; j ++) a[i][n++] = -1;
		}
		for (int i = k + 1; i < 2 * k; i ++)
		{
			int n = 1;
			for (int j = 1; j <= i - k; j ++) a[i][n++] = -1;
			for (int j = 1; j <= 2 * k - i; j ++)
			{
				scanf("%d" , &a[i][n++]);
				if (j < 2 * k - i) a[i][n++] = -1;
			}
			for (int j = 1; j <= i - k; j ++) a[i][n++] = -1;
		}
		//2k-1 * 2k-1
		//from centre to find zhou
		int ok;
		for (v = k; v >= 1; v --)
		{
			for (int z = 0; z <= 1; z ++)
			{
				int x;
				if (z == 0) x = v;
				else x = 2 * k - v;
				ok = 1;
				int i = 0;
				while (1)
				{
					i ++;
					int i1 = x - i;
					int i2 = x + i;
					if (i1 < 1 || i2 > 2 * k - 1) break;
					for (int j = 1; j <= 2 * k - 1; j ++)
						if (a[i1][j] != -1 && a[i2][j] != -1)
						{
							if (a[i1][j] != a[i2][j]) {ok = 0; break;}
						}
					if (ok == 0) break;
				}
				if (ok == 1) { v = x; break; }
			}
			if (ok == 1) break;
		}
		for (h = k; h >= 1; h --)
		{
			for (int z = 0; z <= 1; z ++)
			{
				int x;
				if (z == 0) x = h;
				else x = 2 * k - h;
				ok = 1;
				int j = 0;
				while (1)
				{
					j ++;
					int j1 = x - j;
					int j2 = x + j;
					if (j1 < 1 || j2 > 2 * k - 1) break;
					for (int i = 1; i <= 2 * k - 1; i ++)
						if (a[i][j1] != -1 && a[i][j2] != -1)
						{
							if (a[i][j1] != a[i][j2]) {ok = 0; break;}
						}
					if (ok == 0) break;
				}
				if (ok == 1) { h = x; break; }
			}
			if (ok == 1) break;
		}
		if (h > k) h = 2 * k - h;
		if (v > k) v = 2 * k - v;
		int r = k + 2 * k - v - h;
		printf("Case #%d: %d\n" , t , r * r - k * k);
	}
	return 0;
}