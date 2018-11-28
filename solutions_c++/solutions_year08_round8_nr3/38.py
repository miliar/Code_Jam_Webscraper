#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
using namespace std;

#define MAXN 512
#define MOD 1000000009

int N, K, sons[MAXN], T[MAXN], seen[MAXN];
vector<int> V[MAXN];

int solve()
{
	queue<int> Q;

	Q.push(0);

	int res = 1;
	memset(seen, 0, sizeof(seen));
	memset(sons, 0, sizeof(sons));
	memset(T, -1, sizeof(T));
	seen[0] = 1;
	while (!Q.empty())
	{
		int nod = Q.front();

		for (int k = 0; k < V[nod].size(); k++)
		{
			int current = V[nod][k];
			if (seen[current])
				continue;
			seen[current] = 1;
			T[current] = nod;

			Q.push(current);

			sons[nod]++;
			int cnt = sons[T[current]] - 1;

			if (T[T[current]] != -1)
			{
				cnt += sons[T[T[current]]];
				int grandGrandFather = T[T[T[current]]];
				if (grandGrandFather != -1)
					cnt++;
			}			
			
			if (cnt > K)
				cnt = K;

			res = ((long long) res * (K - cnt)) % MOD;			
		}		

		Q.pop();
	}

	return res;
}

void readDataAndSolve()
{
	int T;

	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{	
		scanf("%d %d", &N, &K);

		for (int i = 0; i < N; i++)
			V[i].clear();

		for (int i = 0; i < N - 1; i++)
		{
			int a, b;

			scanf("%d %d", &a, &b), a--, b--;

			V[a].push_back(b), V[b].push_back(a);
		}

		printf("Case #%d: %d\n", t, solve());
	}
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	readDataAndSolve();

	return 0;
}