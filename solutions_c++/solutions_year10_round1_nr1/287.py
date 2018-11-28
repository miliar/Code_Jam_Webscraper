#include <stdio.h>
#include <string.h>
char card[55][55], rcard[55][55];
int k, n;
int judge(char c)
{
	int i, j;
	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++)
			if (rcard[i][j] == c)
			{
				int ti = i + 1, tj = j + 1, cnt = 1;
				for (; ti < n && tj < n; ti++, tj++)
				{
					if (rcard[ti][tj] != c)
						break;
					cnt++;
				}
				if (cnt >= k)
					return 1;
				ti = i + 1, tj = j, cnt = 1;
				for (; ti < n && tj < n; ti++)
				{
					if (rcard[ti][tj] != c)
						break;
					cnt++;
				}
				if (cnt >= k)
					return 1;
				ti = i, tj = j + 1, cnt = 1;
				for (; ti < n && tj < n; tj++)
				{
					if (rcard[ti][tj] != c)
						break;
					cnt++;
				}
				if (cnt >= k)
					return 1;
				ti = i + 1, tj = j - 1, cnt = 1;
				for (; ti < n && tj >= 0; ti++, tj--)
				{
					if (rcard[ti][tj] != c)
						break;
					cnt++;
				}
				if (cnt >= k)
					return 1;
			}
	return 0;
}
int main()
{
	int T, tcnt = 1;
	freopen("A-large.in", "r", stdin);
	freopen("alarge.out", "w", stdout); 
	scanf("%d", &T);
	while (T--)
	{
		int i, j;
		scanf("%d%d", &n, &k);
		for (i = 0; i < n; i++)
			scanf("%s", card[i]);
		memset(rcard, 0, sizeof(rcard));
		for (i = 0; i < n; i++)
			for (j = 0; j < n; j++)
				rcard[i][j] = card[n - j - 1][i];
		//for (i = 0; i < n; i++)
		//	printf("%s\n", rcard[i]);
		for (i = n - 1; i >= 0; i--)
			for (j = 0; j < n; j++)
				if (rcard[i][j] != '.')
				{
					int l = i + 1;
					while (l < n)
					{
						if (rcard[l][j] == '.')
						{
							rcard[l][j] = rcard[l - 1][j];
							rcard[l - 1][j] = '.';
							l++;
						}
						else
							break;
					}
				}
		//for (i = 0; i < n; i++)
		//	printf("%s\n", rcard[i]);
		int r = judge('R'), b = judge('B');
		printf("Case #%d: ", tcnt);
		tcnt++;
		if (r + b == 0)
			printf("Neither\n");
		else if (r + b == 2)
			printf("Both\n");
		else if (r)
			printf("Red\n");
		else if (b)
			printf("Blue\n");
	}
	return 0;
}
