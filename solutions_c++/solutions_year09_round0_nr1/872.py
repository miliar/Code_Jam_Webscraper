#include <cstdio>

char str[5050][17];
int main()
{
	int l, d, n;
	scanf("%d%d%d", &l, &d, &n);
	for (int i = 0; i < d; ++i)
	{
		scanf("%s", str[i]);
	}
	for (int T = 0; T < n; ++T)
	{
		char s[600];
		scanf("%s", s);
		int ans = 0;
		for (int j = 0; j < d; ++j)
		{
			char *p = s;
			bool bad = false;
			for (int t = 0; t < l && !bad; ++t)
			{
				if (*p != '(')
					if (*p != str[j][t])
						bad = true;
					else
						;
				else
				{
					int ok = 0;
					while (*p != ')')
					{
						if (*p == str[j][t])
							ok = 1;
						++p;
					}
					if (!ok)
						bad = true;
				}
				++p;
			}
			if (!bad)
				++ans;
		}
		printf("Case #%d: %d\n", T + 1, ans);

	}
}
