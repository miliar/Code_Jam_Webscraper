#include<stdio.h>
#include<string.h>

long long n;
long long p[1000000];
int cnt;

void makeprime()
{
	for(int i=2; i<=1000000; i++)
	{
		bool ok = true;
		for(int j=2; ok && j*j<=i; j++)
			if(i % j == 0) ok = false;
		if(ok) p[cnt++] = i;
	}
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int ntest;
	makeprime();
	scanf("%d", &ntest);
	for(int test = 1; test <= ntest; test++)
	{
		scanf("%I64d", &n);
		long long ans = (n==1 ? 0 : 1);
		for(int i=0; p[i]*p[i]<=n && i<cnt; i++)
		{
			long long t = p[i] * p[i];
			while(t <= n)
			{
				t *= p[i];
				ans++;
			}
		}
		printf("Case #%d: %I64d\n", test, ans);
	}
	return 0;
}
