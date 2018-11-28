#include <algorithm>
#include <stdio.h>

#define MAX 52

using namespace std;

int n, m, testCases;
char strMat[MAX][MAX];

int main()
{
	freopen("a-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);

	int t = 0;
	for (scanf("%d", &testCases); testCases; testCases--)
	{
		t++;
		printf("Case #%d:\n", t);

		scanf("%d %d\n", &n, &m);
		for (int i = 1; i <= n; i++)
			fgets(strMat[i] + 1, MAX, stdin);

		for (int i = 1; i < n; i++)
		{
			for (int j = 1; j < m; j++)
				if (strMat[i][j] == '#')
					if (strMat[i + 1][j] == '#' && strMat[i][j + 1] == '#' && strMat[i + 1][j + 1] == '#')
						strMat[i][j] = 47, strMat[i + 1][j] = 92, strMat[i][j + 1] = 92, strMat[i + 1][j + 1] = 47;
		}

		int ok = 1;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				if (strMat[i][j] == '#')
					ok = 0;

		if (!ok)
			printf("Impossible\n");
		else for (int i = 1; i <= n; i++)
			printf("%s", strMat[i] + 1);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
