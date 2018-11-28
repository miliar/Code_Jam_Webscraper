#include <stdio.h>

const int N = 1000000;

int p[N], top = 0;
bool np[N+1] = {};

void create()
{
	np[0] = true;
	np[1] = true;
	for (int i=2;i<=N;i++)
		if (!np[i])
		{
			p[top++] = i;
			for (int j=i+i;j<=N;j+=i)
				np[j] = true;
		}
}

int ans(long long n)
{
	int min = 0, max = 1;
	for (int i=0;i<top && p[i]<=n;i++)
	{
		min++;
		int count = 0;
		long long tmp = 1;
		while (tmp*p[i]<=n)
		{
			tmp = tmp*p[i];
			count++;
		}
		max += count;
	}
	min>?=1;
	return max-min;
}

int main()
{
	create();
	int t;
	long long n;
	scanf("%d", &t);
	for (int i=1;i<=t;i++)
	{
		scanf("%lld", &n);
		printf("Case #%d: %d\n", i, ans(n));
	}
	return 0;
}
