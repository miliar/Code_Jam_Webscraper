#include <stdio.h>
const int MAXN = 100000;
long long int X[MAXN], Y[MAXN];
int n, A, B, C, D, M;
int main()
{
	int t;
	scanf("%d", &t);
	for (int cases = 1; cases <= t; cases++)
	{
		scanf("%d %lld %lld %lld %lld %lld %lld %lld", &n, &A, &B, &C, &D, &X[0], &Y[0], &M);
		for (int i = 1; i < n; i++) {
			X[i] = (X[i - 1] * A + B) % M;
			Y[i] = (Y[i - 1] * C + D) % M;
		}
		int count = 0;
		for (int i = 0; i < n; i++)
			for (int j = i + 1; j < n; j++)
				for (int k = j + 1; k < n; k++)
					if ((X[i] + X[j] + X[k]) % 3 == 0 && ((Y[i] + Y[j] + Y[k]) % 3 == 0)) count++;
		printf("Case #%d: %d\n", cases, count);
	}
}
