#include <stdio.h>
#include <string.h>

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, l;
	scanf("%d", &t);
	for (l = 1; l <= t; ++l)
	{
		char comb[26][26];
		bool opp[26][26];
		memset(comb, 0, sizeof(comb));
		memset(opp, 0, sizeof(opp));
		int c;
		scanf("%d", &c);
		while (c--)
		{
			char s[4];
			scanf("%s", s);
			comb[s[0] - 'A'][s[1] - 'A'] = comb[s[1] - 'A'][s[0] - 'A' ] = s[2];
		}
		int d;
		scanf("%d", &d);
		while (d--)
		{
			char s[3];
			scanf("%s", s);
			opp[s[0] - 'A'][s[1] - 'A'] = opp[s[1] - 'A'][s[0] - 'A'] = true;
		}

		int n, m = 0;
		char s[110], ans[110];
		scanf("%d%s", &n, s);
		for (int i = 0; i < n; ++i)
			if (m > 0 && comb[s[i] - 'A'][ans[m - 1] - 'A'] != 0)
				ans[m - 1] = comb[s[i] - 'A'][ans[m - 1] - 'A'];
			else
			{
				int j;
				for (j = 0; j < m; ++j)
					if (opp[ans[j] - 'A'][s[i] - 'A'] == true)
						break;
				if (j >= m)
					ans[m++] = s[i];
				else
					m = 0;
			}

		printf("Case #%d: [", l);
		for (int i = 0; i < m; ++i)
			printf("%c%s", ans[i], i == m - 1?"":", ");
		printf("]\n");
	}
	return 0;
}
