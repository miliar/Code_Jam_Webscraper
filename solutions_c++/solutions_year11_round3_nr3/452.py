#include <cstdio>

int N,L,H;

int mas[12000];

long long Solve()
{
	for (int r = L; r <= H; r++)
	{
		bool can = true;
		for (int i=0; i<N; i++)
		{
			if (!(mas[i]%r == 0 || r%mas[i] == 0))
			{
				can = false;
				break;
			}
		}
		if (can)
			return r;
	}
	return -1;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		scanf("%d%d%d", &N, &L, &H);
		for (int i=0; i<N; i++)
		{
			scanf("%d", &mas[i]);
		}

		long long res = Solve();
		if (res > 0)
			printf("Case #%d: %lld\n", t, res);
		else
			printf("Case #%d: NO\n", t);
	}
	return 0;
}