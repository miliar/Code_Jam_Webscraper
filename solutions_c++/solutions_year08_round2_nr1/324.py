#include <stdio.h>
#include <memory.h>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

long long matr[3][3];

long long cnm(long long n, long long m)
{
	if (m > n)
		return 0;
	if (m == 0)
		return 1;
	if (m == 1)
		return n;
	if (m == 2)
		return n * (n - 1) / 2;
	if (m == 3)
		return n * (n - 1) * (n - 2) / 6;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		long long n, A, B, C, D, x0, y0, M;
		scanf("%lld%lld%lld%lld%lld%lld%lld%lld", &n, &A, &B, &C, &D, &x0, &y0, &M);
		for (int i = 0; i < 3; i++)
			for (int j = 0; j < 3; j++)
				matr[i][j] = 0;
		long long x, y;
		x = x0;
		y = y0;
		matr[x%3][y%3]++;
		/*
		for i = 1 to n-1
		  X = (A * X + B) mod M
		  Y = (C * Y + D) mod M
		  print X, Y
		*/
		for (int i = 1; i < n; i++)
		{
			x = (A * x + B) % M;
			y = (C * y + D) % M;
			matr[x%3][y%3]++;
		}
		int mm[3][3];
		long long res = 0;
		for (int i = 0; i < 9; i++)
			for (int j = i; j < 9; j++)
				for (int k = j; k < 9; k++)
				{
					int a = (i / 3) + (j / 3) + (k / 3);
					int b = (i % 3) + (j % 3) + (k % 3);
					if (a % 3 == 0 && b % 3 == 0)
					{
						memset(mm, 0, sizeof(int) * 9);
						mm[i/3][i%3]++;
						mm[j/3][j%3]++;
						mm[k/3][k%3]++;

						long long r = 1;
						for (int z1 = 0; z1 < 3; z1++)
							for (int z2 = 0; z2 < 3; z2++)
								r *= cnm(matr[z1][z2], mm[z1][z2]);
						res += r;
					}
					
				}
		printf("Case #%d: %lld\n", t + 1, res);
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}