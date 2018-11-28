#include <stdio.h>
int test, t, n, k;
bool ans;

void init()
{
	scanf ( "%d%d", &n, &k);
}

void process()
{
	int full = 1;
	for (int i = 0; i < n; i++)
		full *= 2;
	ans = ( ( k % full ) == ( full - 1 ) );
}

void print()
{
	if (ans)
		printf("Case #%d: ON\n", test + 1);
	else
		printf("Case #%d: OFF\n", test + 1);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf( "%d", &t);
	for (test = 0; test < t; test++)
	{
		init();
		process();
		print();
	}
	return 0;
}