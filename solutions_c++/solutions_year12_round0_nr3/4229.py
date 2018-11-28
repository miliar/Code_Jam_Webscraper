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
int T,A,B,i,j,k,u,t,dig,dig2,rep,puiss,Possible;
int maxim, maximus[4];
int main ()
{

        pFile1 = fopen ("C-small-attempt0.in","r");
        pFile2 = fopen ("C-small.out","w");
        maximus[0]=0;
        maximus[1]=0;
        maximus[2]=0;
        maximus[3]=0;
        fscanf(pFile1, "%d", &T);
        for (i=1;i<=T;i++)
            {
                fscanf(pFile1, "%d", &A);
                fscanf(pFile1, "%d", &B);
                dig = log(A)/log(10) + 1;
                fprintf (pFile2,"Case #%d: ", i);
                if(dig<2){fprintf (pFile2,"0\n");} else
                {
                  Possible = 0;
                  for(j=A;j<B;j++)
                  {
                       //printf("j=: %d\n",j);
                       for(k=1;k<dig;k++)
                       {
                            puiss = pow(10,k);
                            t = puiss%10;
                            if(t!=0){puiss++;}
                            u = j%puiss;
                            
                            maxim = j-u;
                            
                            maxim = maxim/puiss;
                            
                            puiss = pow(10,dig-k);
                            t = puiss%10;
                            if(t!=0){puiss++;}
                            maxim = maxim + u*puiss;
                            maximus[k-1]=maxim;
                            rep = 0;
                            if(k>1)
                            {
                               for(t=0;t<k-1;t++)
                               {
                                    if(maximus[t]==maxim){rep=1;}
                               }
                            }
                            dig2 = log(maxim)/log(10) + 1;
                            if((j<maxim)&(maxim<=B)&(dig2==dig)&(rep==0)){Possible++;}
                            
                       }   
                  }
                
                  fprintf (pFile2,"%d\n", Possible);
                }
            }
            
        fclose(pFile1);
        fclose(pFile2);

        return 0;
}
