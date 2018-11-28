#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std; 
int gcd(int a, int b)
{
	return b ? gcd(b, a % b) : a;
}
int is_prime(int n)
{
	if (!n || n == 1)
		return 0;
	for (int i = 2; i * i <= n; i++)
	{
		if (n % i == 0)
			return 0;
	}
	return 1;
}
#define PRIME_UPPER 1000000
int prime[PRIME_UPPER], pn, pflag[PRIME_UPPER];
int gene_prime()
{
	memset(pflag, 0, sizeof(pflag));
	pflag[0] = pflag[1] = 1;
	for (int i = 2; i * i <= PRIME_UPPER; i++)
	{
		if (pflag[i])
			continue;
		for (int j = i + i; j < PRIME_UPPER; j += i)
			pflag[j] = 1;
	}
	for (int i = 0; i < PRIME_UPPER; i++)
		if (!pflag[i])
		{
			prime[pn] = i;
			pn++;
		}
}
int main()
{
	int T, tcnt = 0;
	freopen("", "r", stdin);
	freopen("", "w", stdout);
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d%d", &N, &M);
		for (int i = 0; i < M; i++)
			scanf("%d", &ea[i]);
		for (int j = 0; j < M; j++)
			scanf("%d", &eb[j]);
		
	}
	return 0;
}
