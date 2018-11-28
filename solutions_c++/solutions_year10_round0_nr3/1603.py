#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>

#define BUFSZ 10000


long long int calcsubtotal(long int *g, int N, long int k, int ind, int &newind)
{
    long long int subtotal = 0;
    int i;
    int actualind = ind;

    for (i=0; i<N; i++)
    {
        if (subtotal + g[actualind] > k) break;
        subtotal += g[actualind];
        actualind++;
        if (actualind == N) actualind = 0;
    }
    newind = actualind;

    return subtotal;
}

// T test cases
// R rides
// k max seating
// N groups
int main(int argc, char *argv[])
{
    FILE *fp;
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1, *sptr2;
    int T;       // loops
    long int R;
    long int k;
    int N;
    long int g[1000];
    long long int total;
    long long int st[1000];
    int newindarray[1000];
    int i, j;
    int ind, newind;

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
        R = atol(subtoken);
        subtoken = strtok_r(NULL, " ", &sptr2);
        k = atol(subtoken);
        subtoken = strtok_r(NULL, " ", &sptr2);
        N = atoi(subtoken);

        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);

        for (j=0; j<N; j++)
        {
            st[j] = 0; // initialize subtotals
            subtoken = strtok_r(token, " ", &sptr2);
            g[j] = atol(subtoken);
            token = NULL;
        }

        ind = 0;
        total = 0;

        for (j=0; j<R; j++)
        {
            if (st[ind] == 0)
            {
                st[ind] = calcsubtotal(g, N, k, ind, newind);
                newindarray[ind] = newind;
            }
            else
            {
                newind = newindarray[ind];
            }
            total += st[ind];
            ind = newind;
        }

        printf("Case #%d: %lld\n", i+1, total);
    }


    fclose(fp);
    return 0;
}
