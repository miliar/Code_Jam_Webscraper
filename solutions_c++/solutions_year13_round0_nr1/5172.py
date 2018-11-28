#include <stdio.h>

#define MAX 4

int check(char s, char tab[MAX][MAX])
{
	int j;
	for(int i=0; i<MAX; ++i)
	{
		for(j=0; j<MAX && (tab[i][j]==s || tab[i][j]=='T') ; ++j);
		if(j==MAX)
			return 1;
		for(j=0; j<MAX && (tab[j][i]==s || tab[j][i]=='T') ; ++j);
		if(j==MAX)
			return 1;
	}
	
	for(j=0; j<MAX && (tab[j][j]==s || tab[j][j]=='T') ; ++j);
	if(j==MAX)
		return 1;

	for(j=0; j<MAX && (tab[j][MAX-j-1]==s || tab[j][MAX-j-1]=='T') ; ++j);
	if(j==MAX)
		return 1;

	return 0;
}

int main()
{
	int t;

	scanf("%d",&t);

	for(int ccnt =1; ccnt <=t; ++ccnt)
	{
		char tab[MAX][MAX];
		int tmp =0;
		for(int i=0; i<MAX; ++i)
			for(int j=0; j<MAX; ++j)
			{
				scanf(" %c",&tab[i][j]);
				if(tab[i][j] == '.')
					tmp =1;
			}

		printf("Case #%d: ",ccnt);

		if(check('X',tab))
			printf("X won\n");
		else if(check('O',tab))
			printf("O won\n");
		else if(tmp)
			printf("Game has not completed\n");
		else
			printf("Draw\n");
	}
	return 0;
}

