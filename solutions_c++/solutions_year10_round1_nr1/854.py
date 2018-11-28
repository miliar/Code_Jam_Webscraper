#include <iostream>
using namespace std;
const int maxn = 51;
char tmp[maxn][maxn];
char board[maxn][maxn];
int dx[4] = {0, 1, -1, 1};
int dy[4] = {1, 0, 1, 1};
int n, k;
bool dfs(int r, int c)
{
	int i, j;
	for (i = 0; i < 4; i++)
	{
		int cnt = 1;
		int r2 = r + dx[i];
		int c2 = c + dy[i];
		while (r2 >= 0 && r2 < n && c2 >= 0 && c2 < n
			&& board[r2][c2] == board[r][c])
		{
			r2 += dx[i];
			c2 += dy[i];
			cnt++;
		}
		if (cnt >= k)
		{
			return true;
		}
	}
	return false;
}
int main()
{
	int i, j, t, c = 0;
	bool r, b;
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &t);
	while (t--)
	{
		r = b = false;
		scanf("%d %d", &n, &k);
		for (i = 0; i < n; i++)
		{
			scanf("%s", tmp[i]);
		}
		for (i = 0; i < n; i++)
		{
			for (j = 0; j < n; j++)
			{
				board[i][j] = tmp[n-j-1][i];
			}
		}
		for (i = n - 2; i >= 0; i--)
		{
			for (j = 0; j < n; j++)
			{
				if (board[i][j] == '.')
				{
					continue;
				}
				int k = i + 1;
				while (board[k][j] == '.' && k <= n - 1)
				{
					board[k][j] = board[k-1][j];
					board[k-1][j] = '.';
					k ++;
				}
			}
		}
		for (i = 0; i < n; i++)
		{			
			for (j = 0; j < n; j++)
			{
				if (board[i][j] != '.')
				{
					if (board[i][j] == 'R' && !r)
					{
						r = dfs(i, j);
					}
					else if (board[i][j] == 'B' && !b)
					{
						b = dfs(i, j);
					}
				}
				if (b && r)
				{
					break;
				}
			}
		}
		printf("Case #%d: ", ++c);
		if (b && r)
		{
			printf("Both\n");
		}
		else if (b)
		{
			printf("Blue\n");
		}
		else if (r)
		{
			printf("Red\n");
		}
		else
		{
			printf("Neither\n");
		}
	}
	return 0;
}
