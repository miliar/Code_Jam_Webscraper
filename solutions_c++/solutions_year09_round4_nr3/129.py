#include<stdio.h>
#include<string.h>

int n, k;

int c[105], p[105][50];
bool ok[105][105], mat[105][105];
bool check[105];

int DFS(int p)
{
	for (int i = 0; i < n; i++)
	{
		if (mat[p][i] && !check[i])
		{
			check[i] = 1;
			if (c[i] == -1 || DFS(c[i]))
			{
				c[i] = p;
				return 1;
			}
		}
	}
	return 0;
}


bool down(int a, int b)
{
	for (int i = 0; i < k; i++)
	{
		if (p[a][i] >= p[b][i])
			return 0;
	}
	return 1;
}

int main()
{
	int tc;
	scanf("%d", &tc);
	for (int t = 1; t <= tc; t++)
	{
		scanf("%d %d", &n, &k);
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < k; j++)
			{
				scanf("%d", &p[i][j]);
			}
		}
		memset(mat, 0, sizeof(mat));
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (down(i, j))
				{
					mat[i][j] = 1;
				}  
			}
		}
		
		int ans = 0;
		memset(c, 0xff, sizeof(c));
		for (int i = 0; i < n; i++)
		{
            memset(check, 0, sizeof(check));
		    ans += DFS(i);
		}
		printf("Case #%d: %d\n", t, n-ans);
	}
	return 0;
}
