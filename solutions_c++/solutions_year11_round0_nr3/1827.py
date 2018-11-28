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
        N = atoi(token);


        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);

        long int total = 0;
        long int xortotal = 0;
        long int smallest = 1000000;

        for (j=0; j<N; j++)
        {
            long int val;
            subtoken = strtok_r((j==0)?token:NULL, " ", &sptr2);
            val = atol(subtoken);
            if (val < smallest) smallest = val;
            total += val;
            xortotal = xortotal ^ val;
        }

        if (xortotal != 0)
        {
            printf("Case #%d: NO\n", i+1);
        }
        else
        {
            printf("Case #%d: %ld\n", i+1, total - smallest);
        }
    }


    fclose(fp);
    return 0;
}
