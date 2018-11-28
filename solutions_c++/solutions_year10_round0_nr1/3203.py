#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, N;
	long K;
	int i;
	scanf("%d", &T);
	for (i = 1; i <= T; i++)
	{
		scanf("%d%ld", &N, &K);
		if (K % (long)pow(2, N) == ((long)pow(2, N) - 1))
			printf("Case #%d: ON\n", i);
		else printf("Case #%d: OFF\n", i);
	}
	return 0;
}
