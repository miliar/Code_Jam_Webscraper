#include <iostream>

using namespace::std;

void work()
{
	int n, x, o, b, lo, lb, t, i, p;
	char ch;

	scanf("%d", &n);
	o = b = 1;
	lo = lb = t = 0;
	for (i = 1; i <= n; ++i)
	{
		scanf("%c%c%d", &ch, &ch, &x);
		if (ch == 'O') 
		{
			p = min(t - lo, abs(x - o));
			if (abs(o + p - x) < abs(o - p - x)) o += p;
			else o -= p;
			t += abs(o - x) + 1;
			lo = t;
			o = x;
		}
		else
		{
			p = min(t - lb, abs(x - b));
			if (abs(b + p - x) < abs(b - p - x)) b +=p;
			else b -= p;
			t += abs(b - x) + 1;
			lb = t;
			b = x;
		}
	}
	printf("%d\n", t);
}

int main()
{
	int test, t;

	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	for (scanf("%d", &test), t = 1; t <= test; ++t)
	{
		printf("Case #%d: ", t);
		work();
	}

	return 0;
}