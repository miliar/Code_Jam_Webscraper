#include <stdio.h>
#include <string.h>

int com[30][30], opp[30][30];
int n, an;
char ans[110], str[110];

int main()
{
	int T, c, d, x, y, z, i, j, cas=0;
	scanf("%d", &T);
	while (T--)
	{
		memset(com, 0, sizeof(com));
		memset(opp, 0, sizeof(opp));
		
		scanf("%d", &c);
		while (c--)
		{
			scanf("%s", str);
			x=str[0]-'A';
			y=str[1]-'A';
			z=str[2]-'A';
			com[x][y]=com[y][x]=z;
		}
		scanf("%d", &d);
		while (d--)
		{
			scanf("%s", str);
			x=str[0]-'A';
			y=str[1]-'A';
			opp[x][y]=opp[y][x]=1;
		}
		scanf("%d", &n);
		scanf("%s", str);
		an=0;
		for (i=0; i<n; i++)
		{
			ans[++an]=str[i];
			if (an>=2)
			{
				x=ans[an]-'A';
				y=ans[an-1]-'A';
				if (com[x][y]!=0)
					ans[--an]=com[x][y]+'A';	
			}
			x=ans[an]-'A';
			for (j=1; j<an; j++)
			{
				y=ans[j]-'A';
				if (opp[x][y])
				{
					an=0;
					break;
				}
			}
		}
		printf("Case #%d: [", ++cas);
		for (i=1; i<=an; i++)
		  if (i==an) printf("%c", ans[i]);
		  else printf("%c, ", ans[i]);
		printf("]\n");  
	}
	return 0;
}