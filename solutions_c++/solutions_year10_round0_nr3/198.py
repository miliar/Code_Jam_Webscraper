#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long int64;

int64 sumg[2048], r[1024];

int go[1024];

int T, R, k, N;

void cango(int f)
{
	int nxt = upper_bound(sumg, sumg + 2 * N + 1, sumg[f - 1] + k) - sumg - 1;
	go[f] = min(nxt, f + N - 1);
	r[f] = sumg[go[f]] - sumg[f - 1];
}

int pos[1024];
int64 sr[1024];

int main()
{
	freopen("f:\\C-small-attempt0.in", "r", stdin);
	freopen("f:\\C-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for (int t_case = 1; t_case <= T; t_case++)
	{
		scanf("%d %d %d", &R, &k, &N);
		for (int i = 1; i <= N; i++)
		{
			scanf("%lld", &sumg[i]);
			sumg[N + i] = sumg[i];
			sumg[i] += sumg[i - 1];
		}
		for (int i = N + 1; i <= 2 * N; i++)
			sumg[i] += sumg[i - 1];
		for (int i = 1; i <= N; i++)
			cango(i);

		int64 res = 0;
		memset(pos, 0xff, sizeof(pos));
		int i, cur = 1, cycle = -1;
		int64 rc = -1;
		for (i = 0; i < R; i++)
		{
			res += r[cur];
			if (pos[cur] == -1)
			{
				pos[cur] = i;
				sr[cur] = res;
			}
			else
			{
				cycle = i - pos[cur];
				rc = res - sr[cur];
				break;
			}
			cur = go[cur] + 1;
			if (cur > N) cur -= N;
		}
		if (i < R)
		{
			R -= i + 1;
			res += R / cycle * rc;
			R %= cycle;
			for (i = 0; i < R; i++)
			{
				res += r[cur];
				cur = go[cur] + 1;
				if (cur > N) cur -= N;
			}
		}
		printf("Case #%d: %lld\n", t_case, res);
	}
	return 0;
}
