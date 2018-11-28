#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#define MAXP 1003

using namespace std;

int prime[MAXP];

int best(int n)
{
	if (n == 1)
		return 1;
	int ret = 0;
	for (int j = 2; j <= n; j++)
		if (prime[j])
			ret ++;
	return ret;
}

int worst(int n)
{
	int ret = 1;

	for (int j = 2; j <= n; j++)
		if (prime[j]) {
			int exp = 1;
			int v = j;
			while (v*j <= n) {
				v *= j;
				exp ++;
			}
			ret += exp;
		}

	return ret;
}

int main()
{
	for (int i = 2; i <= MAXP; i++)
		prime[i] = 1;
	prime[0] = prime[1] = 0;

	for (int i = 2; i <= MAXP; i++)
		if (prime[i])
			for (int j = i+i; j <= MAXP; j += i)
				prime[j] = 0;

	int T;

	scanf("%d", &T);

	for (int t = 0; t < T; t++) {
		int n;

		scanf("%d", &n);

		printf("Case #%d: %d\n", t+1, worst(n) - best(n));
	}

	return 0;
}
