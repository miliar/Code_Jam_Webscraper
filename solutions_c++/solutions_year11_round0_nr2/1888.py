#include <stdio.h>
#include <string.h>

char com[37][4], opp[29][3];
int c, d, n, k;
char elem, str[101];

int doCom(const char &a, const char &b);
int doOpp(const char &a, const char &b);

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		k = -1;
		memset(com, 0, sizeof (com));
		memset(opp, 0, sizeof (opp));
		memset(str, 0, sizeof (str));
		scanf("%d", &c);
		for (int j = 0; j < c; ++j)
			scanf("%s", com[j]);
		scanf("%d", &d);
		for (int j = 0; j < d; ++j)
			scanf("%s", opp[j]);
		scanf("%d ", &n);
		for (int j = 0; j < n; ++j)
		{
			scanf("%c", &elem);
			if (k == -1)
			{
				str[++k] = elem;
				continue;
			}
			if (doCom(elem, str[k]))
				continue;
			bool add = true;
			for (int l = 0; l <= k; ++l)
			{
				if (doOpp(elem, str[l]))
				{
					memset(str, 0, sizeof (str));
					k = -1;
					add = false;
					break;
				}
			}
			if (add)
				str[++k] = elem;
		}
		printf("Case #%d: [", i);
		for (int j = 0; j < k; ++j)
			printf("%c, ", str[j]);
		if (k != -1)
			printf("%c", str[k]);
		printf("]\n");
	}
}

int doCom(const char &a, const char &b)
{
	for (int i = 0; i < c; ++i)
	{
		if ((a == com[i][0] && b == com[i][1]) || (a == com[i][1] && b == com[i][0]))
		{
			str[k] = com[i][2];
			return 1;
		}
	}
	return 0;
}

int doOpp(const char &a, const char &b)
{
	for (int i = 0; i < d; ++i)
	{
		if ((a == opp[i][0] && b == opp[i][1]) || (a == opp[i][1] && b == opp[i][0]))
			return 1;
	}
	return 0;
}