#include <algorithm>
#include <stdio.h>

#define MAX 128
#define INF 100000
#define mp make_pair
#define f first
#define s second

using namespace std;

char ch;
int n, m, testCases;
int alt[MAX][MAX], ind[MAX][MAX];
pair <int, int> solP[MAX][MAX];

inline pair <int, int> curge(int i, int j)
{
	if (solP[i][j].f)
		return solP[i][j];

	solP[i][j] = mp(i, j);

	if (alt[i - 1][j] < alt[i][j] && alt[i - 1][j] <= min(alt[i + 1][j], min(alt[i][j - 1], alt[i][j + 1])))
		solP[i][j] = curge(i - 1, j);
	else if (alt[i][j - 1] < alt[i][j] && alt[i][j - 1] <= min(alt[i][j + 1], min(alt[i - 1][j], alt[i + 1][j])))
		solP[i][j] = curge(i, j - 1);
	else if (alt[i][j + 1] < alt[i][j] && alt[i][j + 1] <= min(alt[i][j - 1], min(alt[i - 1][j], alt[i + 1][j])))
		solP[i][j] = curge(i, j + 1);
	else if (alt[i + 1][j] < alt[i][j] && alt[i + 1][j] <= min(alt[i - 1][j], min(alt[i][j - 1], alt[i][j + 1])))
		solP[i][j] = curge(i + 1, j);

	if (!ind[solP[i][j].f][solP[i][j].s])
		ind[solP[i][j].f][solP[i][j].s] = ch, ch++;

	ind[i][j] = ind[solP[i][j].f][solP[i][j].s];
	return solP[i][j];
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	scanf("%d", &testCases);

	for (int test = 1; test <= testCases; test++)
	{
		scanf("%d %d", &n, &m);
		ch = 'a';

		memset(alt, 0, sizeof(alt));
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				solP[i][j] = mp(0, 0);
		memset(ind, 0, sizeof(ind));

		for (int i = 0; i <= n + 1; i++)
			alt[i][0] = alt[i][m + 1] = INF;
		for (int i = 0; i <= m + 1; i++)
			alt[0][i] = alt[n + 1][i] = INF;

		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				scanf("%d", &alt[i][j]);

		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				curge(i, j);

		printf("Case #%d:\n", test);
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
				printf("%c ", ind[i][j]);
			printf("\n");
		}
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
