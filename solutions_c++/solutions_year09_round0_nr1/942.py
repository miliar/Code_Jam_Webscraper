#include <cstdio>
#include <cstring>

int main()
{
	
	int l, d, n, i, j, k, lp, lm, cnt;
	char word[5005][16], p[425];
	bool m[16][27], match;
	
	scanf("%d%d%d", &l, &d, &n);
	for (i = 0; i < d; ++i)
		scanf("%s", word[i]);
	
	for (i = 1; i <= n; ++i)
	{
		scanf("%s", p);
		lp = strlen(p);
		
		memset(m, false, sizeof(m));
		lm = 0;
		
		j = 0;
		while (j < lp)
		{
			if (p[j] == '(') {
				k = j + 1;
				while (k < lp && p[k] != ')')
				{
					m[lm][p[k] - '0'] = true;
					++k;
				}
				++lm;
				j = k + 1;
			} else {
				m[lm][p[j] - '0'] = true;
				++lm;
				++j;
			}
		}
		
		cnt = 0;
		for (j = 0; j < d; ++j)
		{
			match = true;
			for (k = 0; k < l; ++k)
				if (m[k][word[j][k] - '0'] == false)
					match = false;
			if (match)
				++cnt;
		}
		printf("Case #%d: %d\n", i, cnt);
	}
	
	return 0;
}
