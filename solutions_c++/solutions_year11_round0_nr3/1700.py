#include <iostream>
#include <algorithm>
using namespace std;
int n, ans, tot;
int a[10000];

void init()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);
}

void process()
{
	sort(a, a + n);
	ans = 0;
	tot = 0;
	for (int i = 0; i < n; i++)
	{
		ans = ans ^ a[i];
		tot += a[i];
	}
	tot -= a[0];
}

int main()
{
//	freopen("gcjc.in", "r", stdin);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		init();
		process();
		if (ans == 0)
			printf("Case #%d: %d\n", i + 1, tot);
		else
			printf("Case #%d: NO\n", i + 1);
	}
	return 0;
}