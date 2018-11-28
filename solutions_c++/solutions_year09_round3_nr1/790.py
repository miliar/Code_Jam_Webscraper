#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int visited[256];
int VTRUE;

int replaced[256];

int count;

int i, j, k, n, ncase;

char str[128];
char c;
int len;

int order[128];

long long ans;


int map[129];
long long aa, bb, cc, dd;
long long tobase()
{
	ans = 0;
	dd = 1;
	bb = count;
	for (aa = len - 1; aa >= 0; --aa)
	{
		cc = str[aa];

		ans += cc * dd;
		dd *= count;
	}
}

int main()
{
	order[0] = 1;
	order[1] = 0;
	for (i = 2; i <= 48; ++i)
	{
		order[i] = i;
	}

	gets(str);
	ncase = atoi(str);

	for (k = 1; k <= ncase; ++k)
	{
		gets(str);
		++VTRUE;

		// find how man distinct digits
		//
		count = 0;

		len = strlen(str);

		for (i = 0; i < len; ++i)
		{
			c = str[i];

			if (visited[c] != VTRUE)
			{
				visited[c] = VTRUE;
				++count;
			}
		}

		for (i = 0, n = 0; n < count; ++i)
		{
			c = str[i];
			if (c < '0' || replaced[c] == VTRUE)
			{
				continue;
			}

			replaced[n] = VTRUE;

			for (j = i; j < len; ++j)
			{
				if (str[j] == c)
				{
					str[j] = order[n];
				}
			}

			++n;
		}

		if (count == 1)
		{
			count = 2;
		}
		tobase();
		printf("Case #%d: %lld\n", k, ans);

	}

	return 0;
}

