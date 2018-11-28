#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define MAXWORDLEN  20
#define MAXLINELEN  1024

int main(int argc, char * argv[])
{
    FILE * fp = fopen(argv[1], "r");
    if (NULL == fp)
    {
        printf("Input File Not Exist!\n");
        return 1;
    }
    FILE * fOut = fopen("output.txt", "w");
    if (NULL == fOut)
    {
        printf("Cannot Open Output File!\n");
        fclose(fp);
        return 1;
    }

    int T;
    fscanf(fp, "%d", &T);
    for (int i=0; i<T; i++)
    {
        int R, K, N;
        fscanf(fp, "%d %d %d", &R, &K, &N);
        long long * G = new long long[N];
        long long * GEuro = new long long[N];
        long long * GNext = new long long[N];

        for (int j=0; j<N; j++)
        {
            fscanf(fp, "%lld", G+j);
        }

        long long money = 0;
        int startID = 0;
        int endID = 0;
        int once = 0;
        for (int j=0; j<N; j++)
        {
            once = 0;
            startID = j;
            endID = j;
            while (once < K)
            {
                once += G[endID];
                if (once > K)
                {
                    once -= G[endID];
                    break;
                }
                endID = (endID+1)%N;
                if (endID == startID)
                {
                    break;
                }
            }
            GEuro[j] = once;
            GNext[j] = endID;
            //printf ("%d: Euro-%d\t Next-%d\n", j, GEuro[j], GNext[j]);
        }

        int index = 0;
        for (int j=0; j<R; j++)
        {
            money += GEuro[index];
            index = GNext[index];
        }

        fprintf(fOut, "Case #%d: %lld\n", i+1, money);
        delete [] G;
        delete [] GEuro;
        delete [] GNext;
    }
    
    fclose(fp);
    fclose(fOut);
    return 0;
}
