#include <cstdio>
#include <algorithm>

using namespace std;

int N;
int data[2001];
long long ans[2001];
long long limit[2001];

long long strict(int st, int ed, long long vst, long long ved, int pt)
{
	long long den = ed - st;
	long long num = ved - vst;

	long long nv = num * (pt - st);
	return (nv + vst * den - 1) / den;
}

long long lte(int st, int ed, long long vst, long long ved, int pt)
{
	long long den = ed - st;
	long long num = ved - vst;

	long long nv = num * (pt - st);
	return (nv + vst * den) / den;
}

int solve(int st, int ed)
{
	if (st > ed)
		return true;
	if (ans[st] != -1)
		return true;
	if (st == ed && st == N - 1)
	{
		ans[st] = limit[st];
		return true;
	}
	int high = data[st];
	if (high > ed + 1)
		return false;

	if (!solve(high, ed))
		return false;

	ans[st] = limit[st];
	if (high != N - 1)
		ans[st] = min(lte(high, data[high], ans[high], ans[data[high]], st), ans[st]);
	for (int i = st + 1;i < high;i++)
		limit[i] = min(strict(st, high, ans[st], ans[high], i), limit[i]);

	if (!solve(st + 1, high - 1))
		return false;
	return true;
}

int main()
{
	int tc;
	scanf("%d", &tc);
	for (int ti = 1;ti <= tc;ti++)
	{
		scanf("%d", &N);
		for (int i = 0;i < N - 1;i++)
		{
			scanf("%d", &data[i]);
			data[i]--;
		}

		for (int i = 0;i < N;i++)
		{
			limit[i] = 1000000000;
			ans[i] = -1;
		}

		int res = solve(0, N - 1);
		printf("Case #%d: ", ti);
		if (!res)
			printf("Impossible\n");
		else
		{
			for (int i = 0;i < N;i++)
				printf("%d ", (int)ans[i]);
			printf("\n");
		}
	}
	return 0;
}
