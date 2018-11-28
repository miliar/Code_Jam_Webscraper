#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstdio>


using namespace std;


vector<int> voisins[401];
int nbPlanetes, nbAretes, nbTests;

int bestConq, bestThreat;


bool dejaConq[401];
int dejaThreat[401];


int calcThreat(void)
{
	int ret = 0;
	for (int i = 2; i < nbPlanetes; i++)
	{
		if (dejaThreat[i] > 0 && !dejaConq[i])
			ret++;
	}

	return 1+ret;
}



void aux(int nbVus, int curPlanete)
{
	if (curPlanete == 1)
	{
		if (nbVus < bestConq)
		{
			bestConq = nbVus;
			bestThreat = calcThreat();
		}


		else if (nbVus == bestConq)
		{
			int nbThreat = calcThreat();
			if (nbThreat > bestThreat)
				bestThreat = nbThreat;
		}
		return;
	}

	else if (nbVus >= bestConq)
		return;


	int nbVoisins = voisins[curPlanete].size(), idVoisin;
	for (int i = 0; i < nbVoisins; i++)
		dejaThreat[voisins[curPlanete][i]]++;





	for (int i = 0; i < nbVoisins; i++)
	{
		idVoisin = voisins[curPlanete][i];
		if (!dejaConq[idVoisin])
		{
			dejaConq[curPlanete] = true;
			aux(nbVus+1, idVoisin);
			dejaConq[curPlanete] = false;
		}
	}



	for (int i = 0; i < nbVoisins; i++)
		dejaThreat[voisins[curPlanete][i]]--;


}


int main()
{
	freopen("small.in", "r", stdin);
	//freopen("small.out", "w", stdout);
	scanf("%d", &nbTests);

	char truc;
	int p1, p2;


	for (int test = 1; test <= nbTests; test++)
	{
		scanf("%d %d", &nbPlanetes, &nbAretes);
		bestConq = nbPlanetes;
		bestThreat = 0;


		for (int i = 0; i < nbAretes; i++)
		{
			scanf("%d %c %d", &p1, &truc, &p2);
			voisins[p1].push_back(p2);
			voisins[p2].push_back(p1);

		}
		aux(-1, 0);
		for (int i = 0; i < nbPlanetes; i++)
		{
			voisins[i].clear();
			dejaConq[i] = false;
			dejaThreat[i] = 0;
		}

	printf("Case #%d: %d %d\n", test, bestConq, bestThreat);

	}


    return 0;
}
