#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
struct Node
{
	long long d, l;
} a[10010];
int T, n;
long long d;
long long x[10010];

bool pass()
{
	memset(x, 0, sizeof(x));
	x[1] = a[1].d;
	for (int i = 1; i <= n; i++)
	{
		if (a[i].d + x[i] >= d) return true;
		for (int j = i + 1; j <= n && a[i].d + x[i] >= a[j].d; j++)
		{
			long long temp = a[j].l;
			if (temp > a[j].d - a[i].d)
				temp = a[j].d - a[i].d;
			if (temp > x[j]) x[j] = temp;
		}
	}
	return false;
}

int main()
{
	scanf("%d", &T);
	int ca = 0;
	while (T--)
	{
		memset(a, 0, sizeof(a));
		ca++;
		scanf("%d", &n);
		for (int i = 1; i <= n; i++)
			scanf("%lld%lld", &a[i].d, &a[i].l);
		scanf("%lld", &d);
		printf("Case #%d: ", ca);
		if (pass())
			puts("YES");
		else puts("NO");
	}
	return 0;
}
