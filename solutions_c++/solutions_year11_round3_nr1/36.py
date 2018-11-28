#include <cstdio>
#include <algorithm>
using namespace std;
char Map[100][100];
void solve()
{
	int N, M;
	scanf ("%d%d\n", &N, &M);
	for (int i = 0; i < N; ++i)
	{
		scanf ("%s", Map[i]);
	}
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			if (Map[i][j] != '#') continue;
			Map[i][j] = '/';
			if (i + 1 >= N || j + 1 >= M)
			{
				printf ("Impossible\n");
				return;
			}
			if (Map[i][j + 1] != '#' || Map[i + 1][j + 1] != '#' || Map[i + 1][j] != '#') 
			{
				printf ("Impossible\n");
				return;
			}
			Map[i][j + 1] = '\\';
			Map[i + 1][j] = '\\';
			Map[i + 1][j + 1] = '/';
		}
	}
	for (int i = 0; i < N; ++i)
	{
		puts(Map[i]);
	}
}
int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int T;
	scanf ("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		printf ("Case #%d:\n", i + 1);
		solve();
	}
	return 0;
}