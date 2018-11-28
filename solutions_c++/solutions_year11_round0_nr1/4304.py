#include <iostream>
#include <cstdio>

using namespace std;

int abs(int x)
{
	if (x < 0)
	{
		return -x;
	}
	else
	{
		return x;
	}
}

int max(int a, int b)
{
	if (a > b)
	{
		return a;
	}
	else
	{
		return b;
	}
}

int n,t,x;
char ch;

int main()
{
	freopen("out.txt", "wt", stdout);
	scanf("%d", &t);

	for (int j = 1; j <= t; j++)
	{
		scanf("%d", &n);

		int p1 = 1;
		int p2 = 1;

		int t1 = 1;
		int t2 = 1;

		int ti = 0;
		
		for (int i = 0; i < n; i++)
		{
			scanf(" %c %d", &ch, &x);

			if (ch == 'O')
			{
				ti = max(ti + 1, t1 + abs(p1-x) + 1);
				t1 = ti;
				p1 = x;
			}
			else if (ch == 'B')
			{
				ti = max(ti + 1, t2 + abs(p2-x) + 1);
				t2 = ti;
				p2 = x;
			}
		}

		printf("Case #%d: %d\n", j, ti-1);
	}
}