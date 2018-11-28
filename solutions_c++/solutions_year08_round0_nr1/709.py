#include <iostream>
#include <map>
#include <string>

using	namespace	std;

const	int	maxlen = 100;
const	int	maxs = 100;
const	int	maxq = 1000;

char	sename[maxlen + 1];
int	query[maxq + 1];
int	f[maxq + 1][maxs + 1];
int	cases;
map<string, int>	hash;

inline	void	update(int &a, int b)
{
	if (b < a)	a = b;
}

void	solve()
{
	int	s, q;
	hash.clear();

	scanf("%d\n", &s);

	for (int i = 0; i < s; ++i)
	{
		gets(sename);
		hash.insert(make_pair(string(sename), hash.size()));
	}
	scanf("%d\n", &q);

	if (q == 0)
	{
		printf("Case #%d: %d\n", ++cases, 0);
		return;
	}

	for (int i = 0; i < q; ++i)
	{
		gets(sename);
		query[i] = hash.find(string(sename))->second;
	}

	for (int j = 0; j < s; ++j)
		f[0][j] = 0;
	f[0][query[0]] = INT_MAX;

	for (int i = 1; i < q; ++i)
	{
		for (int j = 0; j < s; ++j)
		{
			f[i][j]= INT_MAX;
			if (query[i] == j)	continue;

			for (int k = 0; k < s; ++k)
			{
				if (f[i - 1][k] == INT_MAX)	continue;
				if (j == k)
					update(f[i][j], f[i - 1][k]);
				else
					update(f[i][j], f[i - 1][k] + 1);
			}
		}
	}

	int	ans = INT_MAX;
	for (int i = 0; i < s; ++i)
		update(ans, f[q - 1][i]);

	printf("Case #%d: %d\n", ++cases, ans);
}

int	main()
{
	int	t;
	scanf("%d\n", &t);
	while (t--)	solve();
	return	0;
}

