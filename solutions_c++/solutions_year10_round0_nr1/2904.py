#include <cstdio>

using namespace std;

bool allume[10002][32];
bool continuer;
int nbLights, nbSnaps, nbTests;

int saveNbNeeded[32];
bool dejaVu[32];

int main()
{
    freopen("inputLarge.in", "r", stdin);
    freopen("outputLarge.out", "w", stdout);

    int car;
    scanf("%d ", &nbTests);
    for (int curTest = 1; curTest <= nbTests; curTest++)
    {

        continuer = true;

        scanf("%d %d", &nbLights, &nbSnaps);
        int cptSnaps = 0, cptAllumes = 0;

        if (dejaVu[nbLights] == true)
        {
            cptAllumes = nbLights;
            cptSnaps = saveNbNeeded[nbLights];
        }
        while (cptAllumes != nbLights)
        {
            cptAllumes = 0;
            int curL = 0;
            for (; allume[curTest][curL] == true && curL < nbLights; curL++)
            {
                allume[curTest][curL] = false;
            }
            allume[curTest][curL] = true;

            for (int curLu = 0; curLu < nbLights; curLu++)
            {
                if (allume[curTest][curLu] == true)
                    cptAllumes++;
                else
                    break;
            }

            cptSnaps++;
        }
        saveNbNeeded[nbLights] = cptSnaps;
        dejaVu[nbLights] = true;

        if (nbSnaps%(cptSnaps+1) == cptSnaps)
            printf("Case #%d: ON\n", curTest);
        else
            printf("Case #%d: OFF\n", curTest);
    }


    return 0;
}
