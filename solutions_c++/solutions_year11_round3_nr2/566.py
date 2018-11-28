#include <iostream>
#include <cstdio>



using namespace std;



int nbStar, nbTest, nbDist, nbBoost, tpsBuild;
int dists[1000];
int bestTps;



void calcRec(int nbBoostLeft, int idStarFrom, int tps, bool boostActive)
{


    if (idStarFrom == nbStar)
    {
        if (tps < bestTps)
            bestTps = tps;
        return;
    }


    int distToNext = dists[idStarFrom%nbDist];


    if (boostActive)
    {
        if (tpsBuild <= tps)
            tps += distToNext;
        else if (tpsBuild > (tps + 2*distToNext))
            tps += 2*distToNext;
        else
        {
            //tps += (2*(tpsBuild-tps) + (tps+distToNext-tpsBuild))
            tps += (tpsBuild - tps + (distToNext - tpsBuild/2 + tps/2));
        }
    }

    else
        tps += 2*distToNext;

    if (nbBoostLeft > 0)
        calcRec(nbBoostLeft-1, idStarFrom+1, tps, true);

    calcRec(nbBoostLeft, idStarFrom+1, tps, false);
}




int main()
{
    freopen("small.in", "r", stdin);
    freopen("small.out", "w", stdout);


    scanf("%d", &nbTest);

    for (int test = 1; test <= nbTest; test++)
    {
        scanf("%d %d %d %d", &nbBoost, &tpsBuild, &nbStar, &nbDist);
        for (int i = 0; i < nbDist; i++)
            scanf("%d", &dists[i]);

        bestTps = 1<<30;
        calcRec(nbBoost, 0, 0, false);
        if (nbBoost > 0)
            calcRec(nbBoost-1, 0, 0, true);

        printf("Case #%d: %d\n", test, bestTps);
    }




    return 0;
}
