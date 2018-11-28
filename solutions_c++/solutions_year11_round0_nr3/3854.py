#include <cstdio>
#include <fstream>
#include <iostream>
#include <stdlib.h>
using namespace std;

FILE * pFile1, * pFile2;
int A, T, TC, K, N, M, i, j, n;
int C[1000];
string ligne;

int main ()
{

        pFile1 = fopen ("C-small.in","r");
        pFile2 = fopen ("C-small.out","w");
        fscanf(pFile1, "%d", &T);
        for (i=1;i<=T;i++)
            {
                fscanf(pFile1, "%d", &N);
                for(j=1;j<=N;j++)
                    {
                        fscanf(pFile1, "%d", &C[j]);
                    }
                A = 0;
                for(j=1;j<=N;j++)
                    {
                        A^=C[j];
                    }
                if (A != 0) {fprintf (pFile2,"Case #%d: %s\n", i, "NO");} else
                            {
                                     n = 1000000;
                                     for(j=1;j<=N;j++){if (C[j]<n) n = C[j];}
                                     A = 0;
                                     for(j=1;j<=N;j++){A+=C[j];}
                                     A-=n;
                                     fprintf (pFile2,"Case #%d: %d\n", i, A);
                            }
            }
            
        fclose(pFile1);
        fclose(pFile2);

        return 0;
}
