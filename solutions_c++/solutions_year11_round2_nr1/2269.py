#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

const int MAX_TEAM = 100;
const int NON_VU = -1;

int nbTest;
int nbTeam;
char chaine[10*MAX_TEAM][10*MAX_TEAM];
int terrain[MAX_TEAM][MAX_TEAM];
double rpi[MAX_TEAM];

void
afficheTerrain()
{
	for(int i = 0; i < nbTeam; i++)
	{
		for(int j = 0; j < nbTeam; j++)
		{
			printf("%d ", terrain[i][j]);
		}
		printf("\n");
	}
}

double owp[MAX_TEAM];

double
calcule_wp(int team)
{
	int nbParties = 0;
	int nbGain = 0;
	
	for(int adversaire = 0; adversaire < nbTeam; adversaire++)
	{
		if(terrain[team][adversaire] != NON_VU)
			nbParties++;
		if(terrain[team][adversaire] == 1)
			nbGain++;
	}
	
	return (double)((double)nbGain / (double)nbParties);
}

double
calcule_owp(int team)
{
	
	double average_wp = 0.;
	int nbAdversaire = 0;
	
	for(int adv = 0; adv < nbTeam; adv++)
	{
		if(adv != team) {
			
		if(terrain[team][adv] != NON_VU)
		{
			
		double adv_wp;
		
		int v = terrain[adv][team];
		terrain[adv][team] = NON_VU;

		adv_wp = calcule_wp(adv);
		
		terrain[adv][team] = v;
		
		average_wp = average_wp + adv_wp;
		
		nbAdversaire++;
		}
			
		}
	}
	
	owp[team] = (double)(average_wp / (double)(nbAdversaire));
	return (double)(average_wp / (double)(nbAdversaire));
}

double
calcule_oowp(int team)
{
	double moyenne = 0.;
	int nbAdversaire = 0;
	
	
	for(int adv = 0; adv < nbTeam; adv++)
	{
		if(adv != team)
		{
			if(terrain[team][adv] != NON_VU)
			{
				moyenne = moyenne + owp[adv];
				nbAdversaire++;
			}
			
		
		}
	}
	
	return (double)(moyenne / (double)(nbAdversaire));
}

void
init_owp()
{
	for(int i = 0; i < nbTeam; i++)
		owp[i] = NON_VU;
}

int
main()
{
	scanf("%d", &nbTest);
	for(int test = 1; test <= nbTest; test++)
	{
		scanf("%d", &nbTeam);
		for(int team = 0; team < nbTeam; team++)
			scanf("%s", chaine[team]);
		
		for(int i = 0; i < nbTeam; i++)
		{
			int pos = 0;
			
			while(chaine[i][pos] != '\0')
			{
				
				if(chaine[i][pos] == '.')
				{
					terrain[i][pos] = NON_VU;
				}
				
				if(chaine[i][pos] == '1')
				{
					terrain[i][pos] = 1;
				}
				
				if(chaine[i][pos] == '0')
				{
					terrain[i][pos] = 0;
				}
				
				pos++;
			}
			
		}
		
//		afficheTerrain();
		
		printf("Case #%d:\n", test);
		
		init_owp();
		
		for(int team = 0; team < nbTeam; team++)
		{
			rpi[team] = 0.25 * calcule_wp(team) + 0.50 * calcule_owp(team);
		}
		
		for(int team = 0; team < nbTeam; team++)
		{
			rpi[team] += 0.25 * calcule_oowp(team);
			
			printf("%lf\n", rpi[team]);
		}
		
	}
	
	
	return 0;
}
