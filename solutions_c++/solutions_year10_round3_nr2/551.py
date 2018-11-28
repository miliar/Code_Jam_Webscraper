#include <cstdio>

using namespace std;


int nbTests;
int deb, fin;
int C;
int reponse;
int debCk, finCk;
int ajout;



int main()
{
    freopen("small.in", "r", stdin);
    freopen("small.out", "w", stdout);


    scanf("%d", &nbTests);

    for (int test = 1; test <= nbTests; test++)
    {
        reponse = 0;
        scanf("%d %d %d", &deb, &fin, &C);

        while (deb*C < fin)
        {
            debCk = deb, finCk = fin;

            while (debCk < finCk)
            {
                ajout = 0;
                debCk *= C;
                if ((finCk%C) != 0)
                    ajout = 1;
                finCk = (finCk/C) + ajout;
            }

            fin = (debCk+finCk)/2;
            if ((debCk+finCk)%2 != 0)
                fin++;


            reponse++;
            //printf("finCk = %d, debCK = %d     ", finCk, debCk);

           // printf("tour numero = %d, deb = %d, fin = %d, C = %d\n", reponse, deb, fin, C);
        }

        printf("Case #%d: %d\n", test, reponse);
    }


    return 0;
}
