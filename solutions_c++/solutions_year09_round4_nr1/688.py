#include <cstdio>
#include <cstring>

const int NMAX = 45;

int a[NMAX];
int n;

void Swap(int &x, int &y)
{
	int tmp = x;
	x = y;
	y = tmp;
}

int Solve()
{
	int res = 0;
	for (int i = 0; i < n; i++)
	{
		int j = i;
		while (a[j] > i)
			j++;

		for (int k = j; k > i; k--)
		{
			Swap(a[k], a[k - 1]);
			res++;
		}
	}

	return res;
}

int main()
{
	freopen("rows.in", "r", stdin);
	freopen("rows.out", "w", stdout);

	int t;

	scanf("%d", &t);
	for (int tnum = 1; tnum <= t; tnum++)
	{
		memset(a, 0, sizeof(a));
		scanf("%d\n", &n);
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				char ch;
				scanf("%c", &ch);
				if (ch == '1')
					a[i] = j;
			}
			scanf("\n");
		}

		printf("Case #%d: %d\n", tnum, Solve());
	}

	return 0;
}
