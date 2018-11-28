#include <iostream>

using	namespace	std;

const	int	maxk = 10;
const	int	maxlen = 1000;

int	k, cases, ans, l;
char	s[maxlen + 1], t[maxlen + 1];
int	p[maxk + 1];
bool	used[maxk + 1];

int	check()
{
	for (int i = 0; i < l; i += k)
	{
		for (int j = 1; j <= k; ++j)
			t[i + j - 1] = s[i + p[j] - 1];
	}
	int	rtn = 0;
	for (int i = 1; i < l; ++i)
		if (t[i] != t[i - 1])	++rtn;
	return	rtn;
}

void	calc(int dep)
{
	if (dep > k)
	{
		ans = min(ans, check());
		return;
	}
	for (int i = 1; i <= k; ++i)
	{
		if (used[i])	continue;
		used[i] = true;
		p[dep] = i;
		calc(dep + 1);
		used[i] = false;
	}
}

void	solve()
{
	scanf("%d%s", &k, s);
	l = strlen(s);


	ans = INT_MAX;
	for (int i = 0; i <= k; ++i)	used[i] = false;
	calc(1);
	printf("Case #%d: %d\n", ++cases, ans + 1);
}

int	main()
{
	int	t;
	scanf("%d", &t);
	while (t--)	solve();
	return	0;
}

