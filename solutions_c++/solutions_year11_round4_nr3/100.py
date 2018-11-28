#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

const int MAXN = 10000010;

bool b[MAXN];

void init()
{
	int i,j,  k;
	memset(b, 1, sizeof(b));
	k = (int)sqrt(MAXN);
	for (i=2; i<=k; ++i)
	if (b[i])
	for (j=i*i; j<MAXN; j+=i)
		b[j] = false;
}

int gcd(int a, int b){ return (a == 0) ? b : gcd(b%a, a);}

long long n;

int fun(long long k, int j)
{
	int t = 0;
	while (k >= j)
	{
		++t;
		k /= j;	
	}
	return t;
}

void solve()
{
	scanf("%lld", &n);
	if (n == 1) printf("0\n");
	else
	{
		int i, t = 0;
		int j = (int)(sqrt(n) + 1e-6);
		for (i=2; i<=j; ++i)
		if (b[i])
			t += fun(n, i)-1;
		printf("%d\n", t+1);
	}
}

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int CASE, TT;
	init();
	scanf("%d", &TT);
	for (CASE=1; CASE<=TT; ++CASE)
	{
		printf("Case #%d: ", CASE);
		solve();
	}
	return 0;
}
