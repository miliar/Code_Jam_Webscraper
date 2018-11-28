#include <cstdio>
#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;

FILE * pFile1, * pFile2;
int T, N, i, j, k, l, o, p, po, pb, result, z;
int O[100], B[100];
char y, parcours[100];
char col,color;

int main ()
{

        pFile1 = fopen ("A-large.in","r");
        pFile2 = fopen ("A-large.out","w");
        fscanf(pFile1, "%d", &T);
        for (i=1;i<=T;i++)
            {
                fscanf(pFile1, "%d", &N);
                fscanf(pFile1, "%c", &col);
                O[0]=1;
                B[0]=1;
                j=0;
                k=0;
                for (l=0;l<N;l++)
                {
                   fscanf(pFile1, "%c", &color);fscanf(pFile1, "%c", &col);
                   if (color=='O'){fscanf(pFile1, "%d", &z);O[j]=z;printf(" %c%d ->o",color,O[j]);j++;}else{fscanf(pFile1, "%d", &z);B[k]=z;printf(" %c%d ->b",color,B[k]);k++;}
                   fscanf(pFile1, "%c", &col);
                   parcours[l]= color;
                }
                po=1;
                pb=1;
                j=0;
                k=0;
                result=0;
                for(o=0;o<N;o++)
                    {
                     if (parcours[o]=='O')           
                      {
                       printf("O\n\n");
                       while (po!=O[j])
                          {
                             if(po<O[j]) po++; else {if(po!=O[j])po--;}
                             if(pb<B[k]) pb++; else {if(pb!=B[k])pb--;}
                             result++;
                          }
                       if(pb<B[k]) pb++; else {if(pb!=B[k])pb--;}
                       j++;
                       result++;
                      }else
                      {
                       printf("B\n\n");
                       while (pb!=B[k])
                          {
                             if(po<O[j]) po++; else {if(po!=O[j])po--;}
                             if(pb<B[k]) pb++; else {if(pb!=B[k])pb--;}
                             result++;
                          }
                       if(po<O[j]) po++; else {if(po!=O[j])po--;}
                       k++;
                       result++;
                      }                      
                    }
                fprintf (pFile2,"Case #%d: %d\n", i, result);
                
            }
            
        fclose(pFile1);
        fclose(pFile2);

        return 0;
}
