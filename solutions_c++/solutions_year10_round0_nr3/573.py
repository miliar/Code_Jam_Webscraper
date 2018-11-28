#include<cstdio>
#include<cstring>

int g[1000];
int R,K,n;
long long income[1001];
int f[1000];


int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("output.txt","w", stdout);
	int cases;
	scanf("%d",&cases);
	for (int ca = 1; ca <= cases; ++ca)
	{
		scanf("%d%d%d", &R,&K,&n);
		for (int i = 0; i < n; ++i) scanf("%d", g + i);
		memset(f, -1, sizeof(f));
		int now = 0 , round = 0;
		income[0] = 0;
		while (f[now] == -1)
		{
			long long can = 0;
			++round;
			f[now] = round;
		    for (int i = 0; i < n && can + g[now] <= K; ++i)
			{
				can += g[now];
				now = (now + 1) % n;
			}
			income[round] = income[round - 1] + can;
		}
		long long ans;
		if (R < f[now])
			ans = income[R];
		else
		{
			int RR = R - f[now] + 1;
			long long base = income[f[now] - 1];
			int length = round - f[now] + 1;
			ans = (income[round] - base) * (RR / length) + income[f[now] - 1 + RR % length];
		}

		printf("Case #%d: %lld\n", ca, ans );
	}
	fclose(stdin);
	fclose(stdout);
}
