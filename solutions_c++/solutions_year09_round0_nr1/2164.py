#include <stdio.h>

int main()
{
	static char W[5000][16];
	static int B[15]['z' - 'a' + 1];
	int l, d, n;
	scanf("%d %d %d", &l, &d, &n);
	for (int i = 0; i < d; i++)
	{
		scanf("%s", W[i]);
		for (int j = 0; j < l; j++)
			W[i][j] -= 'a';
	}
	for (int t = 1; t <= n; t++)
	{
		scanf("\n");
		for (int i = 0; i < l; i++)
		{
			char chr = getchar();
			if (chr == '(')
				while ((chr = getchar()) != ')')
					B[i][chr - 'a'] = t;
			else
				B[i][chr - 'a'] = t;
		}
		int c = 0;
		for (int i = 0; i < d; i++)
		{
			for (int j = 0; j < l; j++)
				if (B[j][W[i][j]] != t)
					goto _break;
			c++;
_break:;
		}
		printf("Case #%d: %d\n", t, c);
	}
	return 0;
}