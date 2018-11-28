#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

const long maxn = 32;

long n, k, t;

void solve()
{
	bool pd = 1;
	for (long i = 1; i <= n; ++i)
	{
		if (k%2 == 0) pd = 0;
		k /=2;
	}
	
	if (pd) printf("ON\n");
	else printf("OFF\n");
		
}

int main()
{
	freopen("AL.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	scanf("%ld", &t);
	for (long l =  1; l <= t; ++l)
	{
		scanf("%ld%ld", &n, &k);
		printf("Case #%ld: ", l);
		solve();
	}
	return 0;
}

