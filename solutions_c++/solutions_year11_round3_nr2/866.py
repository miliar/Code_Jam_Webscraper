#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>
#include <list>

#define BUFSZ 10000


int main(int argc, char *argv[])
{
    FILE *fp;
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1, *sptr2;
    int T;       // loops
    int L, N, C;
    long long t;
    long long time;
    int a[1000];
    int i, j, k;

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

    char outbuf[3000];
    for (i=0; i<T; i++)
    {
        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);

        subtoken = strtok_r(token, " ", &sptr1);
        L = atoi(subtoken);

        subtoken = strtok_r(NULL, " ", &sptr1);
        t = atoll(subtoken);
        // t is even

        subtoken = strtok_r(NULL, " ", &sptr1);
        N = atoi(subtoken);

        subtoken = strtok_r(NULL, " ", &sptr1);
        C = atoi(subtoken);

        int remaining = N%C;
        int loops = N/C;
        int loopdist = 0;
        int max = 0;
        int partialdist = 0;
        int maxind;
        std::list<int> mylist;
        std::list<int> partiallist;

        for (j=0; j<C; j++)
        {
            subtoken = strtok_r(NULL, " ", &sptr1);
            a[j] = atoi(subtoken);
            mylist.push_back(a[j]);
            if (a[j] > max)
            {
                max = a[j];
                maxind = j;
            }
            loopdist += a[j];
            if (j < remaining) partialdist += a[j];
        }

        time = (loopdist * loops + partialdist) * 2;

        if (L == 0 || t > time)
        {
            // done
        }
        else
        {
            long long timeremaining = time - t;
            long long remainingloops = (timeremaining/2) / loopdist;
            long long remainingpartial = (timeremaining/2) % loopdist;

            int ind = remaining;
            if (ind == 0) ind = C;
            while (remainingpartial > 0)
            {
                if (remainingpartial >= a[ind-1])
                {
                    remainingpartial -= a[ind-1];
                    partiallist.push_back(a[ind-1]);
                    ind--;
                    if (ind == 0) ind = C;
                }
                else
                {
                    partiallist.push_back(remainingpartial);
                    remainingpartial = 0;
                }
            }
            partiallist.sort();
            partiallist.reverse();
            mylist.sort();
            mylist.reverse();

            if (L < remainingloops)
            {
                // assign boosters to longest legs
                // time saved for each booster = max
                time -= L * mylist.front();
            }
            else
            {
                while (L > 0 && (!mylist.empty() || !partiallist.empty()))
                {
                    if (mylist.empty() ||
                        (!partiallist.empty() &&
                         partiallist.front() > mylist.front()))
                    {
                        time -= partiallist.front();
                        partiallist.pop_front();
                        L--;
                    }
                    else if (partiallist.empty() ||
                             (!mylist.empty() &&
                              partiallist.front() <= mylist.front()))
                    {
                        if (L < remainingloops)
                        {
                            time -= L * mylist.front();
                            L = 0;
                        }
                        else
                        {
                            time -= remainingloops * mylist.front();
                            mylist.pop_front();
                            L -= remainingloops;
                        }
                    }
                }
            }
        }

        printf("Case #%d: %lld\n", i+1, time);
    }


    fclose(fp);
    return 0;
}
