#include <stdio.h>
#include <string.h>

int a[150][150];
int main(void)
{
	int t, n, m, i, j, k, p, x, y, l, test = 0;
	bool flag;
	char c[50];
	int d[150];
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &t);
	while(t --)
	{
		scanf("%d %d", &m, &n);
		k = n / 4;
		for(i = 0;i < m;i ++)
		{
			scanf("%s", c);
			for(j = 0;j < k;j ++)
			{
				if(c[j] >= '0' && c[j] <= '9')
					p = c[j] - 48;
				else
					p = c[j] - 65 + 10;
				a[i][j * 4] = p / 8;
				if(p > 7)
					p -= 8;
				a[i][j * 4 + 1] = p / 4;
				if(p > 3)
					p -= 4;
				a[i][j * 4 + 2] = p / 2;
				if(p > 1)
					p -= 2;
				a[i][j * 4 + 3] = p;
			}
		}
		k = n < m ? n : m;
		memset(d, 0, sizeof(d));
		for(l = k;l > 1;l --)
		{
			for(i = 0;i + l <= m;i ++)
			{
				for(j = 0;j + l <= n;j ++)
				{
					if(a[i][j] < 0)
						continue;
					flag = true;
					for(y = j + 1;y < j + l;y ++)
					{
						if(a[i][y] < 0 || a[i][y] == a[i][y - 1])
						{
							flag = false;
							goto lab;
						}
					}
					for(x = i + 1;x < i + l;x ++)
					{
						if(a[x][j] < 0 || a[x][j] == a[x - 1][j])
						{
							flag = false;
							goto lab;
						}
					}
					for(x = i + 1;x < i + l;x ++)
					{
						for(y = j + 1;y < j + l;y ++)
						{
							if(a[x][y] < 0 || a[x][y] == a[x - 1][y] || a[x][y] == a[x][y - 1])
							{
								flag = false;
								goto lab;
							}
						}
					}
					lab:;
					if(flag)
					{
						d[l] ++;
						for(x = i;x < i + l;x ++)
							for(y = j;y < j + l;y ++)
								a[x][y] = - 1;
					}
				}
			}
		}
		for(i = 0;i < m;i ++)
			for(j = 0;j < n;j ++)
				if(a[i][j] >= 0)
					d[1] ++;
		int ans = 0;
		for(i = k;i > 0;i --)
		{
			if(d[i])
				ans ++;
		}
		printf("Case #%d: %d\n", ++ test, ans);
		for(i = k;i > 0;i --)
		{
			if(d[i])
				printf("%d %d\n", i, d[i]);
		}
	}
	return 0;
}

