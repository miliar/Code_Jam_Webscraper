#include <iostream>
using namespace std;

int o[103][2], b[103][2];
int n, n_o, n_b, ans, last;

void init()
{
	int i, x;
	char c;

	scanf("%d", &n);
	n_o = n_b = 0;
	for (i = 1; i <= n; ++i)
	{
		scanf("%c%c%d", &c, &c, &x);
		if (c == 'O')
		{
			o[++n_o][0] = x;
			o[n_o][1] = i;
		}
		else
		{
			b[++n_b][0] = x;
			b[n_b][1] = i;
		}
	}
}

void work()
{
	int i, j, p, q;
	bool flag;

	i = j = p = q = 1;
	for (ans = last = 0; last < n; ++ans)
	{
		flag = 0;
		if (p <= n_o)
		{
			if (i != o[p][0])
			{
				if (i < o[p][0]) ++i;
				else --i;
			}
			else if (o[p][1] == last + 1) flag = ++p;
		}
		if (q <= n_b)
		{
			if (j != b[q][0])
			{
				if (j < b[q][0]) ++j;
				else --j;
			}
			else if (b[q][1] == last + 1) flag = ++q;
		}
		if (flag) ++last;
	}
	printf("%d\n", ans);
}

int main()
{
	int i = 1, t;

//	freopen("A-large.in", "r", stdin);
//	freopen("A-large.out", "w", stdout);
	for (scanf("%d", &t); i <= t; ++i)
	{
		init();
		printf("Case #%d: ", i);
		work();
	}
	return 0;
}