#include <cstdio>
#include <algorithm>
using namespace std;

const int MAX_GROUPES = 1000 + 1;

typedef unsigned long long int ull;

int tailleGroupe[MAX_GROUPES];
int saut[MAX_GROUPES];
ull nbEntrees[MAX_GROUPES];

int main()
{
    int nbTests = 0;
    scanf("%d", &nbTests);
    for (int test = 0; test < nbTests; test++)
    {
	int nbTours = 0, nbPlaces = 0, nbGroupes = 0;
	scanf("%d%d%d", &nbTours, &nbPlaces, &nbGroupes);

	for (int groupe = 0; groupe < nbGroupes; groupe++)
	    scanf("%d", &tailleGroupe[groupe]);

	for (int groupe = 0; groupe < nbGroupes; groupe++)
	{
	    int lgSaut = 0, oGroupe = groupe; 
	    ull taille = 0;
	    while (taille + tailleGroupe[oGroupe%nbGroupes] <= nbPlaces && lgSaut+1 <= nbGroupes)
	    {
		taille += tailleGroupe[oGroupe%nbGroupes];
		lgSaut++;
		oGroupe++;
	    }
	    saut[groupe] = lgSaut;
	    nbEntrees[groupe] = taille;
	}

	int groupeTete = 0;
	ull nbEntreesTotal = 0;
	for (int tour = 0; tour < nbTours; tour++)
	{
	    groupeTete %= nbGroupes;
	    nbEntreesTotal += nbEntrees[groupeTete];
	    groupeTete += saut[groupeTete];
	}

	printf("Case #%d: %llu\n", test + 1, nbEntreesTotal);
    }
}
