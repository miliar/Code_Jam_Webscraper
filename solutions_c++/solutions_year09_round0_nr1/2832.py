#include <stdio.h>

int TRUE = 1;

const int MAX_L = 16;
const int MAX_D = 6400;
int table[MAX_L][128];

char dict[MAX_D][MAX_L];
char str[102400];

int i, j, k, idx;
int l, d, n;

int count;
int ncase = 1;

char c;

int main()
{
	gets(str);
	sscanf(str, "%d %d %d", &l, &d, &n);
	for (i = 0; i < d; ++i)
	{
		gets(dict[i]);
	}

	for (i = 0; i < n; ++i)
	{
		// pattern
		gets(str);

		// build table for fast look up
		++TRUE;

		j = 0;
		idx = 0;

		while (idx < l)
		{
			c = str[j];

			if (c == '(')
			{
				++j;
				c = str[j];
				while(c != ')')
				{
					table[idx][c] = TRUE;

					++j;
					c = str[j];
				}
				++j;
			}
			else
			{
				table[idx][c] = TRUE;
				++j;
			}

			++idx;
		}

/*
puts("debug");
for (int a = 0; a < l; ++a)
{
for (int b = 'a'; b <= 'c'; ++b)
{
printf("%d", table[a][b]);
}
puts("");
}
puts("");
*/

		// look up matching

		count = 0;

		for (j = 0; j < d; ++j)
		{
			for (k = 0; k < l; ++k)
			{
				c = dict[j][k];
				if ( table[k][c] != TRUE)
				{
					break;
				}
			}

			if (k == l)
			{
				++count;
			}
		}

		// output

		printf ("Case #%d: %d\n", ncase++, count);
	}

	return 0;
}

