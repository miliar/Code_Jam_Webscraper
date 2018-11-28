#include<stdio.h>
#include<math.h>
#define MAXN 1000
int test, t, n, ans, ans2;
int a[MAXN];

void init()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);
}

int gcd (int a, int b)
{
	if (b == 0)
		return a;
	else
		return gcd (b, a % b);
}
void process()
{
	ans = abs(a[0] - a[1]);
	for (int i = 0; i < n; i++)
		for (int j = i+1; j < n; j++)
			ans = gcd (ans, abs(a[i] - a[j]));
	ans2 = -a[0] % ans;
	if (ans2 < 0)
		ans2 += ans;
}

void print()
{
	printf ("Case #%d: %d\n", test + 1, ans2);
}

int main()
{
	freopen("B-small-attempt2.in", "r", stdin);
	freopen("B-small-attempt2.out", "w", stdout);
	scanf ("%d", &t);
	for (test = 0; test < t; test++)
	{
		init();
		process();
		print();
	}
}