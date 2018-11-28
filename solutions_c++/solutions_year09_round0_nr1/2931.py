#include <stdio.h>
#include <string.h>

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int L, D, N, v[5000][15], h[500][15], i, j, k, t;
	char s[27*16];
	memset(v, 0, sizeof(v));
	memset(h, 0, sizeof(h));
	scanf("%d%d%d ", &L, &D, &N);
	for (i = 0; i < D; i++)
	{
		for (gets(s), j = 0; j < L; j++)
		{
			v[i][j] |= (1 << (s[j] - 'a'));
		}
	}

	for (i = 0; i < N; i++)
	{
		for (gets(s), j=0, k=0; j < L; j++, k++)
		{
			if (s[k] == '(')
			{
				while (s[++k] != ')')
				{
					h[i][j] |= (1 << (s[k] - 'a'));
				}
			}
			else
			{
				h[i][j] |= (1 << (s[k] - 'a'));
			}
		}
	}

	for (i = 0; i < N; i++)
	{
		for (t = j = 0; j < D; j++)
		{
			for (k = 0; k < L; k++)
			{
				if (!(h[i][k] & v[j][k]))
				{
					break;
				}
			}
			t += (k == L);
		}
		printf("Case #%d: %d\n", i+1, t);
	}
	return 0;
}