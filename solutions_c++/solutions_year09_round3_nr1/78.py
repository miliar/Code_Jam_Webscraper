#include <cstdio>

const int LMAX = 71;

char s[LMAX];
int t;

long long Solve()
{
	long long res = 0;
	int u[256];
	int base = 0;

	for (int i = 0; i < 256; i++)
		u[i] = -1;

	for (int i = 0; s[i]; i++)
		if (u[s[i]] == -1)
		{
			u[s[i]] = base;
			if (u[s[i]] == 0)
				u[s[i]] = 1;
			else if (u[s[i]] == 1)
				u[s[i]] = 0;
			base++;
		}

	if (base == 1)
		base++;

	for (int i = 0; s[i]; i++)
		res = res*base + u[s[i]];

	return res;
}

int main()
{
	freopen("base.in", "r", stdin);
	freopen("base.out", "w", stdout);

	scanf("%d\n", &t);
	for (int tnum = 1; tnum <= t; tnum++)
	{
		gets(s);
		printf("Case #%d: %lld\n", tnum, Solve());
	}

	return 0;
}
