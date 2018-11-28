#include <cstdio>
#include <stack>

using namespace std;


char opposed[30][2];
int nbOpposed;
int nbChar;
char combine[40][3];
int nbCombine;
int nbElems;
char liste[200];


int dejaVu[256];



char testCombine(char c1, char c2)
{
    for (int i = 0; i < nbCombine; i++)
    {
        if ((combine[i][0] == c1 && combine[i][1] == c2) || (combine[i][0] == c2 && combine[i][1] == c1))
            return combine[i][2];
    }

    return -1;
}


bool testClear(char c)
{
    char opposant;
    for (int j = 0; j < nbOpposed; j++)
    {
        if (opposed[j][0] == c)
            opposant = opposed[j][1];
        else if (opposed[j][1] == c)
            opposant = opposed[j][0];
        else
            continue;

        if (c == opposant && dejaVu[c] > 1)
            return true;
        else if (dejaVu[opposant] > 0)
            return true;
    }


    return false;
}


void update(void)
{
    if (nbElems < 2)
        return;

    char retTestComb = testCombine(liste[nbElems-1], liste[nbElems-2]);
    if (retTestComb > 0)
    {
        dejaVu[liste[nbElems-1]]--;
        dejaVu[liste[nbElems-2]]--;
        liste[nbElems-2] = retTestComb;
        dejaVu[retTestComb]++;
        nbElems--;
    }

    if (testClear(liste[nbElems-1]))
    {
        nbElems = 0;
        for (int j = 'A'; j <= 'Z'; j++)
            dejaVu[j] = 0;
    }
}






int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int nbCases;
    scanf("%d", &nbCases);



    bool efface;
    char newCombine;

    char carLu;




    for (int i = 1; i <= nbCases; i++)
    {
        scanf("%d", &nbCombine);
        for (int k = 0; k < nbCombine; k++)
        {
            getchar();
            for (int j = 0; j < 3; j++)
                scanf("%c", &combine[k][j]);
        }

        scanf("%d", &nbOpposed);
        for (int k = 0; k < nbOpposed; k++)
        {
            getchar();
            scanf("%c%c", &opposed[k][0], &opposed[k][1]);
        }

        scanf("%d", &nbChar);


        getchar();

        nbElems = 0;
        for (int j = 'A'; j <= 'Z'; j++)
            dejaVu[j] = 0;




        for (int j = 0; j < nbChar; j++)
        {
            carLu = getchar();
            liste[nbElems] = carLu;
            dejaVu[carLu]++;
            nbElems++;

           update();
        }

        printf("Case #%d: [", i);
        for (int l = 0; l < nbElems-1; l++)
            printf("%c, ", liste[l]);
        if (nbElems > 0)
            printf("%c", liste[nbElems-1]);
        printf("]\n");
    }


    return 0;
}
