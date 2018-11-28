#include <cstdio>
#include <cstring>

int T, ls, lp;
char welcome[32] = "welcome to code jam";
char strg[1512];
int C[1512][32];

int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);

	lp = strlen(welcome);

	scanf("%d\n", &T);
	for (int t = 1; t <= T; ++t)
	{
		int p = 0;
		strg[p] = '#';
		scanf("%c", &strg[p]);
		while ('a' <= strg[p] && strg[p] <= 'z' || strg[p] == ' ')
		{
			++p;
			strg[p] = '#';
			scanf("%c", &strg[p]);
		}
		ls = p+1;

		for (int s = 1; s <= ls; ++s)
			C[1][s] = C[1][s-1] + (strg[s-1] == welcome[0]);

		for (int p = 2; p <= lp; ++p)
			for (int s = 2; s <= ls; ++s)
			{
				C[p][s] = C[p][s-1];
				
				if (strg[s-1] == welcome[p-1])
					C[p][s] += C[p-1][s-1];

				C[p][s] %= 10000;
			}

		printf("Case #%d: ", t);

		for (int c = 1000; c > 0; c /= 10)
		{
			if (C[lp][ls] / c) 
			{
				printf("%d", C[lp][ls] / c);
				C[lp][ls] -= c * (C[lp][ls] / c);
			}
			else
				printf("0");
		}
		printf("\n");
	}

	return 0;
}