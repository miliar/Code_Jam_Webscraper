#include <stdio.h>
#include <algorithm>
using namespace std;

int b[1000010];
int e[1000010];
int c[1000010];
int w[1000010];

void change(int& a, int& b)
{
	int i;
	i = a;
	a = b;
	b = i;
}

void quicksort(int H, int T, int l[])
{
	int p, i;

	if (T-H == 1)
	{
		if (l[T] < l[H])
		{
			change(l[T], l[H]);
			change(c[T], c[H]);
		}
	}
	else if (T-H > 1)
	{
		p = H+1;
  
		for (i=H+1; i<=T; i++)
			if (l[i] < l[H])
			{
				change(l[i], l[p]);
				change(c[i], c[p]);
				p++;
			}

		change(l[p-1], l[H]);
		change(c[p-1], c[H]);

		quicksort (H, p-2, l);
		quicksort (p, T, l);
	}
}

int main()
{
	int T, t, i, j, s, r, x, n, m, tt, sm;
	double ans, rt;

	freopen("1.txt", "rb", stdin);
	freopen("out1.txt", "wb", stdout);

	scanf("%d", &T);

	for (tt=1; tt<=T; tt++)
	{
		ans = 0;
		sm = 0;
		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		rt = t;
		for (i=1; i<=n; i++)
		{
			scanf("%d%d%d", &b[i], &e[i], &w[i]);
			c[i] = e[i] - b[i];
			sm += c[i];
		}
		w[0] = 0;
		c[0] = x-sm;
		quicksort(0, n, w);

		for (i=0; i<=n; i++)
		{
			if ((w[i]+r)*rt > c[i])
			{
				ans += c[i]/(double)(w[i]+r);
				rt -= c[i]/(double)(w[i]+r);
				c[i] = 0;
			}
			else
			{
				ans = ans + rt + (c[i]-(w[i]+r)*rt)/(double)(w[i]+s);
				rt = 0;
				c[i] = 0;
				break;
			}
		}

		for (i=0; i<=n; i++)
			ans += c[i]/(double)(w[i]+s);

		printf("Case #%d: %.6lf\n", tt, ans);
	}

	return 0;
}
