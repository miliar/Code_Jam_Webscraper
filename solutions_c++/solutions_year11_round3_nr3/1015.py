#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int nbTest;
int nbjoueurs;
int bas;
int haut;

int joueurs[100000];

int
verifie()
{
	for(int freq = bas; freq <= haut; freq++)
	{
		bool convient = true;
		for(int joueur = 0; joueur < nbjoueurs; joueur++)
		{
			if(!(0 == (joueurs[joueur] % freq)) && !(0 == (freq % joueurs[joueur])))
				convient = false;
		}
		if(convient)
			return freq;
	}
	
	return -1;
}

void
init()
{
	scanf("%d", &nbTest);
	
	for(int test = 1; test <= nbTest; test++)
	{
		scanf("%d%d%d", &nbjoueurs, &bas, &haut);
		
		for(int joueur = 0; joueur < nbjoueurs; joueur++)
			scanf("%d", &joueurs[joueur]);
		
		printf("Case #%d: ", test);
		
		int valeur = verifie();
		
		if(valeur != -1)
			printf("%d\n", valeur);
		else
			printf("NO\n");
	}
	
}

int
main()
{
	init();
	
	
	return 0;
}
