# include <stdio.h>
# include <string.h>
# include <stdlib.h>

char q[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'}, line[1000], *p;
int n, kase=0;

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.txt", "w", stdout);

	scanf("%d%*c", &n);

	while (n--)
	{
		printf("Case #%d: ",++kase);
		fgets(line, 1000, stdin);
		p=line;
		while (*p!='\n')
		{
			if (*p==' ') printf(" "); else printf("%c", q[*p-'a']);
			p++;
		}
		printf("\n");		
	}
}