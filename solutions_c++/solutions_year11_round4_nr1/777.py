#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;


long double rep, runTimeLeft;
int nbTests, nbBonus, walkSpeed, runSpeed, tailleToDo, runTime;
int distVide;


struct s_bonus
{
    int deb;
    int fin;
    int speed;


    s_bonus() {}

    s_bonus (int a, int b, int c)
    {
        deb = a;
        fin = b;
        speed = c;
    }


    bool operator < (const s_bonus &a) const
    {
        return speed < a.speed;
    }
};



s_bonus bonus[1000];

int main()
{
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);
    scanf("%d", &nbTests);
    int luDeb, luFin, luSpeed;
    long double distTmp, speedTmp, runSpeedTmp, walkSpeedTmp;



    for (int test = 1; test <= nbTests; test++)
    {
        scanf("%d %d %d", &tailleToDo, &walkSpeed, &runSpeed);
        scanf("%d %d", &runTime, &nbBonus);

        distVide = tailleToDo;
        runTimeLeft = runTime;
        rep = 0;
        runSpeedTmp = runSpeed;
        walkSpeedTmp = walkSpeed;

        for (int bon = 0; bon < nbBonus; bon++)
        {
            scanf("%d %d %d", &bonus[bon].deb, &bonus[bon].fin, &bonus[bon].speed);
            distVide -= (bonus[bon].fin - bonus[bon].deb);
        }


        sort(bonus, bonus+nbBonus);
        if (bonus[0].speed > bonus[nbBonus-1].speed)
            exit(43);

        if (runTimeLeft < ((long double) distVide)/(long double)runSpeed)
        {

            rep = runTime + ((long double)distVide - runTimeLeft*runSpeedTmp)/walkSpeedTmp;
            runTimeLeft = -1;
        }

        else
        {
            rep = ((long double) distVide)/runSpeedTmp;
            runTimeLeft -= rep;
        }

        for (int i = 0; i < nbBonus; i++)
        {
            distTmp = bonus[i].fin - bonus[i].deb;


            if (runTimeLeft >= 0)
            {
                speedTmp = bonus[i].speed + runSpeedTmp;
                if (runTimeLeft < distTmp/speedTmp)
                {
                    rep += runTimeLeft + (distTmp - runTimeLeft*speedTmp)/(walkSpeedTmp + bonus[i].speed);
                    runTimeLeft = -1;
                }

                else
                {
                    rep += distTmp/speedTmp;
                    runTimeLeft -= distTmp/speedTmp;
                }
            }

            else
            {
                speedTmp = walkSpeedTmp + bonus[i].speed;
                rep += distTmp/speedTmp;
            }
        }



        printf("Case #%d: %llf\n", test, rep);

    }






    return 0;
}
