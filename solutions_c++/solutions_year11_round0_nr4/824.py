#include <stdio.h>
#include <algorithm>

/*const int max_n = 1000;

double P[max_n + 1][max_n + 1];
double W[max_n + 1];*/

void solve()
{
	int n, k, c;
	scanf("%d", &n);
	c = n;
	for (int i = 1; i <= n; i++)
	{
		scanf("%d", &k);
		if (k == i)
			c--;
	}
	//printf("%.7f\n", W[c]);
	printf("%d.000000\n", c);
}

/*void precomp()
{
	P[0][0] = 1.0;
	P[1][0] = 0.0;
	P[1][1] = 1.0;
	for (int n = 2; n <= max_n; n++)
	{
		P[n][0] = (1.0 - 1.0 / n) * (P[n - 1][0] + P[n - 2][0] / (n - 1));
		for (int k = 1; k <= n; k++)
			P[n][k] = P[n - 1][k - 1] / k;
	}
	W[0] = 0;
	for (int i = 1; i <= max_n; i++)
	{
		W[i] = 1;
		for (int j = 1; j <= i; j++)
			W[i] += P[i][j] * W[i - j];
		W[i] /= 1 - P[i][0];
	}
}*/

int main()
{
	int t;
	//precomp();
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
}