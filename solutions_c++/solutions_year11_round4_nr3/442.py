#include <cstdio>
#include <algorithm>
using namespace std;

int N;

int L;
int P[1009];

int main()
{
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; Ti++)
	{
		//input
		scanf("%d ", &N);
		//printf("N = %d\n", N);
		
		//primes
		L = 0;
		for (int i = 2; i <= N; i++)
		{
			bool prime = true;
			for (int j = 2; j * j <= i; j++)
				if (i % j == 0)
				{
					prime = false;
					break;
				}
			if (prime)
			{
				P[L] = i;
				L++;
			}
		}
		
		//
		int maxima = 1;
		for (int i = 0; i < L; i++)
		{
			int j = P[i];
			while (j <= N)
			{
				j *= P[i];
				maxima++;
			}
		}
		//printf("maxima = %d\n", maxima);
		//printf("minima = %d\n", L);
		//printf("spread = %d\n", maxima - L);
		
		//output
		printf("Case #%d: ", Ti);
		if (N == 1)
			printf("0\n");
		else
			printf("%d\n", maxima - L);
		
	}
	return 0;
}