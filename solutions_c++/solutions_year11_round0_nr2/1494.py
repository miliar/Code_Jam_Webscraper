#include <cstdio>

int C, D, N;
char c[100][10],
	 d[100][10],
	 s[1000],
	 ans[1000];

char find_combine(char a, char b)
{
	for (int i = 0; i < C; i ++)
		if ((c[i][0] == a && c[i][1] == b) ||
				(c[i][1] == a && c[i][0] == b))
			return c[i][2];
	return 0;
}

bool find_oppo(char *s, int n, char b)
{
	for (int i = 0; i < n; i ++)
	{
		char a = s[i];
		for (int i = 0; i < D; i ++)
			if ((d[i][0] == a && d[i][1] == b) ||
					(d[i][1] == a && d[i][0] == b))
				return true;
	}
	return false;
}

void solve(int cid)
{
	scanf("%d", &C);
	for (int i = 0; i < C; i ++)
		scanf("%s", c[i]);
	scanf("%d", &D);
	for (int i = 0; i < D; i ++)
		scanf("%s", d[i]);
	scanf("%d", &N);
	scanf("%s", s);

	int n = 0;
	for (int i = 0; i < N; i ++)
	{
		if (!n)
			ans[n ++] = s[i];
		else if (char ch = find_combine(ans[n - 1], s[i]))
			ans[n - 1] = ch;
		else if (find_oppo(ans, n, s[i]))
			n = 0;
		else ans[n ++] = s[i];
	}
	int p = 0;
	s[p ++] = '[';
	for (int i = 0; i < n; i ++)
	{
		s[p ++] = ans[i];
		if (i != n - 1)
		{
			s[p ++] = ',';
			s[p ++] = ' ';
		}
	}
	s[p ++] = ']';
	s[p] = 0;
	printf("Case #%d: %s\n", cid, s);
}

int main()
{
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i ++)
		solve(i);
	return 0;
}

