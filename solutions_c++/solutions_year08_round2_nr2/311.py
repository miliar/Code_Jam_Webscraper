#include <stdio.h>
#include <memory.h>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

long long A, B, P;

bool isPrime(long long a)
{
	for (long long i = 2; i * i <= a; i++)
		if (a % i == 0)
			return false;
	return true;
}

long long count(long long a, long long b, long long p)
{
	return b / p - (a - 1) / p;
}

bool f(long long a, long long p)
{
	for (long long i = 2; i * i <= a; i++)
		while (a % i == 0)
		{
			a /= i;
			if (i >= p)
				return true;
		}
	if (a >= p)
		return true;
	else
		return false;

}

long long gcd(long long a, long long b)
{
	if (a < b)
		return gcd(b, a);
	if (b == 0)
		return a;
	else
		return gcd(b, a % b);
}

int mas[1001];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		scanf("%lld%lld%lld", &A, &B, &P);

		for (int i = 0; i < 1001; i++)
			mas[i] = i;

		for (long long i = A; i < B; i++)
			for (long long j = i + 1; j <= B; j++)
			{
				long long z = gcd(i, j);
				if (f(z, P))
				{
					int r1 = i - A;
					while (mas[r1] != r1)
						r1 = mas[r1];
					int r2 = j - A;
					while (mas[r2] != r2)
						r2 = mas[r2];
					if (r1 != r2)
						mas[r1] = r2;
				}
			}


		long long res = 0;
		for (int i = 0; i <= B - A; i++)
			if (mas[i] == i)
				res++;

		printf("Case #%d: %lld\n", t+1, res);
	}


	fclose(stdin);
	fclose(stdout);
	return 0;
}