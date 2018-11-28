#include <stdio.h>
#include <cstring>
#include <iostream>

#define INF 999999

using namespace std;

int nb_tests, nengines, nquery, rez;
char engine[101][101], aux[101], query[1001][101];
int a[1003][103];

int main()
{
    FILE *fin = fopen("A.in", "r");
    FILE *fout = fopen("Aout.out", "w");
    fscanf(fin, "%d", &nb_tests);
    fgets(aux, 101, fin);
    for (int i = 1; i <= nb_tests; ++i)
    {
        memset(aux, 0, sizeof(aux));
        memset(query, 0, sizeof(query));
        memset(a, 0, sizeof(a));
        // engines
        memset(engine, 0, sizeof(engine));
        fscanf(fin, "%d", &nengines);
        fgets(aux, 101, fin);
        for (int j = 0; j < nengines; ++j)
            fgets(engine[j], 101, fin);
        // queries
        fscanf(fin, "%d", &nquery);
        fgets(aux, 101, fin);
        for (int j = 0; j < nquery; ++j)
            fgets(query[j], 101, fin);
        
        for (int j = 0; j < nquery; ++j)
           for (int k = 0; k < nengines; ++k) 
               a[j][k] = INF;
        for (int k = 0; k < nengines; ++k)
            if (strcmp(engine[k], query[0]) == 0)
                a[0][k] = INF;
            else
                a[0][k] = 0;
        for (int j = 1; j < nquery; ++j)
            for (int k = 0; k < nengines; ++k)
            {
                if (a[j-1][k] == INF) continue;
                if (strcmp(engine[k], query[j]) == 0)
                {
                    for (int q = 0; q < nengines; ++q)
                        if (q != k)
                            if (a[j][q] > a[j-1][k] + 1)
                                a[j][q] = a[j-1][k] + 1;
                }
                else
                {
                    if (a[j][k] > a[j-1][k])
                        a[j][k] = a[j-1][k];
                }
            }
        rez = INF;
        for (int q = 0; q < nengines; ++q)
            if (a[nquery-1][q] < rez)
                rez = a[nquery-1][q];
        fprintf(fout, "Case #%d: %d", i, rez);
        if (i != nb_tests) fprintf(fout, "\n");
    }
    fclose(fin);
    fclose(fout);
    
    return 0;
}

