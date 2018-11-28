#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>

#define BUFSZ 10000


int main(int argc, char *argv[])
{
    FILE *fp;
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1, *sptr2;
    int T;       // loops
    int N, pd, pg;
    int newpos;
    int i, j;

    if (argc != 2)
    {
        exit(-1);
    }
    fp = fopen(argv[1], "r");
    if (fp == NULL)
    {
        printf("Usage: file is no good\n");
        exit(-1);
    }


    fgets(strBuf, BUFSZ, fp);
    token = strtok_r(strBuf, "\r\n", &sptr1);
    T = atoi(token);

    for (i=0; i<T; i++)
    {
        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);

        subtoken = strtok_r(token, " ", &sptr2);
        if (strlen(subtoken) < 3) // garbage
            N = atoi(subtoken);
        else
            N=50;

        subtoken = strtok_r(NULL, " ", &sptr2);
        pd = atoi(subtoken);

        subtoken = strtok_r(NULL, " ", &sptr2);
        pg = atoi(subtoken);

        // lifetime loser
        if (pg == 0)
        {
            // must be total loser today
            if (pd == 0)
                printf("Case #%d: Possible\n", i+1);
            else
                printf("Case #%d: Broken\n", i+1);
            continue;
        }

        // lifetime champ
        if (pg == 100)
        {
            // must be champ today
            if (pd == 100)
                printf("Case #%d: Possible\n", i+1);
            else
                printf("Case #%d: Broken\n", i+1);
            continue;
        }

        int minlossestoday;
        if (pd == 0) minlossestoday = 1;
        else if (pd == 100) minlossestoday = 0;
        else if (pd % 50 == 0 && N >= 2) minlossestoday = (100-pd)*2/100;
        else if (pd % 25 == 0 && N >= 4) minlossestoday = (100-pd)*4/100;
        else if (pd % 20 == 0 && N >= 5) minlossestoday = (100-pd)*5/100;
        else if (pd % 10 == 0 && N >= 10) minlossestoday = (100-pd)*10/100;
        else if (pd % 5 == 0 && N >= 20) minlossestoday = (100-pd)*20/100;
        else if (pd % 4 == 0 && N >= 25) minlossestoday = (100-pd)*25/100;
        else if (pd % 2 == 0 && N >= 50) minlossestoday = (100-pd)*50/100;
        else
        {
            printf("Case #%d: Broken\n", i+1);
            continue;
        }

        /*
        int absminlost;
        if      (pg % 50 == 0) absminlost = (100-pg)*2/100;
        else if (pg % 25 == 0) absminlost = (100-pg)*4/100;
        else if (pg % 20 == 0) absminlost = (100-pg)*5/100;
        else if (pg % 10 == 0) absminlost = (100-pg)*10/100;
        else if (pg % 5 == 0) absminlost = (100-pg)*20/100;
        else if (pg % 4 == 0) absminlost = (100-pg)*25/100;
        else if (pg % 2 == 0) absminlost = (100-pg)*50/100;
        else absminlost = 100-pg;

        if (minlossestoday <= absminlost)
        */
            printf("Case #%d: Possible\n", i+1);
            /*
        else
            printf("Case #%d: Broken\n", i+1);
            */
    }


    fclose(fp);
    return 0;
}
