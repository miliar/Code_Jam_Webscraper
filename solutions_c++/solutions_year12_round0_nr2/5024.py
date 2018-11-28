#include <cstdio>
#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <math.h>
#include <string.h>
#include <stdio.h>
#include <vector>

using namespace std;

FILE * pFile1, * pFile2;
int T,N,S,p,i,j,Dancer[100],Possible,Probable,Poss_limit,Prob_limit;
int main ()
{

        pFile1 = fopen ("B-large.in","r");
        pFile2 = fopen ("B-large.out","w");
        fscanf(pFile1, "%d", &T);
        for (i=1;i<=T;i++)
            {
                fscanf(pFile1, "%d", &N);
                fscanf(pFile1, "%d", &S);
                fscanf(pFile1, "%d", &p);
                fprintf (pFile2,"Case #%d: ", i);
                Possible = 0;Poss_limit = 3*p-2;
                Probable = 0;Prob_limit = 3*p-4;if(Prob_limit<0){Prob_limit = 1;}
                for (j=0;j<N;j++)
                {
                    fscanf(pFile1, "%d", &Dancer[j]);
                    if(Dancer[j]>=Poss_limit){Possible++;}else
                    {
                         if(Dancer[j]>=Prob_limit){Probable++;}
                    }
                }
                if(Probable<=S){Possible = Possible + Probable;} else {Possible = Possible + S;}
                fprintf (pFile2,"%d\n", Possible);
            }
            
        fclose(pFile1);
        fclose(pFile2);

        return 0;
}
