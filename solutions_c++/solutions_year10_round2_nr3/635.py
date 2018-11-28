#include <iostream>
using namespace std;
__int64 Cna(int n, int a)
{
	int i;
	if (n < a)
	{
		return 0;
	}
	if (a >= n / 2)
	{
		a = n - a;
	}
	__int64 res = 1;
	for (i = n; i >= n - a + 1; i--)
	{
		res *= i;
	}
	for (i = a; i >= 1; i--)
	{
		res /= i;
	}
	return res + 0.5;
}
__int64 rank(int n, int m)
{
	int i;
	__int64 res = 0;
	if (m == 1)
	{
		return 1;
	}
	for (i = 1; i <= m - 1; i++)
	{
		res += Cna(n - m - 1, m - i - 1) * rank(m, i) % 100003;
		res %= 100003;
	}
	return res;
}
int main()
{
	int i, j, n, t, c = 0;
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);
	//freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);
	scanf("%d", &t);
	while (t--)
	{
		__int64 res = 0;
		scanf("%d", &n);
		for (i = 1; i <= n - 1; i++)
		{
			res += rank(n, i);
			res %= 100003;
		}
		printf("Case #%d: %d\n", ++c, res);
	}
	return 0;
}
