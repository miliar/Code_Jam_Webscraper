#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <set>

using namespace std;

int mod = 100003;

int a[555][555];
long long C[555][555];

void Solve(int n, int k)
{
	if (a[n][k] != -1)
		return;
	if (k == 1)
	{
		a[n][k] = 1;
		return;
	}
	a[n][k] = 0;
	for (int i = 1; i < k; ++i)
	{
		Solve(k, i);
		a[n][k] = (a[n][k] +  C[n - k - 1][k - i - 1] * a[k][i]) % mod;
	}
}
void CalcC()
{
	C[0][0] = 1;
	for (int n = 1; n <= 501; ++n)
	{
		C[n][0] = 1;
		for (int k = 1; k <= n; ++k)
			C[n][k] = (C[n - 1][k - 1] + C[n - 1][k]) % mod;
	}
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	CalcC();
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t)
	{
		int n;
		scanf("%d", &n);
		memset(a, -1, sizeof(a));
		int res = 0;
		for (int k = 1; k < n; ++k)
		{
			Solve(n, k);
			res = (res + a[n][k]) % mod;
		}
		printf("Case #%d: ", t + 1);
		printf("%d\n", res);
	}
	

	return 0;
}
