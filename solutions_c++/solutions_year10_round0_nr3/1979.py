#include <cstdio>

int R,k,N;

int mas[1100];

long long Calc1()
{
	int res = 0;
	int pos = 0;
	for (int i=0; i<R; i++)
	{
		int st = pos;
		if (mas[pos] > k)
			break;
		int cur = mas[pos];
		pos++;
		if (pos >= N)
			pos = 0;
		while(cur+mas[pos] <= k && st!=pos)
		{
			cur += mas[pos];
			pos++;
			if (pos >= N)
				pos = 0;
		}
		res += cur;
	}
	return res;
}


int next[1100];
long long add[1100];


void precalc()
{
	for (int i=0; i<N; i++)
	{
		int pos = i;
		int st = pos;
		if (mas[pos] > k)
		{
			next[i] = pos;
			add[i] = 0;
			continue;
		}

		long long cur = mas[pos];
		pos++;
		if (pos >= N)
			pos = 0;
		while(cur+mas[pos] <= k && st!=pos)
		{
			cur += mas[pos];
			pos++;
			if (pos >= N)
				pos = 0;
		}
		next[i] = pos;
		add[i] = cur;
	}
}


long long Calc2()
{
	precalc();
	long long res = 0;
	int pos = 0;
	for (int i=0; i<R; i++)
	{
		long long r2 = res;
		res += add[pos];
		if (res < r2)
			throw 0;
		pos = next[pos];
	}
	return res;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		scanf("%d%d%d", &R, &k, &N);
		for (int i=0; i<N; i++)
		{
			scanf("%d", &mas[i]);
		}
		long long res = Calc2();
		printf("Case #%d: %lld\n", t, res);
	}
	return 0;
}