#include <cstdio>
#include <cstring>

const int MaxN = 2048;

int R, K, N;
long long G[MaxN];
long long Get[MaxN];
int SkipTo[MaxN];
long long Ans;
int Hash[MaxN];
long long D[MaxN];

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		scanf("%d%d%d", &R, &K, &N);
		for (int i = 0; i < N; i ++)
		{
			scanf("%I64d", &G[i]);
			G[i + N] = G[i];
		}

		int j = -1;
		long long Cur = 0;
		for (int i = 0; i < N; i ++)
		{
			if (i != 0)
				Cur -= G[i - 1];
			while (j + 1 < i + N && Cur + G[j + 1] <= K)
				Cur += G[++ j];
			Get[i] = Cur;
			SkipTo[i] = (j + 1) % N;
		}

		memset(Hash, -1, sizeof(Hash));
		Hash[0] = 0;
		D[0] = 0;
		int Pos = 0;
		long long Ret = 0;
		for (int i = 1; ; i ++)
		{
			Ret += Get[Pos];
			if (i == R)
				break;
			if (Hash[SkipTo[Pos]] == -1)
			{
				Hash[SkipTo[Pos]] = i;
				D[SkipTo[Pos]] = D[Pos] + Get[Pos];
				Pos = SkipTo[Pos];
			}
			else
			{
				Pos = SkipTo[Pos];
				long long RoundRet = Ret - D[Pos];
				int RoundR = i - Hash[Pos];
				R -= i;
				Ret += RoundRet * (R / RoundR);
				R %= RoundR;
				while (R --)
				{
					Ret += Get[Pos];
					Pos = SkipTo[Pos];
				}
				break;
			}
		}

		printf("Case #%d: %I64d\n", Case, Ret);
	}
	return 0;
}
