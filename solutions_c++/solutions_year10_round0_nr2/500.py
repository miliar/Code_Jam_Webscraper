#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

const long maxn = 5;

long num[maxn];
long n, t;

long ab(long x)
{
	return x < 0 ? -x : x;
}

long gcd(long x, long y)
{
	return y > 0 ? gcd(y, x%y) : x;
}

void solve()
{
	long d = ab(num[1]-num[2]);
	
	for (long i = 1; i <= n; ++i)
		for (long j = i + 1; j <= n; ++j)
			d = gcd(d, ab(num[i] - num[j]));
	
	if (num[1]%d == 0) 
		printf("0\n");
	else
		printf("%ld\n", d - num[1]%d);
}

int main()
{
	freopen("BS.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%ld", &t);
	for (long l = 1; l <= t; ++l)
	{
		scanf("%ld", &n);
		for (long i = 1; i <= n; ++i) scanf("%ld", &num[i]);
		printf("Case #%ld: ", l);
		solve();
	}
	return 0;
}

