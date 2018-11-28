#include "stdio.h"
#include "string.h"

char engin[102][102];
char query[1002][102];

int find(int i, int e)
{
	for (int k=1; k<=e; k++)
	{
		if (strcmp(query[i], engin[k]) ==0)
			return k;
	}
	return e;
}

int main()
{
	int t;
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	scanf("%d", &t);
	int now = 1;
	while(now <= t)
	{

		bool a[102] = {0};
		int e, q;
		scanf("%d\n", &e);
		int i = 1;

		while (i<=e)
		{
			gets(engin[i]);
			i++;
		}

		i=1;
		scanf("%d\n", &q);
		while(i <= q)
		{
			gets(query[i]);
			i++;
		}


		int count=0;
		int min=0;
		for (i=1; i<=q; i++)
		{
			int p = find(i,e);
			if (!a[p])
			{
				a[p] = true;
				count++;
				if (count == e)
				{
					min++;
					memset(a, 0, sizeof(a));
					count=1;
					a[p] = true;
				}
			}
		}
		printf("Case #%d: %d\n", now, min);
		now++;
	}

	return 0;
}