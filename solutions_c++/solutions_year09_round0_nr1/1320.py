#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <crtdbg.h>

const int MaxL = 15;
const int MaxD = 5000;
const int MaxN = 500;

int main()
{
	int l, d, n;
	char dict[MaxD][MaxL+1];

	scanf("%d %d %d\n", &l, &d, &n);
	for (int i = 0; i < d; i++)
		scanf("%s", dict[i]);

	char flags[MaxL][26];
	for (int in = 1; in <= n; in++)
	{
		char line[512];
		scanf("%s", line);

		memset(flags, 0, sizeof(flags));

		int il = 0;
		bool prntsis = false;
		for (int i = 0; i < strlen(line); i++)
		{
			if (line[i] == '(')
				prntsis = true;
			else if (line[i] == ')')
			{
				prntsis = false;
				il++;
			}
			else if (line[i] >= 'a' && line[i] <= 'z')
			{
				flags[il][line[i] - 'a'] = 1;
				if (!prntsis)
					il++;
			}
			else
				_ASSERT(0);
		}
		_ASSERT(il == l);

		int p = 0;
		for (int id = 0; id < d; id++)
		{
			int il = 0;
			for (il = 0; il < l; il++)
			{
				if (!flags[il][dict[id][il] - 'a'])
					break;
			}
			if (il == l)
				p++;
		}

		printf("Case #%d: %d\n", in, p);
	}
}
