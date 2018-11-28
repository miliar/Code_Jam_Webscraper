#include <iostream>
#include <algorithm>

#define N 60

using namespace std;

char board[N][N], result[N][N];
int n, k;
int dir[][2] = {{1, 0}, {0, 1}, {1, 1}, {1, -1}};

int DFS(int r, int c, char piece, int d, int tot)
{
	if (r >=0 && r < n && c >= 0 && c < n && result[r][c] == piece)
		return DFS(r + dir[d][0], c + dir[d][1], piece, d, tot + 1);
	else return tot;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int caseID = 1;
	while (caseID <= t)
	{
		printf("Case #%d: ", caseID++);
		scanf("%d %d", &n, &k);
		int i, j;
		for (i = 0; i < n; i++)
			scanf("%s", board[i]);
		for (i = 0; i < n; i++)
			for (j = 0; j < n; j++)
				result[i][j] = board[n - 1 - j][i];
		for (i = n - 1; i >= 0; i--)
			for (j = 0; j < n; j++)
			{
				int r = i, c = j;
				while (result[r][c] != '.' && result[r + 1][c] == '.' && r + 1 < n)
				{
					swap(result[r][c], result[r + 1][c]);
					r++;
				}
			}
		bool flag[200];
		memset(flag, 0, sizeof(flag));
		for (i = 0; i < n; i++)
			for (j = 0; j < n; j++)
				if (result[i][j] != '.')
				{
					int p;
					for (p = 0; p < 4; p++)
						if (DFS(i, j, result[i][j], p, 0) >= k) flag[result[i][j]] = 1;
				}
		if (!flag['R'] && !flag['B']) printf("Neither\n");
		if (flag['R'] && !flag['B']) printf("Red\n");
		if (!flag['R'] && flag['B']) printf("Blue\n");
		if (flag['R'] && flag['B']) printf("Both\n");
	}
	return 0;
}