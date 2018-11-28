#include <stdio.h>

int mat[520][520], ans[520];

bool check(int size, int x, int y)
{
	for (int i = x; i < x + size; i ++)
	{
		for (int j = y; j < y + size; j ++)
		{
			if (mat[i][j] == -1) return false;
			if (i < x + size - 1 && (mat[i+1][j] == -1 || mat[i][j] + mat[i+1][j] != 1)) return false;
			if (j < y + size - 1 && (mat[i][j+1] == -1 || mat[i][j] + mat[i][j+1] != 1)) return false;
		}
	}
	for (int i = x; i < x + size; i ++)
	{
		for (int j = y; j < y + size; j ++) mat[i][j] = -1;
	}
	return true;
}

int main()
{
	//freopen("C2.in", "r", stdin);
	//freopen("C2.out", "w", stdout);

	int nprob, num, n, m;
	char ch, str[10000];
	scanf("%d", &nprob);
	for (int prob = 0; prob < nprob; prob ++)
	{
		scanf("%d%d", &m, &n);
		gets(str);
		for (int i = 0; i < m; i ++)
		{
			for (int j = 0; j < n / 4; j ++)
			{
				scanf("%c", &ch);
				if (ch >= 'A' && ch <= 'Z') num = 10 + ch - 'A'; else num = ch - '0';
				for (int k = 0; k < 4; k ++)
				{
					mat[i][(j<<2)+3-k] = num % 2;
					num /= 2;
				}
			}
			gets(str);
		}

		int msize = m < n ? m : n;
		for (int size = 1; size <= msize; size ++) ans[size] = 0;
		for (int size = msize; size >= 1; size --)
		{
			for (int i = 0; i <= m - size; i ++)
			{
				for (int j = 0; j <= n - size; j ++)
				{
					if (mat[i][j] == -1) continue;
					if (check(size, i, j)) {
						ans[size] ++;
					}
				}
			}
		}

		int tot = 0;
		for (int size = 1; size <= msize; size ++)
		{
			if (ans[size]) tot ++;
		}
		printf("Case #%d: %d\n", prob + 1, tot);
		for (int size = msize; size >= 1; size --)
		{
			if (ans[size]) printf("%d %d\n", size, ans[size]);
		}		
	}


	return 0;
}