#include <cstdio>
#include <cstring>


int nt;

char s[100];
char w[300];

__int64 res, cur;

int main()
{
	scanf("%d", &nt);

	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d: ", tt);

		scanf("%s", s);

		int base = 0;
		memset(w, 0, sizeof w);

		int k = 0;


		for(int i = 0; s[i]; i++)
			if (!w[s[i]])
			{
				w[s[i]] = base + 1;
				base++;
			}

		res = 0;
		if (base == 1) base = 2;

		for(int i = 0; s[i]; i++)
		{
			cur = w[s[i]];
			
			if (cur == 2) cur = 1;
			else
			if (cur == 1) cur = 2;

			res = res * base + cur - 1;
		}

		printf("%I64d\n", res);
	}

	return 0;	
}