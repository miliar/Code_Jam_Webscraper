#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

const int MAX = 100;

int nbTest;
int nbLignes;
int nbColonnes;
char chaine[MAX][MAX];


bool verifie()
{
	for(int i = 0; i < nbLignes; i++)
		for(int j = 0; j < nbColonnes; j++)
			if(chaine[i][j] == '#')
				return false;
	
	return true;
}

bool est_dedans(int lig, int col)
{
	if(lig >= 0 && lig+1 < nbLignes && col >= 0 && col+1 < nbColonnes)
		return true;
	else 
		return false;
}

void
explore_voisin(int lig, int col)
{
	if( est_dedans(lig, col) )
	{
		chaine[lig][col]     = '/';
		chaine[lig][col+1]   = '\\';
		chaine[lig+1][col]   = '\\';
		chaine[lig+1][col+1] = '/';
	}
}

void
couvre()
{
	for(int lig = 0; lig < nbLignes; lig++)
	{
		for(int col = 0; col < nbColonnes; col++)
		{
			if( est_dedans(lig, col) && chaine[lig][col] == '#' &&
				chaine[lig][col+1] == '#' &&
				chaine[lig+1][col] == '#' &&
				chaine[lig+1][col+1] == '#'
				)
			{
				explore_voisin(lig, col);
				
			}
		}
	}
}

void
init()
{
	scanf("%d", &nbTest);
	
	for(int test = 1; test <= nbTest; test++)
	{
		scanf("%d%d", &nbLignes, &nbColonnes);
		
		for(int lig = 0; lig < nbLignes; lig++)
		{
			scanf("%s", chaine[lig]);
		}
		
		couvre();
		
		printf("Case #%d:\n", test);
					
		if(verifie())
		{
			for(int i = 0; i < nbLignes; i++)
			{
				for(int j = 0; j < nbColonnes; j++)
				{
					printf("%c", chaine[i][j]);
				}
				printf("\n");
			}
		}
		
		else
		{
			printf("Impossible\n");
		}
		
		
	}
	
}

int
main()
{
	init();
	
	
	return 0;
}
