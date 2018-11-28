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
    int N;
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
        N = atoi(subtoken);

        int totaltime=0;
        int opos=1;
        int bpos=1;
        int currentseqtime=0;
        int swap=0;

        subtoken = strtok_r(NULL, " ", &sptr2);
        char *myturn = subtoken;

        for (j=0; j<N; j++)
        {
            subtoken = strtok_r(NULL, " ", &sptr2);
            newpos = atoi(subtoken);
            if (strcmp(myturn,"O") == 0) // orange
            {
                if (swap)
                {
//printf("SWAP to ORANGE!             adding cur = %d, new total = %d\n", currentseqtime, currentseqtime+totaltime);
                    totaltime += currentseqtime;
                    if (currentseqtime < abs(newpos-opos)) // no need to account for travel
                    {
                        currentseqtime = abs(newpos-opos) - currentseqtime + 1;
                    }
                    else
                    {
                        currentseqtime = 1;
                    }
                    swap = 0;
                }
                else
                {
                    currentseqtime += abs(newpos-opos) + 1;
                }
                opos = newpos;
//printf("orange:   new pos = %d, cur = %d\n", opos, currentseqtime);
            }
            else
            {
                if (swap)
                {
//printf("SWAP to BLUE!               adding cur = %d, new total = %d\n", currentseqtime, currentseqtime+totaltime);
                    totaltime += currentseqtime;
                    if (currentseqtime < abs(newpos-bpos)) // no need to account for travel
                    {
                        currentseqtime = abs(newpos-bpos) - currentseqtime + 1;
                    }
                    else
                    {
                        currentseqtime = 1;
                    }
                    swap = 0;
                }
                else
                {
                    currentseqtime += abs(newpos-bpos) + 1;
                }
                bpos = newpos;
//printf("blue  :   new pos = %d, cur = %d\n", bpos, currentseqtime);
            }
            if (j < N-1)
            {
                subtoken = strtok_r(NULL, " ", &sptr2);
                if (strcmp(myturn,subtoken) != 0) // changed
                {
                    myturn = subtoken;
                    swap = 1;
                }
            }
        }
        totaltime += currentseqtime;

        printf("Case #%d: %d\n", i+1, totaltime);
    }


    fclose(fp);
    return 0;
}
