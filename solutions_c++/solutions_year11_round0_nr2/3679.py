#include <stdio.h>
#include <memory.h>
#include <string.h>

int n, u, c, d;
char tmpc1, tmpc2, tmpc3;
int g[27][27], m[27][27];
;
void init()
{
	scanf("%d", &c);
	tmpc1 = getchar();
	memset(g, 0, sizeof(g));
	memset(m, 0, sizeof(m));
	for (int i = 0; i < c; i++)
	{
		tmpc1 = getchar();
		tmpc2 = getchar();
		tmpc3 = getchar();
		g[tmpc1 - 'A'][tmpc2 - 'A'] = tmpc3 - 'A' + 1;
		g[tmpc2 - 'A'][tmpc1 - 'A'] = tmpc3 - 'A' + 1;
		tmpc1 = getchar();
	}
	scanf("%d", &d);
	getchar();
	for (int i = 0; i < d; i++)
	{
		tmpc1 = getchar();
		tmpc2 = getchar();
		m[tmpc1 - 'A'][tmpc2 - 'A'] = -1;
		m[tmpc2 - 'A'][tmpc1 - 'A'] = -1;
		tmpc1 = getchar();
	}
	char ss[1000];
	strcpy(ss, "");
	scanf("%d", &n);
	tmpc1 = getchar();
	for (int i = 0; i < n; i++)
	{
		tmpc1 = getchar();
		while ((strlen(ss) >= 1) && g[ss[strlen(ss) - 1] - 'A'][tmpc1 - 'A']
				> 0)
		{
			ss[strlen(ss) - 1] = 'A' + g[ss[strlen(ss) - 1] - 'A'][tmpc1 - 'A']
					- 1;
			tmpc1 = ss[strlen(ss) - 1];
			ss[strlen(ss) - 1] = '\0';
		}
		int l = strlen(ss);
		ss[l] = tmpc1;
		ss[l + 1] = '\0';
		for (int j = 0; j < l; j++)
		{
			if (m[ss[j] - 'A'][ss[l] - 'A'] < 0)
			{
				strcpy(ss, "");
				break;
			}
		}
	}
	getchar();
	printf("Case #%d: [", u);
	if (strlen(ss) > 0)
	{
		printf("%c", ss[0]);
		int l;
		l = strlen(ss);
		for (int i = 1; i < l; i++)
		{
			printf(", %c", ss[i]);
		}
	}
	printf("]\n");
}
int main()
{
	freopen("/home/re/workspace/input.txt","r",stdin);
	freopen("/home/re/workspace/output.txt","w",stdout);
	int w;
	scanf("%d", &w);
	while (w--)
	{
		u++;
		init();
	}
	return 0;
}
