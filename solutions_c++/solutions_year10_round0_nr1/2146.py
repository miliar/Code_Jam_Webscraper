#include <stdio.h>

int N,T,K;

int pow(int a, int b)
{
	int r = 1;
	while (b--)
		r *= a;
	return r;
}

int main()
{
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%d %d", &N, &K);
		int p = pow(2, N);
		bool aan = (K % p == p - 1);
		printf("Case #%d: %s\n", i + 1, (aan ? "ON" : "OFF"));
	}
	return 0;
}

