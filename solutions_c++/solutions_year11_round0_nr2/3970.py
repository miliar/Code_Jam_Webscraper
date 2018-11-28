/* Using C++(GCC) over FreeBSD */

#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int
main ()
{
	int cases, cases_r=0;

	scanf("%d", &cases);

	while (cases_r++<cases)
	{
		int m[26][26], p[26][26], x, i, k, c[26];

		char cur[105];

		char r[105];

		bzero(m, sizeof(m));
		bzero(p, sizeof(p));
		bzero(c, sizeof(c));
		bzero(r, sizeof(r));

		scanf("%d", &x);

		for (i=0; i<x; ++i)
		{
			scanf("%s", cur);
			m[cur[0]-'A'][cur[1]-'A'] = m[cur[1]-'A'][cur[0]-'A'] = cur[2];
		}

		scanf("%d", &x);

		for (i=0; i<x; ++i)
		{
			scanf("%s", cur);
			p[cur[0]-'A'][cur[1]-'A'] = p[cur[1]-'A'][cur[0]-'A'] = -1;
		}

		scanf("%d%s", &x, cur);

		for (i=k=0; i<x; ++i)
		{
			if (k>0)
			{
				int f=0;
				switch (m[cur[i]-'A'][r[k-1]-'A'])
				{
					case 0:
						r[k++] = cur[i];
						c[cur[i]-'A']++;
						break;
					default:
						c[r[k-1]-'A']--;
						r[k-1] = m[cur[i]-'A'][r[k-1]-'A'];
						c[r[k-1]-'A']++;
						f = 1;
						break;
				}
				for (int g=0; f==0 && g<26; ++g)
					if (p[cur[i]-'A'][g] == -1 && c[g] > 0)
					{
						k=0;
						bzero(c, sizeof(c));
						break;
					}
			}
			else
			{
				r[k++] = cur[i];
				c[cur[i]-'A']++;
			}
		}

		printf("Case #%d: [", cases_r);

		for (i=0; i<k; ++i)
		{
			putchar(r[i]);
			if (i!=k-1)
				printf(", ");
		}

		printf("]\n");
	}

	return 0;
}

