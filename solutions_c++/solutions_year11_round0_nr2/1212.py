#include <stdio.h>
#include <string.h>

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int t, nrcomb, nropus, sz = 0, len;
	char comb[32][32], opus[32][32];;
	char a, b, c, prev;
	char sol[128];

	scanf("%d", &t);

	for(int test = 1; test <= t; ++test)
	{
		scanf(" %d ", &nrcomb);
		memset(comb, 0, sizeof(comb));
		memset(opus, 0, sizeof(opus));
		for(int i = 0; i < nrcomb; ++i)
		{
			scanf(" %c%c%c ", &a, &b, &c);
			comb[a - 'A'][b - 'A'] = comb[b - 'A'][a - 'A'] = c;
		}
		scanf(" %d ", &nropus);
		for(int i = 0; i < nropus; ++i)
		{
			scanf(" %c%c ", &a, &b);
			opus[a - 'A'][b - 'A'] = opus[b - 'A'][a - 'A'] = 1;
		}
		scanf(" %d ", &len);
		prev = -1;
		sz = 0;
		for(int i = 0; i < len; ++i)
		{
			scanf(" %c ", &a);
			if(prev != -1 && comb[prev][a - 'A'] != 0)
			{
				sol[sz - 1] = comb[prev][a - 'A'];
				prev = -1;
			}
			else
			{
				bool voided = false;
				for(int j = 0; j < sz; ++j)
				{
					if(opus[a - 'A'][sol[j] - 'A'])
					{
						sz = 0;
						voided = true;
						break;
					}
				}
				if(!voided)
				{
					sol[sz++] = a;
					prev = a - 'A';
				}
			}
		}
		printf("Case #%d: [", test);
		if(sz > 0)
		{
			printf("%c", sol[0]);
		}
		for(int i = 1; i < sz; ++i)
		{
			printf(", %c", sol[i]);
		}
		printf("]\n");
	}


	return 0;
}
