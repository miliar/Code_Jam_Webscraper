#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
struct Node
{
	int num, r, x, y;
} a[1010];

int T, n, w, l;

bool cmp1(Node p, Node q)
{
	return (p.r > q.r);
}

bool cmp2(Node p, Node q)
{
	return (p.num < q.num);
}

int main()
{
	scanf("%d", &T);
	int ca = 0;
	while (T--)
	{
		ca++;
		scanf("%d%d%d", &n, &w, &l);
		for (int i = 1; i <= n; i++)
			scanf("%d", &a[i].r);
		for (int i = 1; i <= n; i++)
			a[i].num = i;
		sort(a + 1, a + n + 1, cmp1);
		a[1].x = a[1].y = 0;
		int ll = 1;
		for (int i = 2; i <= n; i++)
			if (a[i - 1].x + a[i - 1].r + a[i].r <= w)
			{
				a[i].x = a[i - 1].x + a[i - 1].r + a[i].r;
				a[i].y = a[i - 1].y;
			}
			else
			{
				a[i].x = 0;
				a[i].y = a[ll].y + a[ll].r + a[i].r;
				ll = i;
			}
		if (a[n].y > l) cout << "T_T" << endl;
		sort(a + 1, a + n + 1, cmp2);
		printf("Case #%d:", ca);
		for (int i = 1; i <= n; i++)
			printf(" %d %d", a[i].x, a[i].y);
		puts("");
	}
	return 0;
}
