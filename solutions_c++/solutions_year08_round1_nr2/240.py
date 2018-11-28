#include <cstring>
#include <cstdio>
#include <vector>
using namespace std;

#define MAXN 2011
#define MAXM 2011

int malted[MAXM], N, M, state[MAXN];
vector<int> like[MAXM];

void solve(int testCase)
{
	memset(state, 0, sizeof(state));

	int stop = 0;
	while (!stop)
	{
		stop = 1;
		for (int i = 0; i < M; i++)
		{
			if (malted[i] != -1 && state[malted[i]] == 1)
				continue;
			int j;
			for (j = 0; j < like[i].size(); j++)
				if (state[like[i][j]] == 0)
					break;
			if (j < like[i].size())
				continue;
			if (malted[i] == -1)
			{
				printf("Case #%d: IMPOSSIBLE\n", testCase + 1);
				return;
			}
			state[malted[i]] = 1;
			stop = 0;
		}
	}

	printf("Case #%d: ", testCase + 1);
	for (int i = 0; i < N; i++)
		printf("%d ", state[i]);
	printf("\n");
}

void readAndSolve()
{
	int T;

	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		memset(malted, -1, sizeof(malted));
		scanf("%d %d", &N, &M);
		for (int i = 0; i < M; i++)
		{
			int nr;
			scanf("%d", &nr);
			like[i].clear();
			for (int j = 0; j < nr; j++)
			{
				int X, Y;
				scanf("%d %d", &X, &Y), X--;
				if (Y == 1)
					malted[i] = X;
				else
					like[i].push_back(X);
			}
		}

		solve(t);
	}
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	readAndSolve();

	return 0;
}