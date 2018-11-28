#include <cstdio>
const int LIM = 51;
char picture[LIM][LIM];
bool substitute(int row, int column, int rlim, int clim)
{
	int dr[] = { 0, 1 };
	int dc[] = { 0, 1 };
	for (int i = 0; i < 2; i++)
		for (int j = 0; j < 2; j++)
			if (row + dr[i] < rlim && column + dc[j] < clim && picture[row + dr[i]][column + dc[j]] == '#')
				picture[row + dr[i]][column + dc[j]] = (dr[i] - dc[j] ? '\\' : '/');
			else
				return false;
	return true;
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int cas = 0; cas < t; cas++)
	{
		int r, c;
		scanf("%d%d", &r, &c);
		for (int i = 0; i < r; i++)
			scanf("%s", picture[i]);
		bool possible = true;
		for (int i = 0; i < r && possible; i++)
			for (int j = 0; j < c && possible; j++)
				if (picture[i][j] == '#')
					possible = substitute(i, j, r,c);
		printf("Case #%d:\n", cas + 1);
		if (!possible)
			printf("Impossible\n");
		else
			for (int i = 0; i < r; i++)
				printf("%s\n", picture[i]);
	}
	return 0;
}