// Google Code Jam 2012
// Round 1C
// Program A. Diamond inheritance

#include <cstdio>
#include <cstring>

int E[1001][1000];
int E_count[1001];
int visited[1001];
int N;

bool dfs(int v) // returns true if singly connected
{
	visited[v] = 1;
//	printf("DFS @ %d\n", v);
	for (int i = 0; i < E_count[v]; i++)
	{
		if (visited[E[v][i]] == 0)
		{
			if (!dfs(E[v][i]))
			{
//				printf("DFS @ %d, FALSE\n", v);
				return false;
			}
		}
		else if (visited[E[v][i]] == 2)
		{
//			printf("DFS @ %d, FALSE\n", v);
			return false;
		}
	}
	visited[v] = 2;
//	printf("DFS @ %d, TRUE\n", v);
	return true;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d", &N);
		for (int i = 1; i <= N; i++)
		{
			scanf("%d", E_count+i);
			for (int j = 0; j < E_count[i]; j++)
				scanf("%d", &(E[i][j]));
		}
		bool answer = 0;
		for (int i = 1; i <= N; i++)
		{
			memset(visited, false, sizeof(visited));
			if (!dfs(i)) // not singly connected
			{
				answer = true;
				break;
			}
		}
		if (answer) printf("Case #%d: Yes\n", t);
		else printf("Case #%d: No\n", t);
	}
}
