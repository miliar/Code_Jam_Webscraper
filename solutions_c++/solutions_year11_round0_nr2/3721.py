#include <cstdio>
#include <fstream>
#include <iostream>
#include <stdlib.h>
using namespace std;

FILE * pFile1, * pFile2;
int T, C, D, N, i, j, k, m, n, p;
char Combine[4], Opposite[3], Word[10];
char Result[10];

int main ()
{

        pFile1 = fopen ("B-small.in","r");
        pFile2 = fopen ("B-small.out","w");
        fscanf(pFile1, "%d", &T);
        for (i=1;i<=T;i++)
            {
                fscanf(pFile1, "%d", &C);
                if (C==1){fscanf(pFile1, "%s", &Combine);}
                fscanf(pFile1, "%d", &D);
                if (D==1){fscanf(pFile1, "%s", &Opposite);}
                fscanf(pFile1, "%d", &N);
                fscanf(pFile1, "%s", &Word);
                Result[0]=Word[0];
                m=1;
                for(j=1;j<N;j++)
                    {
                      if(m==0){Result[0]=Word[j];m=1;}else{if (((Result[m-1]==Combine[0])&&(Word[j]==Combine[1]))||((Word[j]==Combine[0])&&(Result[m-1]==Combine[1]))&&(C==1)){Result[m-1]=Combine[2];}else
                      {   
                          n=2;
                          if (D==1)
                          {
                             if (Word[j]==Opposite[0]){n=0;}
                             if (Word[j]==Opposite[1]){n=1;}
                          }
                          if (n!=2)
                          {
                                p=1;
                                for(k=0;k<m;k++){if (Result[k]==Opposite[1-n]){p=0;}}
                                if (p==0){m=0;}else{Result[m]=Word[j];m++;}
                          } else
                          {
                                Result[m]=Word[j];
                                m++;
                          }
                      }
                      }
                    }
                fprintf (pFile2,"Case #%d: [", i);
                if (m!=0)
                   {
                      fprintf (pFile2,"%c", Result[0]);
                      if (m>1)
                         {
                            for(k=1;k<m;k++){fprintf (pFile2,", %c", Result[k]);}
                         }
                   }
                fprintf (pFile2,"]\n");   
            }
            
        fclose(pFile1);
        fclose(pFile2);

        return 0;
}
