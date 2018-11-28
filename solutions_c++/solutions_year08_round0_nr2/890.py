#include <stdio.h>
#include <algorithm>

using namespace std;

#define maxn 510

int x, l;
int na, nb, nra, nrb, sa, sb;
int a[maxn], tip[maxn], p[maxn];

int cmp(int x, int y)
{
	return a[x] < a[y] || (a[x] == a[y] && tip[x] < tip[y]);
}

int main()
{
	freopen("train.in", "r", stdin);
	freopen("train.out", "w", stdout);

	int T, test;
	int h, min, i;

	scanf("%d ", &T);

	for (test = 1; test <= T; test++)
	{
		scanf("%d ", &x);

		scanf("%d %d ", &na, &nb);

		l = 0;

		for (i=1; i<=na+nb; i++)
		{
			scanf("%d:%d", &h, &min);
			a[++l] = h * 60 + min;
			tip[l] = 2 + (i>na);
			scanf("%d:%d", &h, &min);
			a[++l] = h * 60 + min + x;
			tip[l] = (i<=na);
		}

		for (i=1; i<=l; i++) p[i] = i;

		sort(p+1, p+l+1, cmp);

		nra = nrb = sa = sb = 0;

		for (i=1; i<=l; i++)
		{
			if (tip[p[i]] == 0) sa++;
			if (tip[p[i]] == 1) sb++;
			if (tip[p[i]] == 2)
			{
				if (sa > 0) sa--;
				else nra++;
			}
			if (tip[p[i]] == 3)
			{
				if (sb > 0) sb--;
				else nrb++;
			}
		}

		printf("Case #%d: %d %d\n", test, nra, nrb);
	}

	return 0;
}
