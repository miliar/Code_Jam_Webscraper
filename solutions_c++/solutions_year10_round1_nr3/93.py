#include <cstdio>
#include <cstring>
#include <cmath>

long double point = (sqrtl(5) - 1) / 2;

int count(int x, int y)
{
	if (y == 0) return 1;
	long long total = 0;
	if (y >= x * 2)
	{
		total += y - x * 2 + 1;
		y = x * 2 - 1;
	}
	if (y > x)
	{
		total += y - x + 1 - count(x, y - x);
		y = x - 1;
	}
	int t = int(x * point);
	if (y <= t) return total + y + 1;
	else return total + t + 1;
}

int main()
{
	int testnumber, testcount;
	int a1, a2, b1, b2;
	
	freopen("C-large.in", "r", stdin);
	freopen("c.out", "w", stdout);
	scanf("%d", &testnumber);
	for (testcount = 0; testcount < testnumber; testcount++)
	{
		scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
		long long total = 0;
		for (int i = a1; i <= a2; i++)
			total += count(i, b2) - count(i, b1 - 1);
		printf("Case #%d: %I64d\n", testcount + 1, total);
	}
	
	return 0;
}
