#include <cstdio>
int y, x, test, qt;
char tab[51][51], eol;

int main()
{
	scanf("%d", &test);
	for(int t=0; t<test; t++)
	{
		qt=0;
		scanf("%d%d%c", &y, &x, &eol);
		for(int i=0; i<y; i++)
		{
			for(int j=0; j<x; j++)
			{
				scanf("%c", &tab[i][j]);
				if(tab[i][j]=='#') qt++;
			}
			scanf("%c", &eol);
		}
		for(int i=0; i<y-1; i++)
			for(int j=0; j<x-1; j++)
			{
				if(tab[i][j]=='#' && tab[i][j+1]=='#' && tab[i+1][j]=='#' && tab[i+1][j+1]=='#')
				{
					qt-=4;
					tab[i][j]='/'; tab[i][j+1]='\\';
					tab[i+1][j]='\\'; tab[i+1][j+1]='/';
				}
			}
		printf("Case #%d:\n", t+1);
		if(qt>0) printf("Impossible\n");
		else 		
			for(int i=0; i<y; i++)
			{
				for(int j=0; j<x; j++)
					printf("%c", tab[i][j]);
				printf("\n");
			}
	}
	
	return 0;
}
