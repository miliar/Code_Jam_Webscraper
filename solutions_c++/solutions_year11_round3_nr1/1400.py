#include <cstdlib>
#include <cstdio>
#include <algorithm>

using namespace std;
int nbLignes, nbCols;
int nbTests;
char tab[100][100];

int main()
{
	scanf("%d\n", &nbTests);
	for(int t = 1; t <= nbTests; t++)
	{
		int nb = 0;
		scanf("%d %d\n", &nbLignes, &nbCols);
		for(int i = 0; i < nbLignes; i++)
		{
			for(int j = 0; j < nbCols; j++)
			{
				char c = getchar();
				if(c=='#')nb++;
				tab[i][j]=c;
				if(i>0&&j>0&&tab[i][j]=='#'&&tab[i-1][j]=='#'&&tab[i-1][j-1]=='#'&&tab[i][j-1]=='#')
				{
					tab[i-1][j]=tab[i][j-1]='\\';
					tab[i-1][j-1]=tab[i][j]='/';
					nb-=4;
				}
			}
			getchar();
		}
		printf("Case #%d:\n", t);
		if(nb!=0)puts("Impossible");
		else
		{
			for(int i = 0; i < nbLignes; i++)
			{
				for(int j = 0; j < nbCols; j++)
					putchar(tab[i][j]);
				putchar('\n');
			}
		}
	}

	return 0;
}

