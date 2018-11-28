#include <stdio.h>
#include <string.h>

const int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int cs, ct, n, m;
int a[100][100];
int s[100][100];
char ans[100][100];

bool is_sink(int x, int y)
{
	if (x > 0 && a[x - 1][y] < a[x][y]) return false;
	if (x + 1 < n && a[x + 1][y] < a[x][y]) return false;
	if (y > 0 && a[x][y - 1] < a[x][y]) return false;
	if (y + 1 < m && a[x][y + 1] < a[x][y]) return false;
	return true;
}

void check(int x, int y)
{
	if (s[x][y] != -1) return;
	int i, j, k, ii, jj;
	int max = -1;
	for (k = 0; k < 4; k++) {
		i = x + dir[k][0];
		j = y + dir[k][1];
		if (i >= 0 && i < n && j >= 0 && j < m) {
			if (a[x][y] - a[i][j] > max) {
				max = a[x][y] - a[i][j];
				ii = i;
				jj = j;
			}
		}
	}
	if (s[ii][jj] == -1) check(ii, jj);
	s[x][y] = s[ii][jj];
}

int main()
{
//	freopen("b.in", "r", stdin);
	int i, j, k, x, y;
	scanf("%d", &cs);
	for (ct = 1; ct <= cs; ct++) {
		scanf("%d%d", &n, &m);
		for (i = 0; i < n; i++)
		for (j = 0; j < m; j++)
			scanf("%d", &a[i][j]);

		memset(s, -1, sizeof(s));
		k = 0;
		for (i = 0; i < n; i++)
		for (j = 0; j < m; j++)
			if (is_sink(i, j)) s[i][j] = k++;

		for (i = 0; i < n; i++)
		for (j = 0; j < m; j++)
		if (s[i][j] == -1) check(i, j);		

		printf("Case #%d:\n", ct);
		memset(ans, 0, sizeof(ans));
		k = 0;
		for (i = 0; i < n; i++)
		for (j = 0; j < m; j++)
		if (!ans[i][j])
		{
			ans[i][j] = 'a' + k;
			k++;
			for (x = 0; x < n; x++)
			for (y = 0; y < m; y++)
				if (s[i][j] == s[x][y]) ans[x][y] = ans[i][j];
		}

		for (i = 0; i < n; i++) {
			printf("%c", ans[i][0]);
			for (j = 1; j < m; j++)
				printf(" %c", ans[i][j]);
			printf("\n");
		}

	}	
	return 0;
}
