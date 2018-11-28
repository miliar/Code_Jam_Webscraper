
#include <cstdio>
#include <string.h>

#define INF 10000

int n, m;
int g[2001][2001];
int x[2001];
int res[2001];
FILE* output = NULL;

int ans;
void dfs(int depth, int v)
{
	if (depth == n)
	{
		// Verify everyone is satisfied.
		for (int i = 0; i < m; i++)
		{
			bool ok = false;
			for (int j = 0; j < n; j++)
			{
				if (g[i][j] == 1 && res[j] == 1)
				{
					ok = true;
					break;
				}
				else if (g[i][j] == 3000 && res[j] == 0)
				{
					ok = true;
					break;
				}
			}
			if (!ok)
			{
				return;
			}
		}
		int aa = 0;
		for (int j = 0; j < n; j++) if (res[j] == 1) aa++;
		if (aa < ans)
		{
			ans = aa;
			for (int j = 0; j < n; j++) x[j] = res[j];
		}
		// Ok.
		return;
	}

	res[depth] = v;
	dfs(depth + 1, 0);
	dfs(depth + 1, 1);
}

void run()
{
	printf("n=%d, m=%d\n", n, m);

	ans = INF;
	dfs(0, 0);
	dfs(0, 1);

	if (ans == INF) { fprintf(output, "IMPOSSIBLE\n"); return;}
	for (int i = 0; i < n; i++) fprintf(output, "%d ", x[i]);
	fprintf(output, "\n");
}

int main()
{
	FILE* fp = fopen("d:\\in.txt", "r");
	output = fopen("d:\\out.txt", "w");

	int nTestCases;
	fscanf(fp, "%d", &nTestCases);
	for (int t = 1; t <= nTestCases; t++)
	{
		fscanf(fp, "%d %d", &n, &m);
		for (int i = 0; i < m; i++) for (int j = 0; j < n; j++)g[i][j] = 0;

		for (int i = 0; i < m; i++)
		{
			int nFlavors;
			fscanf(fp, "%d", &nFlavors);
			for (int k = 0; k < nFlavors; k++)
			{
				int flavor, malt;
				fscanf(fp, "%d %d", &flavor, &malt);
				if (malt == 1)
				{
					g[i][flavor - 1] = 1;
				}
				else 
				{
					g[i][flavor - 1] = 3000;
				}
			}
		}
		fprintf(output, "Case #%d: ", t);
		run();
	}

	return 0;
}