#include <cstdio>
using namespace std;
long long a[31];
void init()
{
	int i;
	a[0] = 2;
	for (i = 1; i < 30; i++)
		a[i] = a[i - 1] * 2;
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	init();
	int t, n;
	long long k;
	int i;
	scanf("%d", &t);
	for (i = 1; i <= t; i++)
	{
		scanf("%d%lld", &n, &k);
		k = k % a[n - 1];
		if (k == a[n - 1] - 1)
			printf("Case #%d: ON\n", i);
		else
			printf("Case #%d: OFF\n", i);
	}
	return 0;
}