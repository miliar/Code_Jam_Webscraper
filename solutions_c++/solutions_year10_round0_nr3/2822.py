#include <cstdio>
#include <queue>

using namespace std;



queue<int> file;
int tailleGrps[1000], nbTests, nbGrps, nbTours, nbPlaces, sommeGagnee;

int main()
{
    freopen("inputSmall.in", "r", stdin);
    freopen("outputSmall.in", "w", stdout);


    int curPlacesLeft;
    int curTaille;
    scanf("%d", &nbTests);

    for (int test = 1; test <= nbTests; test++)
    {
        sommeGagnee = 0;
        scanf("%d %d %d", &nbTours, &nbPlaces, &nbGrps);
        for (int curGrpLu = 0; curGrpLu < nbGrps; curGrpLu++)
        {
            scanf("%d", &tailleGrps[curGrpLu]);
            file.push(tailleGrps[curGrpLu]);
        }

        for (int curTour = 0; curTour < nbTours; curTour++)
        {
            curPlacesLeft = nbPlaces;
            for (int curGrp = 0; curGrp < nbGrps && file.front() <= curPlacesLeft; curGrp++)
            {
                curTaille = file.front();
                file.pop();
                sommeGagnee += curTaille;
                file.push(curTaille);
                curPlacesLeft -= curTaille;
            }
        }
        while (file.empty() == false)
            file.pop();

        printf("Case #%d: %d\n", test, sommeGagnee);

    }



    return 0;
}
