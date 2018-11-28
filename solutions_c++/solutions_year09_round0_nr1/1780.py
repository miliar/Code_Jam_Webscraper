#include <stdio.h>
#include <string.h>

bool t[30][30];
char w[5010][20], s[300];
int main()
{
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	int T, l, d, n, m, p, x, i;
	scanf("%d%d%d", &l, &d, &n);
	for (i = 0; i < d; i++)
		scanf("%s", w[i]);
	for (T = 1; T <= n; T++)
	{
		scanf("%s", s);
		memset(t, 0, sizeof(t));
		for (p = x = i = 0; s[i]; i++)
		{
			if (s[i] == '(')
				x = 1;
			if (s[i] == ')')
			{
				x = 0;
				p++;
			}
			if (s[i] >= 'a' && s[i] <= 'z')
			{
				t[p][s[i]-'a'] = 1;
				p += 1-x;
			}
		}
		m = 0;
		for (i = 0; i < d; i++)
		{
			for (p = 0; p < l && t[p][w[i][p]-'a']; p++);
			m += p == l;
		}
		printf("Case #%d: %d\n", T, m);
	}
	return 0;
}

